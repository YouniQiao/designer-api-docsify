# AbortSignal

用于终止异步操作的对象。该类的实例必须在其创建的同一线程中访问。从其他线程访问此类的字段会导致未定义的行为。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-locks-class AbortSignal<T>--><!--Device-locks-class AbortSignal<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { ArkTSUtils } from 'kits/@kit.ArkTS';
```

## aborted

```TypeScript
aborted: boolean
```

是否终止异步操作。为true时表示终止异步操作，为false时表示异步操作未被终止。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbortSignal-aborted: boolean--><!--Device-AbortSignal-aborted: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## reason

```TypeScript
reason: T
```

终止的原因。此值将用于拒绝lockAsync返回的Promise。

**Type:** T

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbortSignal-reason: T--><!--Device-AbortSignal-reason: T-End-->

**System capability:** SystemCapability.Utils.Lang

