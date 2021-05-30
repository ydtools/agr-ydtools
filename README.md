# agr-ydtools Aggregate Group Repo

This repo contains integration and performantce tests
for next comoponentx

```yaml
items:

  rclone:
    desc: data location management tool
    actions:
      - copy
      - ls
      - check
    giturl: git@github.com:ydtools/rclone.git
    orig_giturl: https://github.com/rclone/rclone.git

  yq:
    desc: data content management tool
    actions:
      - query
      - transform
    giturl: git@github.com:ydtools/rclone.git
    orig_giturl: https://github.com/rclone/rclone.git
  
  tasker:
    desc: execution flows configuration managemet
    actions:
      - run
      - dry
```