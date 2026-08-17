# ReadLock

A read lock that allows concurrent read access to a shared resource

**Inheritance/Implementation:** ReadLock implements [Lock](arkts-na-syncprimitives-lock-i.md#lock)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class ReadLock--><!--Device-unnamed-export class ReadLock-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(lock: RWLock)
```

Constructs a new ReadLock associated with the given RWLock

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadLock-constructor(lock: RWLock)--><!--Device-ReadLock-constructor(lock: RWLock)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lock | [RWLock](arkts-na-syncprimitives-rwlock-c.md) | Yes | the RWLock this ReadLock is associated with. |

## lock

```TypeScript
lock(): void
```

Acquires the read lock

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadLock-lock(): void--><!--Device-ReadLock-lock(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## unlock

```TypeScript
unlock(): void
```

Releases the read lock

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadLock-unlock(): void--><!--Device-ReadLock-unlock(): void-End-->

**System capability:** SystemCapability.Utils.Lang

