# onUnhandledRejection

## Modules to Import

```TypeScript
import { errorManager } from '@kit.AbilityKit';
```

## onUnhandledRejection

```TypeScript
function onUnhandledRejection(observer: UnhandledRejectionObserver): void
```

Register unhandled rejection observer.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-errorManager-function onUnhandledRejection(observer: UnhandledRejectionObserver): void--><!--Device-errorManager-function onUnhandledRejection(observer: UnhandledRejectionObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [UnhandledRejectionObserver](arkts-ability-errormanager-unhandledrejectionobserver-t.md) | Yes | The unhandled rejection observer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

