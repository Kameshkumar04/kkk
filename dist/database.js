"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const sequelize_1 = require("sequelize");
const sequelize = new sequelize_1.Sequelize({
    dialect: "postgres",
    host: '192.168.0.210',
    port: 5432,
    database: 'spider',
    username: 'postgres',
    password: 'P@ssw0rd',
});
exports.default = sequelize;
//# sourceMappingURL=database.js.map