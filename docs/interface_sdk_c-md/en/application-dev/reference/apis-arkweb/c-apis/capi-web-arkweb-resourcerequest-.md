# ArkWeb_ResourceRequest_

```c
typedef struct ArkWeb_ResourceRequest_ ArkWeb_ResourceRequest
```

## Overview

ArkWeb_ResourceRequest is a struct that contains detailed information about an intercepted scheme request,including the request URL, HTTP method, request headers, and other metadata. This struct is passed as a parameter inthe onRequestStart callback of ArkWeb_SchemeHandler and is applicable to scenarios such as custom protocol handlingand resource interception. It helps developers implement features like cross-origin request control and localresource mapping, thereby enhancing security and performance. Developers can use it to obtain complete informationabout the intercepted request and decide whether to intercept it and how to construct a custom response.

**Since**: 12

**Related module**: [Web](capi-web.md)

**Header file**: [arkweb_scheme_handler.h](capi-arkweb-scheme-handler-h.md)

