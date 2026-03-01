package main

import (
	"context"
	"log"
	"scheduling_service/config"

	"github.com/jackc/pgx/v5/pgxpool"
)

var db *pgxpool.Pool

func getDb() {
	uri := config.DB_CONNECTION_STRING

	config, err := pgxpool.ParseConfig(uri)
	if err != nil {
		log.Fatal(err)
	}

	db, err := pgxpool.NewWithConfig(context.Background(), config)
	if err != nil {
		log.Fatal(err)
	}

}
