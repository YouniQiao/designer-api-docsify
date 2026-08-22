# HttpAuthHandler

Defines the http auth request result, related to [onHttpAuthRequest](arkts-web-attribute.md#onhttpauthrequest) method.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class HttpAuthHandler--><!--Device-unnamed-export declare class HttpAuthHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## cancel

```TypeScript
cancel(): void
```

cancel.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-HttpAuthHandler-cancel(): void--><!--Device-HttpAuthHandler-cancel(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## confirm

```TypeScript
confirm(userName: string, password: string): boolean
```

confirm.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-HttpAuthHandler-confirm(userName: string, password: string): boolean--><!--Device-HttpAuthHandler-confirm(userName: string, password: string): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userName | string | Yes |  |
| password | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-HttpAuthHandler-constructor()--><!--Device-HttpAuthHandler-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isHttpAuthInfoSaved

```TypeScript
isHttpAuthInfoSaved(): boolean
```

isHttpAuthInfoSaved.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-HttpAuthHandler-isHttpAuthInfoSaved(): boolean--><!--Device-HttpAuthHandler-isHttpAuthInfoSaved(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

