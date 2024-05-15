import { Sequelize } from 'sequelize';

const sequelize = new Sequelize({
    dialect:"postgres",
    host:'192.168.0.210',
    port:5432,
    database:'spider',
    username:'postgres',
    password:'P@ssw0rd',
})

export default sequelize;