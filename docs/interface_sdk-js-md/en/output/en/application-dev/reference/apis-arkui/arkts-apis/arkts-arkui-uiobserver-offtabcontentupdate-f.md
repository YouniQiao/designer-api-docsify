# offTabContentUpdate

## offTabContentUpdate

```TypeScript
export function offTabContentUpdate(options: ObserverOptions, callback?: Callback<TabContentInfo>): void
```

Removes a callback function that was previously registered with \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offTabContentUpdate(options: ObserverOptions, callback?: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function offTabContentUpdate(options: ObserverOptions, callback?: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The options object. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;TabContentInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and Tabs ID will be removed. |


## offTabContentUpdate

```TypeScript
export function offTabContentUpdate(callback?: Callback<TabContentInfo>): void
```

Removes a callback function that was previously registered with \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offTabContentUpdate(callback?: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function offTabContentUpdate(callback?: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;TabContentInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

