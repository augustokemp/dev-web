import { apiUrl } from "@/env";
import axios from "axios";
import { IUserProfile, IUserProfileCreate } from "./interfaces/userProfile";

function authHeaders(token: string) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "multipart/form-data",
    },
  };
}

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
  async createUser(token: string, data: IUserProfileCreate) {
    return axios.post(`${apiUrl}/api/v1/users/`, data, authHeaders(token));
  },
};

export default api;
