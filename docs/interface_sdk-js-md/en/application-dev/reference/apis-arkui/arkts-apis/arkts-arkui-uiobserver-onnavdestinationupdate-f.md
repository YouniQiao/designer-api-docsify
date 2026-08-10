# onNavDestinationUpdate

## Modules to Import

```TypeScript
import { uiObserver } from 'kits/@kit.ArkUI';
```

## onNavDestinationUpdate

```TypeScript
export function onNavDestinationUpdate(
    options: NavDestinationSwitchObserverOptions, 
    callback: Callback<NavDestinationInfo>
  ): void
```

监听NavDestination组件的状态变化。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onNavDestinationUpdate(    options: NavDestinationSwitchObserverOptions,     callback: Callback<NavDestinationInfo>  ): void--><!--Device-uiObserver-export function onNavDestinationUpdate(    options: NavDestinationSwitchObserverOptions,     callback: Callback<NavDestinationInfo>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [NavDestinationSwitchObserverOptions](arkts-arkui-uiobserver-navdestinationswitchobserveroptions-i.md) | Yes | 指定监听的Navigation的id。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NavDestinationInfo&gt; | Yes | 回调函数。返回当前的NavDestination组件状态。 |


## onNavDestinationUpdate

```TypeScript
export function onNavDestinationUpdate(callback: Callback<NavDestinationInfo>): void
```

监听NavDestination组件的状态变化。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onNavDestinationUpdate(callback: Callback<NavDestinationInfo>): void--><!--Device-uiObserver-export function onNavDestinationUpdate(callback: Callback<NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NavDestinationInfo&gt; | Yes | 回调函数。返回当前的NavDestination组件状态。 |

