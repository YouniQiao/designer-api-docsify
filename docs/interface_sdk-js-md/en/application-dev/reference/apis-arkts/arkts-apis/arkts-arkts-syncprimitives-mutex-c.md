# Mutex

A mutual exclusion lock that provides exclusive access to a shared resource

**Inheritance/Implementation:** Mutex implements [Lock](arkts-arkts-syncprimitives-lock-i.md#Lock)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class Mutex implements Lock--><!--Device-unnamed-export class Mutex implements Lock-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

Constructs a new Mutex instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Mutex-constructor()--><!--Device-Mutex-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## lock

```TypeScript
lock(): void
```

Acquires the lock

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Mutex-lock(): void--><!--Device-Mutex-lock(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## lockGuard

```TypeScript
lockGuard(callback: () => void): void
```

Executes the callback while holding the lock, automatically releasing it afterwards

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Mutex-lockGuard(callback: () => void): void--><!--Device-Mutex-lockGuard(callback: () => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | () =&gt; void | Yes | the callback to execute while holding the lock. |

## unlock

```TypeScript
unlock(): void
```

Releases the lock

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Mutex-unlock(): void--><!--Device-Mutex-unlock(): void-End-->

**System capability:** SystemCapability.Utils.Lang

