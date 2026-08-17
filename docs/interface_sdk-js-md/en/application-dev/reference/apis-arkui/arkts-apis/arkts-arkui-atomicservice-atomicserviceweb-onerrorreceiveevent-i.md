# OnErrorReceiveEvent

Represents the callback invoked when an error occurs during web page loading.

**Since:** 12

<!--Device-unnamed-export declare interface OnErrorReceiveEvent--><!--Device-unnamed-export declare interface OnErrorReceiveEvent-End-->

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

## error

```TypeScript
error: WebResourceError
```

Web resource error of event.

**Type:** WebResourceError

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnErrorReceiveEvent-error: WebResourceError--><!--Device-OnErrorReceiveEvent-error: WebResourceError-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## request

```TypeScript
request: WebResourceRequest
```

Web resource request of event.

**Type:** WebResourceRequest

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnErrorReceiveEvent-request: WebResourceRequest--><!--Device-OnErrorReceiveEvent-request: WebResourceRequest-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

