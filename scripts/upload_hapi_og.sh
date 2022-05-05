#/bin/bash

curl 'https://stu3.test.pyrohealth.net/fhir/Patient' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"' \
  -H 'Accept: application/json; charset=utf-8' \
  -H 'Prefer: return=representation' \
  -H 'Content-Type: application/json' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'Origin: https://fhir-drills.github.io' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://fhir-drills.github.io/' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  --data-raw $'{"resourceType":"Patient","maritalStatus":{"coding":[{"code":"M","display":"Married","system":"http://hl7.org/fhir/v3/MaritalStatus"}]},"text":{"status":"generated","div":"<div xmlns=\'http://www.w3.org/1999/xhtml\'>\\n  <p>Patient: Fhirman, Sam</p>\\n</div>"},"identifier":[{"system":"http://ns.electronichealth.net.au/id/hi/ihi/1.0","value":"8003608166690503","type":{"coding":[{"code":"NI","display":"National unique individual identifier","system":"http://hl7.org/fhir/v2/0203"}],"text":"IHI"}},{"system":"urn:oid:1.2.36.146.595.217.0.1","period":{"start":"2001-05-06"},"use":"usual","type":{"coding":[{"system":"http://hl7.org/fhir/v2/0203","code":"MR"}]},"assigner":{"display":"Acme Healthcare"},"value":"6666"}],"telecom":[{"system":"phone","use":"mobile","value":"+61481059995"}],"birthDate":"1973-09-30","gender":"male","address":[{"postalCode":"4000","use":"work","line":["400 George Street"],"city":"Brisbane","country":"AUS","state":"QLD"}],"name":[{"use":"official","text":"Sam Fhirman","prefix":["Mr"],"family":["Fhirman"],"given":["Sam"]}]}' \
  --compressed > /tmp/upload_response.txt



curl 'http://hapi.fhir.org/create' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: _ga=GA1.2.406339667.1651453496; _gid=GA1.2.107099177.1651714231; _gat=1; _gali=resource-create-btn' \
  -H 'Origin: http://hapi.fhir.org' \
  -H 'Referer: http://hapi.fhir.org/resource?serverId=home_r4&pretty=false&_summary=&resource=Patient' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36' \
  --data-raw 'serverId=home_r4&pretty=true&_summary=&resource=Patient&resource-create-id=abc123&resource-create-body=%7B%7D' \
  --compressed \
  --insecure
