# telegram-chatops
Codebase of the app, its infra, and chat-bot which triggers the deployment

## Link to the bot: https://t.me/DeployTriggerBot

## Link to the simple-dimple-app: http://174.138.106.54:8080/

![my-infra](images/infra.jpg)

So, it is very simple. After making ``/deploy`` command - telegram-bot sends POST request to the GitHUB actions
which runs new workflow. It builds and pushes new image to the container registry.

After new image appears in the Container registry the rollout happens.

# Technologies - reasons:

* Python - I am on vacation with a few hours per day available to do this work, so I need something fast to write
* DigitalOcean - No experience, I want to try
* GitHUB Actions - the same as DO
* Terraform - nice tool to rollout new infra very quickly and also no one knows where is my tfstate (haha)
* Kubernetes - HA, easy to scale (that simple-dimple app) and a lot of features
* Lens - I've used to it and also I like its monitoring windows 
* Monitoring - installed on the DO, here is my monitoring pods:

![my-monitoring](images/monit.png)
