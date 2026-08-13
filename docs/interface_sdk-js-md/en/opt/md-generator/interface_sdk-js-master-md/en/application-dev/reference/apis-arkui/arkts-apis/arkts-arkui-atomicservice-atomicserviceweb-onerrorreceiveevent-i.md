# OnErrorReceiveEvent

Represents the callback invoked when an error occurs during web page loading.

**Since:** 12

**Deprecated since:** -1

<!--Device-unnamed-export declare interface OnErrorReceiveEvent--><!--Device-unnamed-export declare interface OnErrorReceiveEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceWeb, OnMessageEvent, OnPageEndEvent, OnHttpErrorReceiveEvent, OnLoadInterceptEvent, WebHeader, OnProgressChangeEvent, OnErrorReceiveEvent, OnPageBeginEvent, OnLoadInterceptCallback, AtomicServiceWebController } from '@kit.ArkUI';
```

## error

```TypeScript
error: WebResourceError
```

Web resource error of event.

**Type:** [WebResourceError](../../apis-arkweb/arkts-components/arkts-arkweb-webresourceerror-c.md)

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnErrorReceiveEvent-error: WebResourceError--><!--Device-OnErrorReceiveEvent-error: WebResourceError-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## request

```TypeScript
request: WebResourceRequest
```

Web resource request of event.

**Type:** [WebResourceRequest](../../apis-arkweb/arkts-components/arkts-arkweb-webresourcerequest-c.md)

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnErrorReceiveEvent-request: WebResourceRequest--><!--Device-OnErrorReceiveEvent-request: WebResourceRequest-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
