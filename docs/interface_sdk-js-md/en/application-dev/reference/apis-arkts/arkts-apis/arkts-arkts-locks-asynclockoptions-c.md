# AsyncLockOptions

Lock operation's options

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-locks-class AsyncLockOptions--><!--Device-locks-class AsyncLockOptions-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { ArkTSUtils } from '@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

Default constructor.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLockOptions-constructor()--><!--Device-AsyncLockOptions-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## isAvailable

```TypeScript
isAvailable: boolean
```

If the value is true and lockAsync cannot acquire the lock immediately, the operation is canceled.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLockOptions-isAvailable: boolean--><!--Device-AsyncLockOptions-isAvailable: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## signal

```TypeScript
signal: AbortSignal<T> | null
```

The object used to abort the async operation. If signal.aborted is true, the callback will not be called.

**Type:** [AbortSignal](arkts-arkts-locks-abortsignal-c.md)&lt;T&gt; \| null

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLockOptions-signal: AbortSignal<T> | null--><!--Device-AsyncLockOptions-signal: AbortSignal<T> | null-End-->

**System capability:** SystemCapability.Utils.Lang

## timeout

```TypeScript
timeout: number
```

Lock operation timeout in milliseconds. If it is greater than zero, lockAsync will reject the resulting promise when the timeout is exceeded.

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLockOptions-timeout: number--><!--Device-AsyncLockOptions-timeout: number-End-->

**System capability:** SystemCapability.Utils.Lang

