# ComponentUtils

Provides API for obtaining the coordinates and size of the drawing area of a component. > **NOTE：**> > - The initial APIs of this class are supported since API version 10. > > - In the following API examples, you must first use [getComponentUtils()](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentutils) in > **UIContext** to obtain a **ComponentUtils** instance, and then call the APIs using the obtained instance.

**Since:** 10

<!--Device-unnamed-export class ComponentUtils--><!--Device-unnamed-export class ComponentUtils-End-->

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

## getRectangleById

```TypeScript
getRectangleById(id: string): componentUtils.ComponentInfo
```

Obtains the size, position, translation, scaling, rotation, and affine matrix information of the specified component. > **NOTE：**> > This API should be called after the target component's layout is complete to obtain its size information. It is > recommended that you use this API within onAppear.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ComponentUtils-getRectangleById(id: string): componentUtils.ComponentInfo--><!--Device-ComponentUtils-getRectangleById(id: string): componentUtils.ComponentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | Unique component ID. |

**Return value:**

| Type | Description |
| --- | --- |
| componentUtils.ComponentInfo | Size, position, translation, scaling, rotation, and affine matrix information of the component. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../errorcode-internal.md#100001-internal-error) | UI execution context not found. |

