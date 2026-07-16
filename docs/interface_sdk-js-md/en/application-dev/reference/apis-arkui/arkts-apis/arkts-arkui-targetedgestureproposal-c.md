# TargetedGestureProposal

Base class for smart gesture handling with a target node.

**Inheritance/Implementation:** TargetedGestureProposal extends [BaseGestureHandlingProposal](arkts-arkui-basegesturehandlingproposal-c.md)

**Since:** 26.0.0

<!--Device-unnamed-export abstract class TargetedGestureProposal extends BaseGestureHandlingProposal--><!--Device-unnamed-export abstract class TargetedGestureProposal extends BaseGestureHandlingProposal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from '@kit.ArkUI';
```

## node

```TypeScript
node: FrameNode
```

Target node that handles the current smart gesture.

**Type:** FrameNode

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TargetedGestureProposal-node: FrameNode--><!--Device-TargetedGestureProposal-node: FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

