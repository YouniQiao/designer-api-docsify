# offNavDestinationUpdate

## Modules to Import

```TypeScript
```

## offNavDestinationUpdate

```TypeScript
export function offNavDestinationUpdate(
    options: NavDestinationSwitchObserverOptions, 
    callback?: Callback<NavDestinationInfo>
  ): void
```

Removes a callback function that was previously registered with `onNavDestinationUpdate`.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offNavDestinationUpdate(    options: NavDestinationSwitchObserverOptions,     callback?: Callback<NavDestinationInfo>  ): void--><!--Device-uiObserver-export function offNavDestinationUpdate(    options: NavDestinationSwitchObserverOptions,     callback?: Callback<NavDestinationInfo>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [NavDestinationSwitchObserverOptions](arkts-uiobserver-navdestinationswitchobserveroptions-i.md) | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NavDestinationInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and navigation ID will be removed. |


## offNavDestinationUpdate

```TypeScript
export function offNavDestinationUpdate(callback?: Callback<NavDestinationInfo>): void
```

Removes a callback function that was previously registered with `onNavDestinationUpdate`.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offNavDestinationUpdate(callback?: Callback<NavDestinationInfo>): void--><!--Device-uiObserver-export function offNavDestinationUpdate(callback?: Callback<NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NavDestinationInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

