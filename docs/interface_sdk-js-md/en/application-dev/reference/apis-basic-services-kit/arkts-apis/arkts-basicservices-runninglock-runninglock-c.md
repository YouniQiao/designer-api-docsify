# RunningLock

Defines a **RunningLock** object.

**Since:** 7

**System capability:** SystemCapability.PowerManager.PowerManager.Core

## Modules to Import

```TypeScript
import { runningLock } from 'kits/@kit.BasicServicesKit';
```

## hold

```TypeScript
hold(timeout: number): void
```

Holds a running lock.

**Since:** 9

**Required permissions:** ohos.permission.RUNNING_LOCK

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeout | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## isHolding

```TypeScript
isHolding(): boolean
```

Checks whether this running lock is being held.

**Since:** 9

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isUsed

```TypeScript
isUsed(): boolean
```

Checks whether this running lock is used.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isHolding](#isholding)

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## lock

```TypeScript
lock(timeout: number): void
```

Locks and holds a **RunningLock** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [hold](#hold)

**Required permissions:** ohos.permission.RUNNING_LOCK

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeout | number | Yes |

## unhold

```TypeScript
unhold(): void
```

Releases this running lock.

**Since:** 9

**Required permissions:** ohos.permission.RUNNING_LOCK

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## unlock

```TypeScript
unlock(): void
```

Releases this running lock.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [unhold](#unhold)

**Required permissions:** ohos.permission.RUNNING_LOCK

**System capability:** SystemCapability.PowerManager.PowerManager.Core
