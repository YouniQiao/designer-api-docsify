# WebHeader

Describes the request/response header returned by the **AtomicServiceWeb** component.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface WebHeader--><!--Device-unnamed-export declare interface WebHeader-End-->

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

## headerKey

```TypeScript
headerKey: string
```

Key of the request/response header.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebHeader-headerKey: string--><!--Device-WebHeader-headerKey: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## headerValue

```TypeScript
headerValue: string
```

Value of the request/response header.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebHeader-headerValue: string--><!--Device-WebHeader-headerValue: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

