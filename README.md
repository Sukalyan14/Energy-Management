# System Installation

For this project, Frappe Docker is being used to set up the environment. Follow the steps below:

## Prerequisites
- Docker installed in the current system
- Docker-compose installed in the system

## Installation Steps

1. Open the terminal. Before proceeding, configure git with your email and username.

2. Clone the Frappe Docker repository:
   ```bash
   git clone https://github.com/frappe/frappe_docker.git
   cd frappe_docker
   ```

3. Open VSCode in the frappe_docker directory.

4. Install the following VSCode extensions:
   - Docker Extension
   - Dev Container Extension

5. After installation, press `Ctrl+Shift+P` to open the command palette and select "Dev Containers: Reopen in Container".

6. Once inside the container, verify dependencies and their versions:
   ```bash
   git status
   node -v
   python --version
   ```

7. Open terminal in VSCode and initialize Frappe bench:
   ```bash
   bench init --frappe-bench
   ```
   Note: Version 14 is being used for this system.

8. Enter the frappe-bench directory:
   ```bash
   cd frappe-bench
   ```

9. Run the following commands to set up services with their respective ports:
   ```bash
   bench set-config -g db_host mariadb
   bench set-config -g redis_cache redis://redis-cache:6379
   bench set-config -g redis_queue redis://redis-queue:6379
   bench set-config -g redis_socketio redis://redis-queue:6379
   ```

10. Create a new site:
    ```bash
    bench new-site sitename.localhost
    ```
    Note: Because a local environment is being used to run the container, the sitename must be in the format "sitename.localhost"

11. Provide the default SQL password when prompted.

12. Set up the administrator password and confirm it.

13. Enable developer mode:
    ```bash
    bench --site sitename.localhost set-config developer_mode 1
    ```

14. Install ERPNext to access the customer doctype:
    ```bash
    bench get-app erpnext
    bench --site sitename.localhost install-app erpnext
    ```

15. Create and install a custom app called test_Sukalyan:
    ```bash
    bench --site sitename.localhost install-app test_Sukalyan
    ```

16. Start the application:
    ```bash
    bench start
    ```
    By default, it runs on Port 8000. Open in browser with `sitename.localhost:8000`.
