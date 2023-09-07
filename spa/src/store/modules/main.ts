import api from "@/api";
import { IAppNotification } from "@/interfaces/appNotification";
import { IUserProfile } from "@/interfaces/userProfile";
import router from "@/router";
import { getLocalToken, removeLocalToken, saveLocalToken } from "@/utils";
import { AxiosError } from "axios";
import { Action, Module, Mutation, VuexModule } from "vuex-module-decorators";

import { UNAUTHORIZED } from "http-status-codes";

@Module({ name: "main" })
export default class MainModule extends VuexModule {
  public token = "";

  public isLoggedIn: boolean | null = null;

  public logInError = false;

  public sendPassword = false;

  public userProfile: IUserProfile | null = null;

  public dashboardMiniDrawer = false;

  public dashboardShowDrawer = true;

  public notifications: IAppNotification[] = [];

  get hasAdminAccess() {
    return (
      this.userProfile &&
      this.userProfile.is_superuser &&
      this.userProfile.is_active
    );
  }

  get firstNotification() {
    if (this.notifications) {
      return this.notifications.length > 0 && this.notifications[0];
    }
  }

  @Mutation
  public setToken(payload: string) {
    this.token = payload;
  }

  @Mutation
  public setLoggedIn(payload: boolean) {
    this.isLoggedIn = payload;
  }

  @Mutation
  public setLogInError(payload: boolean) {
    this.logInError = payload;
  }

  @Mutation
  public setSendPassword(payload: boolean) {
    this.sendPassword = payload;
  }

  @Mutation
  public setUserProfile(payload: IUserProfile) {
    this.userProfile = payload;
  }

  @Mutation
  public setDashboardMiniDrawer(payload: boolean) {
    this.dashboardMiniDrawer = payload;
  }

  @Mutation
  public setDashboardShowDrawer(payload: boolean) {
    this.dashboardShowDrawer = payload;
  }

  @Mutation
  public setNotification(payload: IAppNotification[]) {
    this.notifications = payload;
  }

  @Mutation
  public addNotification(payload: IAppNotification) {
    if (this.notifications.length > 0) {
      if (
        this.notifications[this.notifications.length - 1].content !==
        payload.content
      ) {
        this.notifications.push(payload);
      }
    } else {
      this.notifications.push(payload);
    }
  }

  @Mutation
  public removeNotification(payload: IAppNotification) {
    this.notifications = this.notifications.filter(
      (notification) => notification !== payload
    );
  }

  @Action
  public async logIn(payload: { username: string; password: string }) {
    try {
      const response = await api.logInGetToken(
        payload.username,
        payload.password
      );
      const token = response.data.access_token;
      if (token) {
        saveLocalToken(token);
        this.setToken(token);
        this.setLoggedIn(true);
        this.setLogInError(false);
        await this.getUserProfile();
        await this.routeLoggedIn();
        this.addNotification({
          content: "Login efetuado com sucesso!",
          color: "success",
        });
      } else {
        await this.logOut();
      }
    } catch (err) {
      const error: any = err;

      if (error.response.status === 403) {
        location.reload();
      }

      this.addNotification({
        content: error.response.data.detail || "E-mail ou senha incorretos.",
        color: "error",
      });
      this.setLogInError(true);
      await this.logOut();
    }
  }

  @Action
  public async getUserProfile() {
    try {
      const response = await api.getMe(this.token);
      if (response.data) {
        this.setUserProfile(response.data);
      }
    } catch (error) {
      await this.checkApiError(<any>error);
    }
  }

  @Action
  public async checkLoggedIn() {
    if (!this.isLoggedIn) {
      let token = this.token;
      if (!token) {
        const localToken = getLocalToken();
        if (localToken) {
          this.setToken(localToken);
          token = localToken;
        }
      }
      if (token) {
        try {
          const response = await api.getMe(token);
          this.setLoggedIn(true);
          this.setUserProfile(response.data);
        } catch (error) {
          await this.removeLogIn();
        }
      } else {
        await this.removeLogIn();
      }
    }
  }

  @Action
  public async removeLogIn() {
    removeLocalToken();
    this.setToken("");
    this.setLoggedIn(false);
  }

  @Action
  public async logOut() {
    await this.removeLogIn();
    await this.routeLogOut();
  }

  @Action
  public async userLogOut() {
    await this.logOut();
    this.addNotification({
      content: "Você foi deslogado com sucesso!",
      color: "success",
    });
  }

  @Action
  public async routeLogOut() {
    if (router.currentRoute.path !== "/login") {
      router.push("/login");
    }
  }

  @Action
  public async checkApiError(payload: AxiosError) {
    if (payload.response && payload.response.status === UNAUTHORIZED) {
      await this.logOut();
    }

    if (payload.request) {
      if (payload.request.status === 405) {
        window.location.href = "/main/dashboard";
      }
    }
  }

  @Action
  public async routeLoggedIn() {
    if (
      router.currentRoute.path === "/login/" ||
      router.currentRoute.path === "/login" ||
      router.currentRoute.path === "/"
    ) {
      router.push("/main");
    }
  }

  @Action
  public async removeNotificationDelayed(payload: {
    notification: IAppNotification;
    timeout: number;
  }) {
    return new Promise((resolve) => {
      setTimeout(() => {
        this.removeNotification(payload.notification);
        resolve(true);
      }, payload.timeout);
    });
  }
}
