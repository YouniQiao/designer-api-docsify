# HttpAuthHandler

HttpAuthHandler is a handler class used by the Web component to process HTTP authentication requests. When the server returns 401 Unauthorized to request authentication, the Web component obtains an HttpAuthHandler instance through the onHttpAuthRequest event callback, and the app decides whether to provide authentication credentials. For sample code, see [onHttpAuthRequest](arkts-arkweb-web-attribute.md#onhttpauthrequest).

**Since:** 9

<!--Device-unnamed-declare class HttpAuthHandler--><!--Device-unnamed-declare class HttpAuthHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## cancel

```TypeScript
cancel(): void
```

Cancels HTTP authentication as requested by the user.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpAuthHandler-cancel(): void--><!--Device-HttpAuthHandler-cancel(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## confirm

```TypeScript
confirm(userName: string, password: string): boolean
```

Performs HTTP authentication with the user name and password provided by the user.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpAuthHandler-confirm(userName: string, password: string): boolean--><!--Device-HttpAuthHandler-confirm(userName: string, password: string): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userName | string | Yes |
| password | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## constructor

```TypeScript
constructor()
```

Constructs an **HttpAuthHandler**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpAuthHandler-constructor()--><!--Device-HttpAuthHandler-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isHttpAuthInfoSaved

```TypeScript
isHttpAuthInfoSaved(): boolean
```

Checks whether the credentials stored for the current host are applicable. The credentials are not applicable if they have been rejected by the server in the current request.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpAuthHandler-isHttpAuthInfoSaved(): boolean--><!--Device-HttpAuthHandler-isHttpAuthInfoSaved(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
