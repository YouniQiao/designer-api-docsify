# offApplicationStateChange

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## offApplicationStateChange

```TypeScript
function offApplicationStateChange(observerId: int, callback: AsyncCallback<void>): void
```

Unregister application state observer.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function offApplicationStateChange(observerId: int, callback: AsyncCallback<void>): void--><!--Device-appManager-function offApplicationStateChange(observerId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observerId | int | Yes | Indicates the number code of the observer. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The callback of off. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |


## offApplicationStateChange

```TypeScript
function offApplicationStateChange(observerId: int): Promise<void>
```

Unregister application state observer.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function offApplicationStateChange(observerId: int): Promise<void>--><!--Device-appManager-function offApplicationStateChange(observerId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observerId | int | Yes | Indicates the number code of the observer. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

