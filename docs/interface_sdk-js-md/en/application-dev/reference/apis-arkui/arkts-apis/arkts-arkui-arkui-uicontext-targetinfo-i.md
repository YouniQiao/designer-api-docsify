# TargetInfo

Specifies the target node for component binding.

**Since:** 18

<!--Device-unnamed-export interface TargetInfo--><!--Device-unnamed-export interface TargetInfo-End-->

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

## componentId

```TypeScript
componentId?: number
```

Unique ID of the custom component where the target node is located. When the above **id** is specified as a string, this property can be used to narrow down the scope, helping you ensure the uniqueness of **id: string** within a certain range.

**Type:** number

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TargetInfo-componentId?: number--><!--Device-TargetInfo-componentId?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id: string | number
```

Target node for binding popups or menus.<br>**NOTE：**<br>1. When **id** is a number, it corresponds to the component's **UniqueID**, whose uniqueness is guaranteed by the system.<br>2. When **id** is a string, it corresponds to the component specified by the universal attribute id. You must ensure the uniqueness of this ID, although there may be multiple instances.

**Type:** string \| number

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TargetInfo-id: string | number--><!--Device-TargetInfo-id: string | number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

