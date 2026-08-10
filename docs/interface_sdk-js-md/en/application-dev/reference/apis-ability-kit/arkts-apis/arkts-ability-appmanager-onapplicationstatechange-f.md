# onApplicationStateChange

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## onApplicationStateChange

```TypeScript
function onApplicationStateChange(observer: ApplicationStateObserver): int
```

注册所有应用程序的状态监听器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver): int--><!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver): int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [ApplicationStateObserver](arkts-ability-applicationstateobserver-c.md) | Yes | 应用状态监听器，用于监听应用的生命周期变化。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 已注册监听器ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 201 | Permission denied. |


## onApplicationStateChange

```TypeScript
function onApplicationStateChange(observer: ApplicationStateObserver, bundleNameList: Array<string>): int
```

注册指定应用程序的状态监听器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver, bundleNameList: Array<string>): int--><!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver, bundleNameList: Array<string>): int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [ApplicationStateObserver](arkts-ability-applicationstateobserver-c.md) | Yes | 应用状态监听器，用于监听应用的生命周期变化。 |
| bundleNameList | Array&lt;string&gt; | Yes | 表示需要注册监听的bundleName数组。最大值128。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 已注册监听器ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 201 | Permission denied. |

