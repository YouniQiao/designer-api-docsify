# onNavDestinationUpdate

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## onNavDestinationUpdate

```TypeScript
export function onNavDestinationUpdate(
    options: NavDestinationSwitchObserverOptions, 
    callback: Callback<NavDestinationInfo>
  ): void
```

Registers a callback function to be called when the navigation destination is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onNavDestinationUpdate(    options: NavDestinationSwitchObserverOptions,     callback: Callback<NavDestinationInfo>  ): void--><!--Device-uiObserver-export function onNavDestinationUpdate(    options: NavDestinationSwitchObserverOptions,     callback: Callback<NavDestinationInfo>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [NavDestinationSwitchObserverOptions](arkts-arkui-uiobserver-navdestinationswitchobserveroptions-i.md) | Yes | The options object. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;NavDestinationInfo&gt; | Yes | The callback function to be called when the navigation destination is updated. |


## onNavDestinationUpdate

```TypeScript
export function onNavDestinationUpdate(callback: Callback<NavDestinationInfo>): void
```

Registers a callback function to be called when the navigation destination is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onNavDestinationUpdate(callback: Callback<NavDestinationInfo>): void--><!--Device-uiObserver-export function onNavDestinationUpdate(callback: Callback<NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;NavDestinationInfo&gt; | Yes | The callback function to be called when the navigation destination is updated. |

