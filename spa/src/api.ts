import { apiUrl } from "@/env";
import axios, { AxiosRequestConfig } from "axios";
import {
  IUserProfile,
  IUserProfileCreate,
  IUserProfileUpdate,
} from "./interfaces/userProfile";
import { ITool } from "./interfaces/tool";

const authHeaders = (token: string, formdata?: boolean) => {
  const config: AxiosRequestConfig = {
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": !formdata ? "application/json" : "multipart/form-data",
    },
  };

  return config;
};

const api = {
  async logInGetToken(username: string, password: string) {
    const params = new URLSearchParams();
    params.append("username", username);
    params.append("password", password);
    return axios.post(`${apiUrl}/api/v1/login/access-token/`, params);
  },
  async getMe(token: string) {
    return axios.get<IUserProfile>(
      `${apiUrl}/api/v1/users/me/`,
      authHeaders(token)
    );
  },
  async getUsers(token: string) {
    return axios.get<IUserProfile[]>(
      `${apiUrl}/api/v1/users/`,
      authHeaders(token)
    );
  },
  async getUser(token: string, userId: number) {
    if (!userId) return;
    return axios.get<IUserProfile>(
      `${apiUrl}/api/v1/users/${userId}/`,
      authHeaders(token)
    );
  },
  async createUser(
    token: string,
    data: IUserProfileCreate
  ): Promise<IUserProfile> {
    return axios.post(`${apiUrl}/api/v1/users/`, data, authHeaders(token));
  },
  async updateUser(
    token: string,
    id: number,
    data: IUserProfileUpdate
  ): Promise<IUserProfile> {
    return axios.put(`${apiUrl}/api/v1/users/${id}/`, data, authHeaders(token));
  },
  async deleteUser(token: string, id: number): Promise<Number> {
    return axios.delete(`${apiUrl}/api/v1/users/${id}/`, authHeaders(token));
  },
  async getTools(token: string) {
    return axios.get<ITool[]>(`${apiUrl}/api/v1/tools/`, authHeaders(token));
  },
};

export default api;
