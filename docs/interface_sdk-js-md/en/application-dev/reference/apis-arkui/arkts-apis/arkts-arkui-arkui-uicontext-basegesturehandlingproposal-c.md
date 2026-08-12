# BaseGestureHandlingProposal

Class BaseGestureHandlingProposal.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export abstract class BaseGestureHandlingProposal--><!--Device-unnamed-export abstract class BaseGestureHandlingProposal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CustomKeyboardContinueFeature, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from '@kit.ArkUI';
```

## action

```TypeScript
action: SmartGestureAction
```

The smart gesture action to be performed. Defines the specific operation triggered by the gesture.

**Type:** SmartGestureAction

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseGestureHandlingProposal-action: SmartGestureAction--><!--Device-BaseGestureHandlingProposal-action: SmartGestureAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operateIntention

```TypeScript
operateIntention: OperateIntention
```

The underlying user operation intention. Represents the fundamental user interaction goal.

**Type:** OperateIntention

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseGestureHandlingProposal-operateIntention: OperateIntention--><!--Device-BaseGestureHandlingProposal-operateIntention: OperateIntention-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

