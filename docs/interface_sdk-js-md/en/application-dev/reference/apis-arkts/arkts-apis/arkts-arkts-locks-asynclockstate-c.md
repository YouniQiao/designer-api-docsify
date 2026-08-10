# AsyncLockState

用于存储异步锁实例上当前执行的所有锁操作的信息的类。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-locks-class AsyncLockState--><!--Device-locks-class AsyncLockState-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { ArkTSUtils } from 'kits/@kit.ArkTS';
```

## held

```TypeScript
held: AsyncLockInfo[]
```

持有的锁信息。

**Type:** [AsyncLockInfo](arkts-arkts-locks-asynclockinfo-c.md)[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLockState-held: AsyncLockInfo[]--><!--Device-AsyncLockState-held: AsyncLockInfo[]-End-->

**System capability:** SystemCapability.Utils.Lang

## pending

```TypeScript
pending: AsyncLockInfo[]
```

等待中的锁信息。

**Type:** [AsyncLockInfo](arkts-arkts-locks-asynclockinfo-c.md)[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyncLockState-pending: AsyncLockInfo[]--><!--Device-AsyncLockState-pending: AsyncLockInfo[]-End-->

**System capability:** SystemCapability.Utils.Lang

