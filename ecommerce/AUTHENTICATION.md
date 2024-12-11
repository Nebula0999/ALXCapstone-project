# Authentication Setup

## Overview
This API uses token-based authentication. Each user is issued a unique token that must be included in the `Authorization` header of every request to protected endpoints.

## How to Obtain a Token
1. Send a `POST` request to the `/api/v1/login/` endpoint with your username and password:
   
   '{"username": "testuser", "password": "password123"}'
