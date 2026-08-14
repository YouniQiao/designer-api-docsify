# OnProgressChangeEvent

Represents the callback invoked when the web page loading progress changes.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface OnProgressChangeEvent--><!--Device-unnamed-export declare interface OnProgressChangeEvent-End-->

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

## newProgress

```TypeScript
newProgress: number
```

The new progress of the page.

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnProgressChangeEvent-newProgress: number--><!--Device-OnProgressChangeEvent-newProgress: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

