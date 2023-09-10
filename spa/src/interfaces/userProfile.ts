import { IAdress } from "./address";
import { IUserTool } from "./userTool";

export interface IUserProfile {
  id?: number;
  name?: string;
  email: string;
  is_active: boolean;
  is_admin: boolean;
  full_name: string;
  addresses: IAdress[];
  user_tools: IUserTool[];
}

export interface IUserProfileCreate {
  email: string;
  password: string;
}

export interface IUserProfileUpdate extends IUserProfile {}
