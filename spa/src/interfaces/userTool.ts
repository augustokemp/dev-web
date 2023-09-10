import { ITool } from "./tool";

export interface IUserTool {
  id?: number;
  allow_create: boolean;
  allow_read: boolean;
  allow_update: boolean;
  allow_delete: boolean;
  tool: ITool;
}
