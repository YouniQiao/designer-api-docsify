# OnHttpErrorReceiveEvent

Represents the callback invoked when an HTTP error occurs during web page resource loading.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export declare interface OnHttpErrorReceiveEvent--><!--Device-unnamed-export declare interface OnHttpErrorReceiveEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceWeb, OnMessageEvent, OnPageEndEvent, OnHttpErrorReceiveEvent, OnLoadInterceptEvent, WebHeader, OnProgressChangeEvent, OnErrorReceiveEvent, OnPageBeginEvent, OnLoadInterceptCallback, AtomicServiceWebController } from 'kits/@kit.ArkUI';
```

## request

```TypeScript
request: WebResourceRequest
```

Web resource request of event.

**Type:** [WebResourceRequest](../../apis-arkweb/arkts-apis/arkts-arkweb-web-webresourcerequest-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnHttpErrorReceiveEvent-request: WebResourceRequest--><!--Device-OnHttpErrorReceiveEvent-request: WebResourceRequest-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## response

```TypeScript
response: WebResourceResponse
```

Web resource response of event.

**Type:** [WebResourceResponse](../../apis-arkweb/arkts-components/arkts-arkweb-webresourceresponse-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnHttpErrorReceiveEvent-response: WebResourceResponse--><!--Device-OnHttpErrorReceiveEvent-response: WebResourceResponse-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

