# offDensityUpdate

## offDensityUpdate

```TypeScript
export function offDensityUpdate(context: UIContext, callback?: Callback<DensityInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offDensityUpdate(context: UIContext, callback?: Callback<DensityInfo>): void--><!--Device-uiObserver-export function offDensityUpdate(context: UIContext, callback?: Callback<DensityInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | The context scope of the observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DensityInfo](../../apis-arkui/arkts-apis/arkts-arkui-uiobserver-densityinfo-c.md)&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

