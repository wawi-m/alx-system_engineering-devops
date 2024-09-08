 # My first postmortem

![Alt text](images/serverdown.gif)

## Incident Report on Apache server error

### Issue Summary
_Outage duration_ - July 9th, 2024, 19:25 EAT to July 9th, 2024, 20:00 EAT.

_Impact_ - "Empty reply from server" error when querying "Hello Holberton" page at port 8080.
Service was completely unavailable to 100% users during the outage.

_Root cause_ - incomplete install and configuration of Apache server in Docker container

### Timeline
- 19:25 EAT: Issue detected when the software engineer attempted to reach "Hello Holberton" webpage at `0:8080` but received `curl: (52) Empty reply from server` error, during a Docker container routine test.
- 19:35 EAT: Initial investigation showed the Docker container was running but returning an empty response from server. Assumptions were made that the issue might be related to container configuration or Apache service status. Detected incorrect response at port 8080 while looking for error source.
- 19:45 EAT: Investigated software install and configuration, checking Apache service status inside the container, and discovered that Apache was not installed or running.
- 19:55 EAT: Misleading debugging performed for correct network configurations and Docker port mappings.
- 20:00 EAT: Issue resolved by installing and configuring Apache within the container and setting up the default page. Confirmed that accessing the service at port 8080 returned the "Hello Holberton" page as expected. Engineer did not escalate the issue as it was unnecessary at this stage.
### Root Cause and Resolution 
* Root Cause: The Docker container was launched with an image that did not have Apache installed and correctly configured. Consequently, when one attempted to access the server, there was no service to respond to the requests.
* Resolution: A bash script was executed as follows to run Apache server.
 
#!/usr/bin/env bash

sudo apt-get -y update # To update package lists in the docker container.

sudo apt-get -y upgrade # To upgrade package lists in the docker container.

sudo apt-get -y install apache2 # To install Apache Server in the docker container

echo "Hello Holberton" | sudo tee -a /var/www/html/index.html # To create a default web page with the content "Hello Holberton".

sudo service apache2 restart # To restart Apache to apply the changes.

### Corrective and Preventative Measures
Improvements to ensure Docker-containers’ reliability and performance helps in identifying and resolving issues before they impact production environments, leading to smoother and more reliable deployments. These may include:

-	Ensure that Docker images used for deployment are correctly configured and tested before use.
-	Implement automated checks and validations for container readiness, including service availability, during the container build and deployment process.
  
**_Tasks to conduct._**
1.	Update Docker Image:
-  Modify Docker file: Revise the Docker file for the holbertonschool/265-0 image to include the installation and basic configuration of Apache. This might involve adding commands to install Apache, set up configuration files, and start the Apache service.

- 	Prevent Future Issues: By including Apache in the Docker file, you address issues related to missing configurations or outdated setups that can affect the container’s functionality. Ensure that the image is built and tested thoroughly after making changes.
    
2.	Add Automated Tests:
-  Integration of Tests: Implement automated tests to check for correct install and configuration of essential services like Apache. This can include:
- 	Unit Tests: Test individual components or configuration files.
- 	Integration Tests: Verify that Apache works correctly within the container and interacts properly with other services.
- 	End-to-End Tests: Simulate real-world scenarios to ensure the container performs well under expected conditions.
3.	Enhance Monitoring:
- 	Service Status Monitoring: Set up monitoring tools, such as Datadog to track the status of services within the container. This could involve:
- 	Logs: Aggregate and analyze logs to detect errors or issues.
- 	Metrics: Collect metrics on service performance, such as response times and error rates.
- 	Content Delivery Monitoring: Implement alerts for content delivery issues, such as broken links or incorrect content.
4.	Document Procedures:
- 	Verification Steps: Update internal documentation to include detailed steps for verifying container configurations. This should cover:
- 	Configuration Checks: How to ensure that environment variables, network settings, and file permissions are correct.
- 	Testing Procedures: Guidelines for running automated tests and interpreting results.
- 	Deployment Checklist: Provide a checklist for the deployment process that includes steps for configuration verification, testing, and monitoring setup.
