# TargetedGestureProposal

类TargetedGestureProposal。

**继承/实现关系：** TargetedGestureProposal extends [BaseGestureHandlingProposal](arkts-arkui-arkui-uicontext-basegesturehandlingproposal-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export abstract class TargetedGestureProposal extends BaseGestureHandlingProposal--><!--Device-unnamed-export abstract class TargetedGestureProposal extends BaseGestureHandlingProposal-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## node

```TypeScript
node: FrameNode
```

手势处理的目标节点。该节点将接收并处理手势事件。

**类型：** [FrameNode](arkts-arkui-framenode-t.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TargetedGestureProposal-node: FrameNode--><!--Device-TargetedGestureProposal-node: FrameNode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

