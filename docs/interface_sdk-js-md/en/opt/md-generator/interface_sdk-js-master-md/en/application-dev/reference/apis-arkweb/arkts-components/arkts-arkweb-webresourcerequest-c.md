# WebResourceRequest

WebResourceRequest is a class in the Web component that represents a network resource request, providing detailed metadata about the requested resource. This object is used in event callbacks such as `onErrorReceive`, `onHttpErrorReceive`, and request interception to help developers diagnose network errors, monitor request status, and implement resource interception control. By using this class, the app can improve error handling, enhance request controllability, and optimize user experience. For sample code, see [onErrorReceive event](arkts-arkweb-web-attribute.md#onerrorreceive).

**Since:** 8

<!--Device-unnamed-declare class WebResourceRequest--><!--Device-unnamed-declare class WebResourceRequest-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Constructs a **WebResourceRequest** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceRequest-constructor()--><!--Device-WebResourceRequest-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## getRequestHeader

```TypeScript
getRequestHeader(): Array<Header>
```

Obtains the information about the resource request header.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceRequest-getRequestHeader(): Array<Header>--><!--Device-WebResourceRequest-getRequestHeader(): Array<Header>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[Header](arkts-arkweb-header-i.md)&gt; |

## getRequestMethod

```TypeScript
getRequestMethod(): string
```

Obtains the request method.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceRequest-getRequestMethod(): string--><!--Device-WebResourceRequest-getRequestMethod(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getRequestUrl

```TypeScript
getRequestUrl(): string
```

Obtains the URL of the resource request.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceRequest-getRequestUrl(): string--><!--Device-WebResourceRequest-getRequestUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## isMainFrame

```TypeScript
isMainFrame(): boolean
```

Checks whether the resource request is for the main frame. Used to differentiate between main frame and subframe requests.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceRequest-isMainFrame(): boolean--><!--Device-WebResourceRequest-isMainFrame(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isRedirect

```TypeScript
isRedirect(): boolean
```

Checks whether the resource request is redirected by the server. Used to inspect the request redirect chain and identify malicious redirects.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceRequest-isRedirect(): boolean--><!--Device-WebResourceRequest-isRedirect(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isRequestGesture

```TypeScript
isRequestGesture(): boolean
```

Checks whether the resource request is associated with a gesture (such as a tap).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceRequest-isRequestGesture(): boolean--><!--Device-WebResourceRequest-isRequestGesture(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
