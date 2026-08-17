# DragController

class DragController

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class DragController--><!--Device-unnamed-export declare class DragController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## interruptFollowHandMorphDropAnimation

```TypeScript
interruptFollowHandMorphDropAnimation(): boolean
```

Interrupt the pending follow-hand morph drop animation and trigger the finish sequence immediately.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragController-interruptFollowHandMorphDropAnimation(): boolean--><!--Device-DragController-interruptFollowHandMorphDropAnimation(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if interrupted successfully; false if there is no pending follow-hand morph drop animation to interrupt. |

