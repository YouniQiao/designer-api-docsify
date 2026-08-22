# onWillDraw

## Modules to Import

```TypeScript
```

## onWillDraw

```TypeScript
export function onWillDraw(context: UIContext, callback: Callback<void>): void
```

Registers a callback function to be called when the draw command will be drawn.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onWillDraw(context: UIContext, callback: Callback<void>): void--><!--Device-uiObserver-export function onWillDraw(context: UIContext, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-uicontext-uicontext-c.md) | Yes | The context scope of the observer. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | The callback function to be called when the draw command will be drawn. |

