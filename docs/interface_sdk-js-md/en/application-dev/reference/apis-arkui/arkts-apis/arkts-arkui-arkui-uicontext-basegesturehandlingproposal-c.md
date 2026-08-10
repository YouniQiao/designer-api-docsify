# BaseGestureHandlingProposal

类BaseGestureHandlingProposal。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export abstract class BaseGestureHandlingProposal--><!--Device-unnamed-export abstract class BaseGestureHandlingProposal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## action

```TypeScript
action: SmartGestureAction
```

要执行的智能手势操作。定义手势触发的具体操作。

**Type:** [SmartGestureAction](arkts-arkui-smartgestureaction-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseGestureHandlingProposal-action: SmartGestureAction--><!--Device-BaseGestureHandlingProposal-action: SmartGestureAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operateIntention

```TypeScript
operateIntention: OperateIntention
```

底层的用户操作意图。表示基本的用户交互目标。

**Type:** [OperateIntention](arkts-arkui-operateintention-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseGestureHandlingProposal-operateIntention: OperateIntention--><!--Device-BaseGestureHandlingProposal-operateIntention: OperateIntention-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

