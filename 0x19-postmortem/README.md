 # My first postmortem
_{1. Make people want to read your postmortem
We are constantly stormed by a quantity of information, it’s tough to get people to read you.
Make your post-mortem attractive by adding humour, a pretty diagram or anything that would catch your audience attention.}_
## Incident Report on Apache server error

### Issue Summary
`Outage duration` - July 9th 2024 19:25 EAT to  July 9th 2024 20:00 EAT.

`Impact` - "Empty reply from server" error when querying "Hello Holberton" page at port 8080.
Service was completely unavailable to 100% users during the outage.

`Root cause` - incomplete install and configuration of Apache server in Docker container

### Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:

when was the issue detected
how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
misleading investigation/debugging paths that were taken
which team/individuals was the incident escalated to
how the incident was resolved
- 19:25 EAT: Issue detected when users reported receiving an empty reply from the server.
- 19:05 EAT: Detected through a monitoring alert indicating that port 8080 was not responding correctly.
- 19:10 EAT: Initial investigation showed the Docker container was running but returning an empty response. Assumptions were made that the issue might be related to container configuration or Apache service status.
- 19:15 EAT: Investigated Apache service status inside the container, discovering that Apache was not installed or running.
- 19:20 EAT: Misleading debugging paths included checking network configurations and Docker port mappings, which were correctly set.
- 19:25 EAT: Escalated to the DevOps team who further verified the Apache service was not installed or started within the container.
- 19:30 EAT: Issue resolved by installing and configuring Apache within the container. Confirmed that accessing the service at port 8080 returned the "Hello Holberton" page as expected.
### Root cause and resolution must contain:

explain in detail what was causing the issue
explain in detail how the issue was fixed
### Corrective and preventative measures must contain:

what are the things that can be improved/fixed (broadly speaking)
a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)

Be brief and straight to the point, between 400 to 600 words

While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.
