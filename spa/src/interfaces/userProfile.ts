export interface IUserProfile {
  id?: number;
  name?: string;
  email: string;
  is_active: boolean;
  is_superuser: boolean;
  full_name: string;
}

export interface IUserProfileCreate {
  email: string;
  password: string;
}

export interface IUserProfileUpdate extends IUserProfile {}
