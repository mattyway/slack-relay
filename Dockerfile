FROM gliderlabs/alpine:edge

ENV slack_hook='https://hooks.slack.com/services/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'
ENV relay_port=80
ENV VIRTUAL_HOST='slack-relay.modius.io, slack-relay.dev'

RUN apk add --update \
    python \
    py-requests \
    py-twisted \
  && rm -rf /var/cache/apk/*

RUN mkdir /app
COPY code /app
WORKDIR /app

EXPOSE 80
CMD ["python", "relay.py"]