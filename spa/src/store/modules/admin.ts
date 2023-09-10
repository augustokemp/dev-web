import api from "@/api";
import { VuexModule, Module, Mutation, Action } from "vuex-module-decorators";
import { IUserProfile, IUserProfileCreate } from "@/interfaces/userProfile";
import _ from "lodash";
import { mainStore } from "@/utils/store-acessor";

@Module({ name: "admin" })
export default class AdminModule extends VuexModule {
  public users: IUserProfile[] = [];
  public usersSenior: IUserProfile[] = [];

  public user: IUserProfile = {
    email: "",
    is_active: true,
    is_admin: false,
    full_name: "",
    id: 0,
    addresses: [],
    user_tools: []
  };

  @Mutation
  public setUsers(payload: IUserProfile[]) {
    this.users = payload;
  }

  @Mutation
  public setUser(payload: IUserProfile) {
    this.user = payload;
  }

  @Action
  public async getUsers() {
    try {
      const response = await api.getUsers(mainStore.token);
      if (response) {
        this.setUsers(response.data);
      }
    } catch (error) {
      await mainStore.checkApiError(<any>error);
    }
  }

  @Action
  public async getUser(id: number) {
    try {
      const response = await api.getUser(mainStore.token, id);
      if (response) {
        this.setUser(response.data);
      }
    } catch (error) {
      await mainStore.checkApiError(<any>error);
    }
  }

  @Action
  public async createUser(payload: IUserProfileCreate) {
    const loadingNotification = { content: "Salvando", showProgress: true };
    try {
      mainStore.addNotification(loadingNotification);

      const result = await api.createUser(mainStore.token, payload);

      mainStore.removeNotification(loadingNotification);
      mainStore.addNotification({
        content: "Usuário criado com sucesso",
        color: "success",
      });
      return result.data.id;
    } catch (error: any) {
      mainStore.removeNotification(loadingNotification);
      mainStore.addNotification({
        content: error.response.data.detail,
        color: "error",
      });
      await mainStore.checkApiError(<any>error);
    }
  }
}
