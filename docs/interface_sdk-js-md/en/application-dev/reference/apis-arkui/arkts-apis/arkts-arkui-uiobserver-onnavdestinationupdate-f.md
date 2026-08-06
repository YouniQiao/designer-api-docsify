# onNavDestinationUpdate

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
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The options object. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;NavDestinationInfo&gt; | Yes | The callback function to be called when the navigation destination is updated. |


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
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;NavDestinationInfo&gt; | Yes | The callback function to be called when the navigation destination is updated. |

