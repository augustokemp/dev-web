const env = process.env.VUE_APP_ENV;

let envApiUrl = "";
let appNameEnv = "";

if (env == "production") {
  envApiUrl = `https://${process.env.VUE_APP_DOMAIN_PROD}`;
  appNameEnv = 'prod';
} else if (env == "staging") {
  envApiUrl = `https://${process.env.VUE_APP_DOMAIN_STAG}`;
  appNameEnv = 'staging';
} else {
  envApiUrl = `http://${process.env.VUE_APP_DOMAIN_DEV}`;
  appNameEnv = 'dev';
}
 
export const apiUrl = envApiUrl;
export const appName = env + ' ' + appNameEnv;
