# onApplicationStateChange

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## onApplicationStateChange

```TypeScript
function onApplicationStateChange(observer: ApplicationStateObserver): int
```

Register application state observer.

**Since:** 23

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver): int--><!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver): int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | ApplicationStateObserver | Yes | The application state observer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the number code of the observer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |


## onApplicationStateChange

```TypeScript
function onApplicationStateChange(observer: ApplicationStateObserver, bundleNameList: Array<string>): int
```

Register application state observer.

**Since:** 23

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver, bundleNameList: Array<string>): int--><!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver, bundleNameList: Array<string>): int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | ApplicationStateObserver | Yes | The application state observer. |
| bundleNameList | Array&lt;string&gt; | Yes | The list of bundleName. The max length is 128. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the number code of the observer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

