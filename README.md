# trii-technical-test

This project provides an API to fetch data from the Rick and Morty API and download the results as a ZIP file. The API is packaged in a Docker container for easy deployment and execution.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Docker Commands](#docker-commands)
- [Notes](#notes)

---

## Prerequisites

- **Docker:** Ensure you have Docker installed on your machine. You can download Docker from [here](https://www.docker.com/get-started).

---

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/jomorales1/trii-technical-test.git
    cd trii-technical-test
    ```

---

## Usage

1. **Run the Docker Container:**
    ```bash
    docker compose up
    ```

    This command will start the container and map port 8000 of the container to port 8000 on your local machine.

2. **Access the API:**

    - Open your web browser or use the postman collection under the docs directory and send a request to `http://localhost:8000/v1/search` to fetch Rick and Morty characters.
    - To download the results as a ZIP file, go to `http://localhost:8000/public/exports/<filename>`.

---

## API Endpoints

### 1. **Get Rick and Morty Characters**

- **URL:** `/v1/search`
- **Method:** `GET`
- **Description:** Fetches a list of characters from the Rick and Morty API.
- **Query Parameters:**
  - `page` (optional): Results page.
  - `name` (optional): Filter characters by name.
  - `status` (optional): Filter characters by their status (alive, dead, unknown).
  - `gender` (optional): Filter characters by gender (male, female, genderless, unknown).
  - `generate_zip` (optional): Boolean that Indicates if the results will be saved ito a zip file.

### 2. **Download Characters as ZIP**

- **URL:** `/public/exports/<filename>`
- **Method:** `GET`
- **Description:** Downloads a ZIP file containing the fetched character data where filename corresponds to the `zip_filename` field returned in the search response.

---

## Docker Commands

- **Stop the Container:**
    ```bash
    docker compose stop
    ```

- **Remove the Container:**
    ```bash
    docker compose down -v
    ```

- **Remove the Docker Image:**
    ```bash
    docker rmi trii-technical-test
    ```

---

## Notes

- Ensure that your Docker daemon is running before executing the commands.
- You can customize the query parameters in the API request to fetch specific character data.
