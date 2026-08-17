# PageInfo

Represents the page information of the router or navigation destination. If there is no related page information, **undefined** is returned.

**Since:** 12

<!--Device-unnamed-export interface PageInfo--><!--Device-unnamed-export interface PageInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceBar } from 'AtomicServiceBar';
import { ComponentUtils } from 'ComponentUtils';
import { ContextMenuController } from 'ContextMenuController';
import { CursorController } from 'CursorController';
import { DialogPresenter } from 'DialogPresenter';
import { DragController } from 'DragController';
import { Font } from 'Font';
import { KeyboardAvoidMode } from 'KeyboardAvoidMode';
import { MediaQuery } from 'MediaQuery';
import { OverlayManager } from 'OverlayManager';
import { PromptAction } from 'PromptAction';
import { Router } from 'Router';
import { UIContext } from 'UIContext';
import { UIInspector } from 'UIInspector';
import { UIObserver } from 'UIObserver';
import { PageInfo } from 'PageInfo';
import { SwiperDynamicSyncScene } from 'SwiperDynamicSyncScene';
import { SwiperDynamicSyncSceneType } from 'SwiperDynamicSyncSceneType';
import { MarqueeDynamicSyncScene } from 'MarqueeDynamicSyncScene';
import { MarqueeDynamicSyncSceneType } from 'MarqueeDynamicSyncSceneType';
import { MeasureUtils } from 'MeasureUtils';
import { FrameCallback } from 'FrameCallback';
import { OverlayManagerOptions } from 'OverlayManagerOptions';
import { TargetInfo } from 'TargetInfo';
import { TextMenuController } from 'TextMenuController';
import { NodeIdentity } from 'NodeIdentity';
import { NodeRenderState } from 'NodeRenderState';
import { NodeRenderStateChangeCallback } from 'NodeRenderStateChangeCallback';
import { Magnifier } from 'Magnifier';
import { ResolvedUIContext } from 'ResolvedUIContext';
import { TextSelectionClearPolicy } from 'TextSelectionClearPolicy';
import { CustomKeyboardContinueFeature } from 'CustomKeyboardContinueFeature';
import { BackgroundLuminanceSamplingConfigs } from 'BackgroundLuminanceSamplingConfigs';
import { LuminanceSampler } from 'LuminanceSampler';
```

## navDestinationInfo

```TypeScript
navDestinationInfo?: observer.NavDestinationInfo
```

the property of navDestination information.

**Type:** observer.NavDestinationInfo

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PageInfo-navDestinationInfo?: observer.NavDestinationInfo--><!--Device-PageInfo-navDestinationInfo?: observer.NavDestinationInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## routerPageInfo

```TypeScript
routerPageInfo?: observer.RouterPageInfo
```

Router information.

**Type:** observer.RouterPageInfo

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PageInfo-routerPageInfo?: observer.RouterPageInfo--><!--Device-PageInfo-routerPageInfo?: observer.RouterPageInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

