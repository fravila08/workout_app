
# API User Authentication

## Register

```http
  POST http://127.0.0.1:8000/api/v1/users/
```

| Parameter | Type     | Description                       | Example|
| :-------- | :------- | :-------------------------------- | :------|
| `email`      | `string` | **Required** Must end with @*.com | francisco@email.com|
| `username`   | `string` | **Required** username           | fravila08 |
|`password`    | `string` | **Required** Must contain 6-8 characters, 1 special, 1 numeric |P3r&3us|

> This endpoint will return your username and authentication token. Please ensure to make all requests with your authentication token under the `Authorization` header in your requests prepended by the word token. For example: `Autorization = Token abcw3432bcaw823dfw`

## Log In

```http
  POST http://127.0.0.1:8000/api/v1/users/login/
```

| Parameter | Type     | Description                       | Example|
| :-------- | :------- | :-------------------------------- | :------|
| `username`   | `string` | **Required** username           | fravila08 |
|`password`    | `string` | **Required** Must contain 6-8 characters, 1 special, 1 numeric |P3r&3us|

> This endpoint will return your username and authentication token. Please ensure to make all requests with your authentication token under the `Authorization` header in your requests prepended by the word token. For example: `Autorization = Token abcw3432bcaw823dfw`

## Log Out

```http
  GET http://127.0.0.1:8000/api/v1/users/logout/
```

| Header | Type | Description     | Example                |
| :--------| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Your API token | Token abcw3432bcaw823dfw |

> This endpoint will delete your current token and effectively sign you out of the application.

## Update Username or Password

```http
  PUT http://127.0.0.1:8000/api/v1/users/info/
```

**Headers**

| Header | Type | Description     | Example                |
| :--------| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Your API token | Token abcw3432bcaw823dfw |

**Parameters**

| Parameter | Type     | Description                       | Example|
| :-------- | :------- | :-------------------------------- | :------|
| `new_username`   | `string` | username           | fravila08 |
|`new_password`    | `string` | Must contain 6-8 characters, 1 special, 1 numeric |P3r&3us|
|`password`    | `string` | **Required** Must contain 6-8 characters, 1 special, 1 numeric |P3r&3us|

> This endpoint will update your current user information by confirming your password and changing the values you've provided.

## Get User Data

```http
  GET http://127.0.0.1:8000/api/v1/users/info/
```

| Header | Type | Description     | Example                |
| :--------| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Your API token | Token abcw3432bcaw823dfw |

> This endpoint will return your user information we are currently tracking to ensure you have a positive experience. None of this information will be shared with any outside parties and will only be utilized to better your interactions with this application.
