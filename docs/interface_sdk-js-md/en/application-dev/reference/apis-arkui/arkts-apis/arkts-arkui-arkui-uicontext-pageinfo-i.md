# PageInfo

Router和NavDestination等页面信息，若无对应的Router或NavDestination页面信息，则对应属性为undefined。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface PageInfo--><!--Device-unnamed-export interface PageInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## navDestinationInfo

```TypeScript
navDestinationInfo?: observer.NavDestinationInfo
```

NavDestination信息。

**Type:** observer.NavDestinationInfo

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageInfo-navDestinationInfo?: observer.NavDestinationInfo--><!--Device-PageInfo-navDestinationInfo?: observer.NavDestinationInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## routerPageInfo

```TypeScript
routerPageInfo?: observer.RouterPageInfo
```

Router信息。

**Type:** observer.RouterPageInfo

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageInfo-routerPageInfo?: observer.RouterPageInfo--><!--Device-PageInfo-routerPageInfo?: observer.RouterPageInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

