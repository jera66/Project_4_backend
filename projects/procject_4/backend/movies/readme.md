# Project 4

####  A movie app by Jerathel Jean

## Project Summary

This is a full CRUD application on which the user is able to create, read, update, and delete movies.  It's made in Python Flask, Postgres and React

## Tell me what are you're building and what tools are you using?

I'm building a movie app  that's fully  CRUD  and MVP .  The user can add, update, delete, and see as many movies as they want.

## Route Table

List your routes in a table

| url             | method | action                                         |
| --------------- | ------ | -------------------------------------- |
| /movies/         | get    | get all movies (index)               |
| /movies/:id      | get    | get a particular movie (show)  |
| /movies/new      | get    | get a new movie (new)          |
| /movies          | post   | create a new movie                   |
| /movies/:id/edit | get    | edit a movie                           |
| /movies/:id      | put    | update a movie                        |
| /movies/:id      | delete | delete a movie                        |

## User Stories

User is able to perform the CRUD functionality.

## Challenges

My challenges include structuring the app. I was low on inspiration, not sure what I wanted the app to look like. Although, I had more than enough class materials, I still didn't know where to start and I had to watch some of the recordings in the recordings channel in Slack. It's very easy to feel overwhelmed when information keeps coming at you fast and furious. Also, I didn't feel well and I slept and rested most of the time. As a result, I missed presentation day.

- detail roadblocks and anything you did to overcome whether you did or didn't
  I didn't really run into any major roadblocks, the only issue I had was figuring out why my server wouldn't run and that ws fairly easy to fix.

## List of Technologies

Python
Flask
Postgres
React

### Dependencies

```python
################################################################################################
####                                                        DEPENDENCIES
################################################################################################
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import psycopg2
import os
```
