# WebSchemeHandlerRequest

Defines the Web resource request used for scheme handler.

**Since:** 12

**Deprecated since:** -1

<!--Device-webview-class WebSchemeHandlerRequest--><!--Device-webview-class WebSchemeHandlerRequest-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## getFrameUrl

```TypeScript
getFrameUrl(): string
```

Gets the URL of frame which trigger this request.

**Since:** 12

**Deprecated since:** -1

<!--Device-WebSchemeHandlerRequest-getFrameUrl(): string--><!--Device-WebSchemeHandlerRequest-getFrameUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getHeader

```TypeScript
getHeader(): Array<WebHeader>
```

Gets request headers.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerRequest-getHeader(): Array<WebHeader>--><!--Device-WebSchemeHandlerRequest-getHeader(): Array<WebHeader>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;WebHeader & gt; |

## getHttpBodyStream

```TypeScript
getHttpBodyStream(): WebHttpBodyStream | null
```

Get http body stream.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerRequest-getHttpBodyStream(): WebHttpBodyStream | null--><!--Device-WebSchemeHandlerRequest-getHttpBodyStream(): WebHttpBodyStream | null-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebHttpBodyStream](arkts-arkweb-webview-webhttpbodystream-c.md) |

## getReferrer

```TypeScript
getReferrer(): string
```

Get referrer of request.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerRequest-getReferrer(): string--><!--Device-WebSchemeHandlerRequest-getReferrer(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getRequestMethod

```TypeScript
getRequestMethod(): string
```

Get request method.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerRequest-getRequestMethod(): string--><!--Device-WebSchemeHandlerRequest-getRequestMethod(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getRequestResourceType

```TypeScript
getRequestResourceType(): WebResourceType
```

Get request's resource type.

**Since:** 12

**Deprecated since:** -1

<!--Device-WebSchemeHandlerRequest-getRequestResourceType(): WebResourceType--><!--Device-WebSchemeHandlerRequest-getRequestResourceType(): WebResourceType-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebResourceType](arkts-arkweb-webview-webresourcetype-e.md) |

## getRequestUrl

```TypeScript
getRequestUrl(): string
```

Gets the request URL.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerRequest-getRequestUrl(): string--><!--Device-WebSchemeHandlerRequest-getRequestUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## hasGesture

```TypeScript
hasGesture(): boolean
```

Check whether the request is associated with gesture.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerRequest-hasGesture(): boolean--><!--Device-WebSchemeHandlerRequest-hasGesture(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isMainFrame

```TypeScript
isMainFrame(): boolean
```

Check whether the request is for getting the main frame.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerRequest-isMainFrame(): boolean--><!--Device-WebSchemeHandlerRequest-isMainFrame(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
