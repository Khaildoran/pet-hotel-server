CREATE DATABASE "pets_hotel";

CREATE TABLE "owners" (
	"id" serial NOT NULL,
	"first_name" varchar(255) NOT NULL,
	"last_name" varchar(255) NOT NULL,
	CONSTRAINT "owners_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "pets" (
	"id" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	"breed" varchar(255) NOT NULL,
	"color" varchar(255) NOT NULL,
	"is_checked_in" BOOLEAN NOT NULL,
	"owner_id" integer NOT NULL,
	CONSTRAINT "pets_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

ALTER TABLE "pets" ADD CONSTRAINT "pets_fk0" FOREIGN KEY ("owner_id") REFERENCES "owners"("id"); 