# WebHttpCookie

Defines the Web's HTTPCookie.<p><strong>API Note</strong>:<br>The maximum length allowed for each attribute value in a cookie string is 1024.</p>

**Since:** 23

<!--Device-webview-interface WebHttpCookie--><!--Device-webview-interface WebHttpCookie-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## domain

```TypeScript
domain: string
```

Gets the domain of the cookie.

**Type:** string

**Since:** 23

<!--Device-WebHttpCookie-domain: string--><!--Device-WebHttpCookie-domain: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## expiresDate

```TypeScript
expiresDate: string
```

Gets the cookie's expiration date.

**Type:** string

**Since:** 23

<!--Device-WebHttpCookie-expiresDate: string--><!--Device-WebHttpCookie-expiresDate: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isHttpOnly

```TypeScript
isHttpOnly: boolean
```

Gets whether the current cookie is marked as HttpOnly.

**Type:** boolean

**Since:** 23

<!--Device-WebHttpCookie-isHttpOnly: boolean--><!--Device-WebHttpCookie-isHttpOnly: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isSecure

```TypeScript
isSecure: boolean
```

Gets whether the current cookie is marked as Secure.

**Type:** boolean

**Since:** 23

<!--Device-WebHttpCookie-isSecure: boolean--><!--Device-WebHttpCookie-isSecure: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isSessionCookie

```TypeScript
isSessionCookie: boolean
```

Gets if the cookie is session cookie.

**Type:** boolean

**Since:** 23

<!--Device-WebHttpCookie-isSessionCookie: boolean--><!--Device-WebHttpCookie-isSessionCookie: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## name

```TypeScript
name: string
```

Gets the cookie's name.

**Type:** string

**Since:** 23

<!--Device-WebHttpCookie-name: string--><!--Device-WebHttpCookie-name: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## path

```TypeScript
path: string
```

Gets the cookie's path.

**Type:** string

**Since:** 23

<!--Device-WebHttpCookie-path: string--><!--Device-WebHttpCookie-path: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## samesitePolicy

```TypeScript
samesitePolicy: WebHttpCookieSameSitePolicy
```

Gets the cookie's samesite policy.

**Type:** WebHttpCookieSameSitePolicy

**Since:** 23

<!--Device-WebHttpCookie-samesitePolicy: WebHttpCookieSameSitePolicy--><!--Device-WebHttpCookie-samesitePolicy: WebHttpCookieSameSitePolicy-End-->

**System capability:** SystemCapability.Web.Webview.Core

## value

```TypeScript
value: string
```

Gets the cookie's value.

**Type:** string

**Since:** 23

<!--Device-WebHttpCookie-value: string--><!--Device-WebHttpCookie-value: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

