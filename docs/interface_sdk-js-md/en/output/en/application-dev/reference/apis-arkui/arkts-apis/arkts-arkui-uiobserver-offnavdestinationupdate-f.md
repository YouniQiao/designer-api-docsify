# offNavDestinationUpdate

## offNavDestinationUpdate

```TypeScript
export function offNavDestinationUpdate(
    options: NavDestinationSwitchObserverOptions, 
    callback?: Callback<NavDestinationInfo>
  ): void
```

Removes a callback function that was previously registered with \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offNavDestinationUpdate(    options: NavDestinationSwitchObserverOptions,     callback?: Callback<NavDestinationInfo>  ): void--><!--Device-uiObserver-export function offNavDestinationUpdate(    options: NavDestinationSwitchObserverOptions,     callback?: Callback<NavDestinationInfo>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The options object. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;NavDestinationInfo&gt; | No | The callback function to remove. If not provided,all callbacks for the given event type and navigation ID will be removed. |


## offNavDestinationUpdate

```TypeScript
export function offNavDestinationUpdate(callback?: Callback<NavDestinationInfo>): void
```

Removes a callback function that was previously registered with \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offNavDestinationUpdate(callback?: Callback<NavDestinationInfo>): void--><!--Device-uiObserver-export function offNavDestinationUpdate(callback?: Callback<NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;NavDestinationInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

