# BackgroundLuminanceSamplingConfigs (System API)

Sets the background luminance sampling parameters.

**Since:** 23

<!--Device-unnamed-export interface BackgroundLuminanceSamplingConfigs--><!--Device-unnamed-export interface BackgroundLuminanceSamplingConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

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

## brightThreshold

```TypeScript
brightThreshold?: number
```

Light color brightness threshold. The value must be an integer in the range of [0, 255]. The dark color brightness threshold must be less than the light color brightness threshold.

**Type:** number

**Default:** 220

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundLuminanceSamplingConfigs-brightThreshold?: number--><!--Device-BackgroundLuminanceSamplingConfigs-brightThreshold?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## darkThreshold

```TypeScript
darkThreshold?: number
```

Dark color brightness threshold. The value must be an integer in the range of [0, 255]. The dark color brightness threshold must be less than the light color brightness threshold.

**Type:** number

**Default:** 150

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundLuminanceSamplingConfigs-darkThreshold?: number--><!--Device-BackgroundLuminanceSamplingConfigs-darkThreshold?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## region

```TypeScript
region?: Edges<LengthMetrics>
```

Sample area offset relative to the component, calculated from the component's upper left corner as the reference point. The component's own area is used by default.

**Type:** Edges&lt;LengthMetrics&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundLuminanceSamplingConfigs-region?: Edges<LengthMetrics>--><!--Device-BackgroundLuminanceSamplingConfigs-region?: Edges<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## samplingInterval

```TypeScript
samplingInterval?: number
```

Color sampling interval, in milliseconds. The minimum value is 180 ms.

**Type:** number

**Default:** 500

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundLuminanceSamplingConfigs-samplingInterval?: number--><!--Device-BackgroundLuminanceSamplingConfigs-samplingInterval?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

