# ArkWeb_RequestHeaderList_

```c
typedef struct ArkWeb_RequestHeaderList_ ArkWeb_RequestHeaderList
```

## Overview

ArkWeb_RequestHeaderList is an HTTP request header list struct used to represent and manage a collection ofkey-value pairs of HTTP request headers in the ArkWeb NDK. This struct contains a request header array (headers) andthe array length (headerCount), where headers is a pointer array of ArkWeb_RequestHeader and headerCount indicatesthe number of elements in the array. This struct is used together with ArkWeb_ResourceRequest and other structs toprovide the capability of reading and setting network request headers for Web components. Use cases: processing HTTPrequest headers in a custom protocol handler, modifying request headers in a network request interceptor, addingauthentication headers in API authentication scenarios, and configuring request headers in scenarios such as cachecontrol and content negotiation.

**Since**: 12

**Related module**: [Web](capi-web.md)

**Header file**: [arkweb_scheme_handler.h](capi-arkweb-scheme-handler-h.md)

