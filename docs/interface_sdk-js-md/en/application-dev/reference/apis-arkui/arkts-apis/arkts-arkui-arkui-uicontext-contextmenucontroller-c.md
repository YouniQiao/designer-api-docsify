# ContextMenuController

提供控制菜单关闭的能力。  
> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> - 以下API需先使用UIContext中的[getContextMenuController()](arkts-arkui-arkui-uicontext-uicontext-c.md#getcontextmenucontroller)方
> 法获取ContextMenuController实例，再通过此实例调用对应方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ContextMenuController--><!--Device-unnamed-export declare class ContextMenuController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## close

```TypeScript
close(): void
```

关闭菜单。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuController-close(): void--><!--Device-ContextMenuController-close(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

