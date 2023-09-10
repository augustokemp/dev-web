import { IAddress } from "./address";
import { IUserTool } from "./userTool";

export interface IUserProfile {
  id?: number;
  name?: string;
  email: string;
  is_active: boolean;
  is_admin: boolean;
  full_name: string;
  addresses: IAddress[];
  user_tools?: IUserTool[];
}

export interface IUserProfileCreate extends IUserProfile {
  email: string;
  password: string;
  confirmPassword: string;
}

export interface IUserProfileUpdate extends IUserProfile {}
