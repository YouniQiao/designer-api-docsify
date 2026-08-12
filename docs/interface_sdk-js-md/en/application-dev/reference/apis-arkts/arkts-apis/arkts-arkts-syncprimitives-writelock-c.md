# WriteLock

A write lock that provides exclusive write access to a shared resource

**Inheritance/Implementation:** WriteLock implements [Lock](arkts-arkts-syncprimitives-lock-i.md#Lock)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class WriteLock implements Lock--><!--Device-unnamed-export class WriteLock implements Lock-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(lock: RWLock)
```

Constructs a new WriteLock associated with the given RWLock

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WriteLock-constructor(lock: RWLock)--><!--Device-WriteLock-constructor(lock: RWLock)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lock | [RWLock](arkts-arkts-syncprimitives-rwlock-c.md) | Yes | the RWLock this WriteLock is associated with. |

## lock

```TypeScript
lock(): void
```

Acquires the write lock

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WriteLock-lock(): void--><!--Device-WriteLock-lock(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## unlock

```TypeScript
unlock(): void
```

Releases the write lock

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WriteLock-unlock(): void--><!--Device-WriteLock-unlock(): void-End-->

**System capability:** SystemCapability.Utils.Lang

