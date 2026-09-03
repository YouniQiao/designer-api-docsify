# ArkWeb_ResourceHandler_

```c
typedef struct ArkWeb_ResourceHandler_ ArkWeb_ResourceHandler
```

## Overview

The ArkWeb_ResourceHandler struct is a resource handler for processing intercepted scheme requests. AfterArkWeb_SchemeHandler intercepts a request of a specified scheme, this struct can be used to return custom responsedata to the Web component, including the response status code, response headers, and response body. This struct ispassed as a parameter in the onRequestStart callback, through which developers can implement fully custom responsesto intercepted requests.

**Since**: 12

**Related module**: [Web](capi-web.md)

**Header file**: [arkweb_scheme_handler.h](capi-arkweb-scheme-handler-h.md)

