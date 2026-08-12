# ResolvedUIContext

Defines the result of UIContext.resolveUIContext.This class is a subclass of UIContext and additionally provides the strategy used to obtain this UIContext.

**Inheritance/Implementation:** ResolvedUIContext extends [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ResolvedUIContext extends UIContext--><!--Device-unnamed-export declare class ResolvedUIContext extends UIContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CustomKeyboardContinueFeature, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from '@kit.ArkUI';
```

## strategy

```TypeScript
strategy: ResolveStrategy
```

Resolving strategy of the UIContext.

**Type:** [ResolveStrategy](arkts-arkui-arkui-uicontext-resolvestrategy-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResolvedUIContext-strategy: ResolveStrategy--><!--Device-ResolvedUIContext-strategy: ResolveStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

