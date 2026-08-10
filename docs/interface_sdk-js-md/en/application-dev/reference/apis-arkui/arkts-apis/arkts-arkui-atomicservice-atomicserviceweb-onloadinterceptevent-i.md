# OnLoadInterceptEvent

定义Web组件加载url之前触发的加载拦截事件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export declare interface OnLoadInterceptEvent--><!--Device-unnamed-export declare interface OnLoadInterceptEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceWeb, OnMessageEvent, OnPageEndEvent, OnHttpErrorReceiveEvent, OnLoadInterceptEvent, WebHeader, OnProgressChangeEvent, OnErrorReceiveEvent, OnPageBeginEvent, OnLoadInterceptCallback, AtomicServiceWebController } from 'kits/@kit.ArkUI';
```

## data

```TypeScript
data: WebResourceRequest
```

网页请求的封装信息。

**Type:** [WebResourceRequest](../../apis-arkweb/arkts-apis/arkts-arkweb-web-webresourcerequest-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnLoadInterceptEvent-data: WebResourceRequest--><!--Device-OnLoadInterceptEvent-data: WebResourceRequest-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

