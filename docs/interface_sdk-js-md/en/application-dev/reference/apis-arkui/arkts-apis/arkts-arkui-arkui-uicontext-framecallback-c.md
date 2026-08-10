# FrameCallback

Class FrameCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare abstract class FrameCallback--><!--Device-unnamed-export declare abstract class FrameCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
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

在下一帧空闲时回调。如果没有下一帧，会自动请求一帧。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameCallback-onIdle(timeLeftInNano: long): void--><!--Device-FrameCallback-onIdle(timeLeftInNano: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeLeftInNano | long | Yes | The remaining time from the deadline for this frame. |

