package config

import (
	"fmt"
	"os"
)

const PORT = 8001

var DB_USERNAME = os.Getenv("DB_USERNAME")
var DB_PASSWORD = os.Getenv("DB_PASSWORD")
var DB_URL = os.Getenv("DB_URL")
var DB_NAME = os.Getenv("DB_NAME")
var DB_PORT = os.Getenv("DB_PORT")

var DB_CONNECTION_STRING = fmt.Sprintf("postgresql//%s:%s@%s:%s/%s", DB_USERNAME, DB_PASSWORD, DB_URL, DB_PORT, DB_NAME)
