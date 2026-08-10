# OnProgressChangeEvent

定义网页加载进度变化时触发该回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export declare interface OnProgressChangeEvent--><!--Device-unnamed-export declare interface OnProgressChangeEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceWeb, OnMessageEvent, OnPageEndEvent, OnHttpErrorReceiveEvent, OnLoadInterceptEvent, WebHeader, OnProgressChangeEvent, OnErrorReceiveEvent, OnPageBeginEvent, OnLoadInterceptCallback, AtomicServiceWebController } from 'kits/@kit.ArkUI';
```

## newProgress

```TypeScript
newProgress: number
```

新的加载进度，取值范围为0到100的整数。单位：%。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnProgressChangeEvent-newProgress: number--><!--Device-OnProgressChangeEvent-newProgress: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

