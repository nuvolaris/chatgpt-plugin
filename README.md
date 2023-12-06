# A ChatGPT Plugin in Nuvolaris

The goal of this repo is to build a chatgpt-plugin implemented in Nuvolaris

At the moment we are experimenting with new ideas.

Our first working function queries GitHub to list projects for an organization, and it is working.

We are developing a function to prcesses Figma Files generating an user interface from a design.

Discuss your ideas and contributions in our forum.

https://nuvolaris.discourse.group/t/a-new-open-source-project-open-to-everyone-chatgpt-plugin-in-nuvolaris/79/1


## How to deploy the demo

Follow these steps to deploy the demo, in this case using the `nuvolaris.app` domain

```
# Setup 1st a nuvolaris chatgpt user
nuv adduser chatgpt <password> --all

# Login as user chatgpt (enter the password when requested)
nuv -login https://nuvolaris.app

# create a .env file setting a GITHUB_TOKEN env variable

# Deploy the project with
task deploy

# or alternatively with
export GITHUB_TOKEN=<token>;export CGPT_REDIS_URL=<redis_url>; export CGPT_REDIS_PREFIX=chatgpt: ; nuv gcp deploy

```
