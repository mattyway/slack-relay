# Slack Relay

A simple relay of Docker Hub post build webhook payloads to a Slack Channel.

Available on Docker Hub at `daemonite/slack-relay:latest`. Configured via ENV variables.

## Installation

1. set up your outgoing Docker Hub webhooks to point at your Slack-Relay URL; for example, http://slack-relay.myweb.com/relay
2. set up an Incoming Webhook for your Slack team
3. run the Slack Relay container with environment variables pointing at your Slack integration

## Environment Variables

**SLACK_HOOK**
The URL of the Incoming Webhook integration you have set up for your Slack team.

**RELAY_PORT**
Defaults to port 80.  Only needed if you intend to relay on a different port.

## Sample Tutum Stack

```
slack-relay:
  image: 'daemonite/slack-relay:latest'
  environment:
    - 'SLACK_HOOK=https://hooks.slack.com/services/MY/SLACK/HOOK'
    - RELAY_PORT=80
    - VIRTUAL_HOST=slack-relay.someday.io
  tags:
    - prod
```

## Building Locally

If you have Vagrant installed, you can run up a local development environment for the container with `vagrant up slacker`

(h/t https://github.com/matsengrp/relay)
