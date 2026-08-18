# DragController

Provides APIs for initiating drag actions. When receiving a gesture event, such as a touch or long-press event, an application can initiate a drag action and carry drag information therein. > **NOTE：**> > In the following API examples, you must first use [getDragController()](arkts-arkui-arkui-uicontext-uicontext-c.md#getdragcontroller) in > **UIContext** to obtain a **DragController** instance, and then call the APIs using the obtained instance.

**Since:** 11

<!--Device-unnamed-export class DragController--><!--Device-unnamed-export class DragController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## interruptFollowHandMorphDropAnimation

```TypeScript
interruptFollowHandMorphDropAnimation(): boolean
```

Interrupt the pending follow-hand morph drop animation and trigger the finish sequence immediately.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragController-interruptFollowHandMorphDropAnimation(): boolean--><!--Device-DragController-interruptFollowHandMorphDropAnimation(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
