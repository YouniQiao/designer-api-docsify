# onDensityUpdate

## onDensityUpdate

```TypeScript
export function onDensityUpdate(context: UIContext, callback: Callback<DensityInfo>): void
```

Registers a callback function to be called when the screen density is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onDensityUpdate(context: UIContext, callback: Callback<DensityInfo>): void--><!--Device-uiObserver-export function onDensityUpdate(context: UIContext, callback: Callback<DensityInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The context scope of the observer. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;DensityInfo&gt; | Yes | The callback function to be called when the screen density is updated. |

