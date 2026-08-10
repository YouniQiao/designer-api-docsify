# offApplicationStateChange

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## offApplicationStateChange

```TypeScript
function offApplicationStateChange(observerId: int, callback: AsyncCallback<void>): void
```

注销应用状态监听器。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function offApplicationStateChange(observerId: int, callback: AsyncCallback<void>): void--><!--Device-appManager-function offApplicationStateChange(observerId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observerId | int | Yes | 注册的应用状态监听器ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The callback of off. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 201 | Permission denied. |


## offApplicationStateChange

```TypeScript
function offApplicationStateChange(observerId: int): Promise<void>
```

注销应用状态监听器。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function offApplicationStateChange(observerId: int): Promise<void>--><!--Device-appManager-function offApplicationStateChange(observerId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observerId | int | Yes | 注册的应用状态监听器ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 201 | Permission denied. |

