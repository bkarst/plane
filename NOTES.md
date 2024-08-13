How to develop a backend endpoint. 

Startup front end code in development. 

From the root of `plane`, run `./setup.sh`

Go to a similar url, you want to develop. Copy the curl command for that url. 

get all issues
http://localhost/api/workspaces/polygen/issues/?order_by=sort_order&sub_issue=false&cursor=100:0:0&per_page=100

Cookie
session_key=418bc439-eca9-4c2a-8215-334a275551b0; csrftoken=435uCOaC6FtmraSIOjUcMYhmDlPMaDqe; plane-session-id=b26pqc19u6zevx5co9bmdvc7jcysatcs605u8n5gq1gexyffxh3uhv00gp4ewtwuuvcg8l9egep7s7ehhjc3dnkgtjk3tulq2184zg447k3wsujbu0jhm029n51dydk1

get my assigned issues
http://localhost/api/workspaces/polygen/issues/?assignees=46bacd92-2932-4ca1-a3b0-a8be25867bb5&order_by=sort_order&sub_issue=false&cursor=100:0:0&per_page=100

Get all issues for a project.
http://localhost/api/workspaces/polygen/projects/3a88eb36-1c68-41ff-8016-6c39e9d23f11/issues/?group_by=state_id&order_by=-created_at&sub_issue=true&cursor=30:0:0&per_page=30

People are invited to a workspace. 

Cookie
session_key=418bc439-eca9-4c2a-8215-334a275551b0; csrftoken=435uCOaC6FtmraSIOjUcMYhmDlPMaDqe; plane-session-id=b26pqc19u6zevx5co9bmdvc7jcysatcs605u8n5gq1gexyffxh3uhv00gp4ewtwuuvcg8l9egep7s7ehhjc3dnkgtjk3tulq2184zg447k3wsujbu0jhm029n51dydk1


manage.py set default environment there

python apiserver/manage.py djangoviz