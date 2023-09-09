import copy
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from app import models
from app.db.base_class import Base
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import Date, cast, func
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, **kwargs) -> Optional[ModelType]:
        queries = []

        for filter in kwargs:
            queries.append(getattr(self.model, filter) == kwargs.get(filter))

        return db.query(self.model).filter(*queries).first()

    def get_multi(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 5000,
        current_user=None,
        **kwargs,
    ) -> List[ModelType]:
        queries = []
        data_inicial = kwargs.pop('data_inicial', None)
        data_final = kwargs.pop('data_final', None)
        order_by = kwargs.pop('order_by', None)
        order_dir = kwargs.pop('order_dir', None)

        if current_user:
            queries.append(self.model.company_id == current_user.company_id)
            kwargs.pop('current_user', None)

        if hasattr(self.model, 'created_at') and data_final and data_inicial:
            if data_inicial:
                queries.append(func.date(self.model.created_at)
                               >= data_inicial)
                queries.append(func.date(self.model.created_at) <= data_final)

        for filter in kwargs:
            queries.append(getattr(self.model, filter) == kwargs.get(filter))

        query = db.query(self.model).filter(*queries)

        if order_by:
            if order_dir == 'desc':
                query = query.order_by(order_by.desc())
            else:
                query = query.order_by(order_by)
        elif hasattr(self.model, 'created_at'):
            return db.query(self.model).filter(
                *queries
            ).order_by(self.model.created_at.desc()).offset(skip).limit(limit).all()
        else:
            return db.query(self.model).filter(*queries).offset(skip).limit(limit).all()

    def create(
        self,
        db: Session,
        current_user: models.User = None,
        additional_log_info: dict = {},
        log_model_id: str = None,
        *,
        obj_in: CreateSchemaType,
    ) -> ModelType:
        db.expire_on_commit = False
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore

        if hasattr(db_obj, 'created_by_id') and current_user:
            db_obj.created_by_id = current_user.id

        if hasattr(db_obj, 'created_by_name') and current_user:
            db_obj.created_by_name = current_user.full_name

        db.add(db_obj)
        db.commit()

        db.refresh(db_obj)
        obj_return = copy.deepcopy(db_obj)

        if current_user:
            model_id = db_obj.id

            if log_model_id:
                model_id = log_model_id

            db_obj_log = models.Log(
                model=self.model.__name__,
                model_id=model_id,
                data=jsonable_encoder({**obj_in_data, **additional_log_info}),
                created_by_id=current_user.id,
                created_by_name=current_user.full_name,
                allowed_by_id=None,
                allowed_by_name=None,
            )
            db.add(db_obj_log)
            db.commit()
            db.refresh(db_obj_log)

        return obj_return

    def update(
        self,
        db: Session,
        current_user: models.User = None,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
        additional_log_info: dict = {},
        log_model_id: str = None,
    ) -> ModelType:
        db.expire_on_commit = False
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        # obj_return = copy.deepcopy(db_obj)
        if current_user:
            model_id = db_obj.id

            if log_model_id:
                model_id = log_model_id

            db_obj_log = models.Log(
                model=self.model.__name__,
                model_id=model_id,
                data=jsonable_encoder({**update_data, **additional_log_info}),
                created_by_id=current_user.id,
                created_by_name=current_user.full_name,
                allowed_by_id=None,
                allowed_by_name=None,
            )
            db.add(db_obj_log)
            db.commit()
            db.refresh(db_obj_log)

        return db_obj

    def remove(self, db: Session, current_user: models.User = None, log_model_id: str = None, **kwargs) -> ModelType:
        queries = []

        for filter in kwargs:
            queries.append(getattr(self.model, filter) == kwargs.get(filter))

        obj = db.query(self.model).filter(*queries).first()
        obj_data = jsonable_encoder(obj)
        db.delete(obj)
        db.commit()

        if current_user:
            model_id = obj.id

            if log_model_id:
                model_id = log_model_id

            db_obj_log = models.Log(
                model=self.model.__name__,
                model_id=model_id,
                data=jsonable_encoder(obj),
                created_by_id=current_user.id,
                created_by_name=current_user.full_name,
                allowed_by_id=None,
                allowed_by_name=None,
            )
            db.add(db_obj_log)
            db.commit()
            db.refresh(db_obj_log)

        return obj

    def remove_multi(self, db: Session, current_user: models.User = None, **kwargs) -> ModelType:
        queries = []

        for filter in kwargs:
            queries.append(getattr(self.model, filter) == kwargs.get(filter))

        obj_list = db.query(self.model).filter(*queries).all()

        for obj in obj_list:
            db.delete(obj)
            db.commit()

            if current_user:
                db_obj_log = models.Log(
                    model=self.model.__name__,
                    model_id=obj.id,
                    data=jsonable_encoder(obj),
                    created_by_id=current_user.id,
                    created_by_name=current_user.full_name,
                    allowed_by_id=None,
                    allowed_by_name=None,
                )
                db.add(db_obj_log)
                db.commit()
                db.refresh(db_obj_log)

        return obj_list
