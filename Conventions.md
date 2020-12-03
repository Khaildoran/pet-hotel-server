# Description
This document houses the conventions we will use to ensure our code is unified and formatted that same way.

## Redux

### Saga Type Formats
GET routes: `FETCH_REDUCER-NAME`
POST routes: `PUSH_REDUCER-NAME`
PUT routes: `UPDATE_REDUCER-NAME`
DELETE routes: `DELETE_REDUCER-NAME`

### Reducer Type Formats
POST routes: `SET_REDUCER-NAME`
Additional routes: `SET_REDUCER-NAME_SPECIFIC-CASE`

## API

### Route Formats
Server routes `/api/TABLE-NAME`

## SQL

### Column and Table Names
These should be surrounded by double quotes, eg. `'SELECT * FROM "user" WHERE "id" = %s;'`

