# OnMessageEvent

Represents the callback invoked when the page is navigated back or destroyed.

**Since:** 12

<!--Device-unnamed-export declare interface OnMessageEvent--><!--Device-unnamed-export declare interface OnMessageEvent-End-->

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
data: object[]
```

The message data list.

**Type:** object[]

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnMessageEvent-data: object[]--><!--Device-OnMessageEvent-data: object[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

