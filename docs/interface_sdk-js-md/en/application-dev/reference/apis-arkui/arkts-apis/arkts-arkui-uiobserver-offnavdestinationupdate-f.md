# offNavDestinationUpdate

## Modules to Import

```TypeScript
import { uiObserver } from 'kits/@kit.ArkUI';
```

## offNavDestinationUpdate

```TypeScript
export function offNavDestinationUpdate(
    options: NavDestinationSwitchObserverOptions, 
    callback?: Callback<NavDestinationInfo>
  ): void
```

取消监听NavDestination组件的状态变化。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offNavDestinationUpdate(    options: NavDestinationSwitchObserverOptions,     callback?: Callback<NavDestinationInfo>  ): void--><!--Device-uiObserver-export function offNavDestinationUpdate(    options: NavDestinationSwitchObserverOptions,     callback?: Callback<NavDestinationInfo>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [NavDestinationSwitchObserverOptions](arkts-arkui-uiobserver-navdestinationswitchobserveroptions-i.md) | Yes | 指定监听的Navigation的id。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NavDestinationInfo&gt; | No | 回调函数。返回当前的NavDestination组件状态。 |


## offNavDestinationUpdate

```TypeScript
export function offNavDestinationUpdate(callback?: Callback<NavDestinationInfo>): void
```

取消监听NavDestination组件的状态变化。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offNavDestinationUpdate(callback?: Callback<NavDestinationInfo>): void--><!--Device-uiObserver-export function offNavDestinationUpdate(callback?: Callback<NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NavDestinationInfo&gt; | No | 回调函数。返回当前的NavDestination组件状态。 |

