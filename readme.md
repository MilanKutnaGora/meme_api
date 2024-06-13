# Meme API

## Overview

Meme API is a RESTful API for managing memes.

## Endpoints

### GET /memes

* Returns a list of all memes.
* Supports pagination.

### GET /memes/{id}

* Returns a specific meme by its ID.
* Returns a 404 if the meme is not found.

### POST /memes

* Creates a new meme.
* Requires a JSON body with the meme's image and text.
* Returns the created meme.

### PUT /memes/{id}

* Updates a specific meme by its ID.
* Requires a JSON body with the updated meme's image and text.
* Returns the updated meme.

### DELETE /memes/{id}

* Deletes a specific meme by its ID.
* Returns a 204 if the meme is deleted.

## Media Service

### POST /media

* Uploads a media file.
* Returns the uploaded media.

### GET /media/{id}

* Returns a specific media file by its ID.
* Returns a 404 if the media is not found.

### DELETE /media/{id}

* Deletes a specific media file by its ID.
* Returns a 204 if the media is deleted.

## S3 Storage

### POST /s3

* Uploads a file to S3.
* Returns the uploaded file.

### GET /s3/{key}

* Returns a specific file from S3 by its key.
* Returns a 404 if the file is not found.