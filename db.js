import mysql from "mysql2/promise";
import fs from "fs";
import path from "path";

export const pool = mysql.createPool({
  host: "gateway01.ap-northeast-1.prod.aws.tidbcloud.com",
  port: 4000,
  user: "3TJFdzBsW6BQcdA.root",
  password: "FcuHmsVgzsXf1Bwz",
  database: "nextvortfolio",
  ssl: {
    ca:   fs.readFileSync(path.join(process.cwd(), "isrgrootx1.pem")), // put file in project root
  },
});
