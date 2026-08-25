# @system.fetch

## Modules to Import

```TypeScript
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Fetch](arkts-network-system-fetch-fetch-depr-c.md) | **Table 1** Mapping between data and Content-Type  \| data \| Content-Type \| Description\| \| -------- \| -------- \| -------- \| \| string \| Left unspecified\| The default value of Content-Type is **text/plain**, and the value of data is used as the request body.\| \| string \| Any type\| The value of data is used as the request body.\| \| Object \| Left unspecified\| The default value of **Content-Type** is **application/x-www-form-urlencoded**. The **data** value is encoded based on the URL rule and appended in the request body.\| \| Object \| application/x-www-form-urlencoded \| The value of data is encoded based on the URL rule and is used as the request body.\|

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FetchResponse](arkts-network-system-fetch-fetchresponse-depr-i.md) | **Table 2** Mapping between responseType and data in success callback  \| responseType \| data \| Description\| \| -------- \| -------- \| -------- \| \| N/A\| string \| When the type in the header returned by the server is **text/\***, **application/json**, **application/javascript**, or **application/xml**, the value is the text content.\| \| text \| string \| Text content.\| \| json \| Object \| A JSON object.\|
