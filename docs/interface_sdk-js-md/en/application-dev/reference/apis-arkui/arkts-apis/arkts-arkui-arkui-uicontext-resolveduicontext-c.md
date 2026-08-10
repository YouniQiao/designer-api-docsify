# ResolvedUIContext

UIContext.resolveUIContext接口的返回值类型，属于UIContext类型的子类，额外包含获取该UIContext的解析策略。

**Inheritance/Implementation:** ResolvedUIContext extends [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ResolvedUIContext extends UIContext--><!--Device-unnamed-export declare class ResolvedUIContext extends UIContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## strategy

```TypeScript
strategy: ResolveStrategy
```

UIContext的解析策略

**Type:** [ResolveStrategy](arkts-arkui-arkui-uicontext-resolvestrategy-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResolvedUIContext-strategy: ResolveStrategy--><!--Device-ResolvedUIContext-strategy: ResolveStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

