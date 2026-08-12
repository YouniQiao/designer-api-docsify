# FrameCallback

Class FrameCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare abstract class FrameCallback--><!--Device-unnamed-export declare abstract class FrameCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CustomKeyboardContinueFeature, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from '@kit.ArkUI';
```

## onFrame

```TypeScript
onFrame(frameTimeInNano: long): void
```

Call when a new display frame is being rendered.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameCallback-onFrame(frameTimeInNano: long): void--><!--Device-FrameCallback-onFrame(frameTimeInNano: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| frameTimeInNano | long | Yes | The frame time in nanoseconds. |

## onIdle

```TypeScript
onIdle(timeLeftInNano: long): void
```

Called at the end of the next idle frame. If there is no next frame, will request one automatically.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameCallback-onIdle(timeLeftInNano: long): void--><!--Device-FrameCallback-onIdle(timeLeftInNano: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeLeftInNano | long | Yes | The remaining time from the deadline for this frame. |

