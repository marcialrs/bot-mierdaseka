curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer ASDASDASD" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/marcialrs/bot-mierdaseka/pulls/33 \
  -d '{"milestone": 9913011}'

curl -X GET "https://api.github.com/repos/marcialrs/bot-mierdaseka/milestones/3" \
  -H "Authorization: token ADASDASDASD" \
  -H "Accept: application/vnd.github.v3+json"

