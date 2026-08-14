# OnHttpErrorReceiveEvent

Represents the callback invoked when an HTTP error occurs during web page resource loading.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface OnHttpErrorReceiveEvent--><!--Device-unnamed-export declare interface OnHttpErrorReceiveEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceWeb } from 'AtomicServiceWeb';
import { OnMessageEvent } from 'OnMessageEvent';
import { OnErrorReceiveEvent } from 'OnErrorReceiveEvent';
import { OnHttpErrorReceiveEvent } from 'OnHttpErrorReceiveEvent';
import { OnPageBeginEvent } from 'OnPageBeginEvent';
import { OnPageEndEvent } from 'OnPageEndEvent';
import { AtomicServiceWebController } from 'AtomicServiceWebController';
import { OnLoadInterceptEvent } from 'OnLoadInterceptEvent';
import { OnProgressChangeEvent } from 'OnProgressChangeEvent';
import { OnLoadInterceptCallback } from 'OnLoadInterceptCallback';
import { WebHeader } from 'WebHeader';
```

## request

```TypeScript
request: WebResourceRequest
```

Web resource request of event.

**Type:** WebResourceRequest

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnHttpErrorReceiveEvent-request: WebResourceRequest--><!--Device-OnHttpErrorReceiveEvent-request: WebResourceRequest-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## response

```TypeScript
response: WebResourceResponse
```

Web resource response of event.

**Type:** WebResourceResponse

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnHttpErrorReceiveEvent-response: WebResourceResponse--><!--Device-OnHttpErrorReceiveEvent-response: WebResourceResponse-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

