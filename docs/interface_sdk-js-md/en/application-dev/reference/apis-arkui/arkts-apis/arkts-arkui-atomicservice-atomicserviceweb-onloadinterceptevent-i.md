# OnLoadInterceptEvent

Represents the event triggered when resource loading is intercepted.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface OnLoadInterceptEvent--><!--Device-unnamed-export declare interface OnLoadInterceptEvent-End-->

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

## data

```TypeScript
data: WebResourceRequest
```

Web resource request of event.

**Type:** WebResourceRequest

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnLoadInterceptEvent-data: WebResourceRequest--><!--Device-OnLoadInterceptEvent-data: WebResourceRequest-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

