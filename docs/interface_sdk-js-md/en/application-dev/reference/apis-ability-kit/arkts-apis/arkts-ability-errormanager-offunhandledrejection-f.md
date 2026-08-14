# offUnhandledRejection

## Modules to Import

```TypeScript
import { errorManager } from 'errorManager';
```

## offUnhandledRejection

```TypeScript
function offUnhandledRejection(observer?: UnhandledRejectionObserver): void
```

Unregister unhandled rejection observer.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

<!--Device-errorManager-function offUnhandledRejection(observer?: UnhandledRejectionObserver): void--><!--Device-errorManager-function offUnhandledRejection(observer?: UnhandledRejectionObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [UnhandledRejectionObserver](arkts-ability-errormanager-unhandledrejectionobserver-t.md) | No | the registered observer |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16300004](../errorcode-ability.md#16300004-observer-does-not-exist) | If the observer does not exist |

