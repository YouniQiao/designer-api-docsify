# onDensityUpdate

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

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
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | The context scope of the observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DensityInfo](arkts-arkui-uiobserver-densityinfo-c.md)&gt; | Yes | The callback function to be called when the screen density is updated. |

