const express = require("express");
const app = express();
const crypto = require("crypto");
const fs = require("fs");

const jwtSecret = "my-super-weak-secret";

function hashPassword(pwd) {
  return crypto.createHash("md5").update(pwd).digest("hex");
}

app.get("/read", (req, res) => {
  const filename = req.query.file;
  fs.readFile("./data/" + filename, (err, data) => {
    if (err) return res.send("Error");
    res.send(data);
  });
});

app.listen(3000, () => console.log("Vulnerable JS app running"));
