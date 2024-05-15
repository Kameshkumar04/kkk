import * as dotenv from 'dotenv';
dotenv.config({
  path: '${__dirname}/../.env'
});

var paths = '${__dirname}/../.env';
console.log(paths);
export const port = Number(process.env.API_PORT);//3000
export const db_host = String(process.env.DB_HOST); //192.168.0.210
export const db_port = Number(process.env.DB_PORT); //5432
export const db_name = String(process.env.DB_NAME); //spider
export const db_user = String(process.env.DB_USER); //postgres
export const db_password = String(process.env.DB_PASSWORD); //P@ssw0rd