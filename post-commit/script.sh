#!/bin/bash

curl -s -S -i -X POST http://builds-for-managers-ykezyp-post-commit.apps.eu46a.prod.ole.redhat.com/api/builds -f -d 'developer=Dev&git=Git&project=proj'
