 System Installation.
        ◦ For this project , frappe docker is being used to setup the environment. Steps are as mentioned below:-          
            1. To start some pre-requisite must be met. These include 
                I. docker being installed in the current system
                II. docker-compose installed in the system
            2. First open the terminal .Before the next step git has to be configured for specifically email and user.
            3. Clone the frappe_docker directory via - git clone https://github.com/frappe/frappe_docker.git and enter the frappe_docker  directory with cd frappe_docker
            4. In the frappe_docker directory open vscode.
            5. Install Docker extension and Dev container Extension in vscode via visual studio marketplace
            6. After installation , press (Ctrl+Shift+P) , a command palette appears and click “Dev Containers:Reopen in Container” option.
            7. After inside the container . Check for git status , node -v , python –version  to verify dependencies and their versions
            8. Open terminal in vscode and type bench init –frappe-bench . This will install the latest version of frappe.
               Note: I am using version 14 for the system
            9. Enter cd frappe-bench
            10. Run the following commands to setup mariadb , redis-cache , redis_queue , redis_socketio and also specifying the ports on which other services will be running
                I. bench set-config -g db_host mariadb
                II. bench set-config -g redis_cache redis://redis-cache:6379
                III. bench set-config -g redis_queue redis://redis-queue:6379
                IV. bench set-config -g redis_socketio redis://redis-queue:6379
            11. After the above steps create a new site with the command – bench new-site sitename.
               Note: Because I am using a local environment to run the container, the sitename has to be in the format of “sitename.localhost” 
            12. Provide the default sql password . 
            13. Setup the administrator password and confirm it
            14. To setup the developer mode enter the command :- bench –site {sitename} set-config developer_mode 1
            15. Get the apps necessary for upcoming development. I am using erpnext to get the access to the customer doctype. So use this command to get erpnext : bench get-app erpnext
            16. Install the app to the site : bench –site {sitename} install-app erpnext
            17. I am creating a custom app called test_Sukalyan as per requirements and installing that into the site with the above mentioned command(Point 16)
            18. After this enter bench start to start the application(By default it runs on Port 8000). And open it in browser with {sitename}:8000
                   Reference
