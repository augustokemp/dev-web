import api from "@/api";
import { Action, Module, Mutation, VuexModule } from "vuex-module-decorators";

import { ITool } from "@/interfaces/tool";
import { mainStore } from "..";
import _ from "lodash";

@Module({ name: "tool" })
export default class ToolModule extends VuexModule {
  public tools: ITool[] = [];

  @Mutation
  public setTools(payload: ITool[]) {
    this.tools = payload;
  }

  @Action
  public async getTools() {
    try {
      const response = await api.getTools(mainStore.token);
      if (response.data) {
        this.setTools(response.data);
      }
    } catch (error) {
      await mainStore.checkApiError(<any>error);
    }
  }
}
