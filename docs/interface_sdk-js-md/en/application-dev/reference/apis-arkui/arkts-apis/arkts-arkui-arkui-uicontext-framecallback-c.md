# FrameCallback

Implements the API for setting the task that needs to be executed during the next frame rendering. > **NOTE：**> > - The following APIs must be used in conjunction with [postFrameCallback](arkts-arkui-arkui-uicontext-uicontext-c.md#postframecallback) and > [postDelayedFrameCallback](arkts-arkui-arkui-uicontext-uicontext-c.md#postdelayedframecallback) from [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#uicontext). > Extend this class and override either the [onFrame](#onframe) or > [onIdle](#onidle) method to implement specific service logic.

**Since:** 12

<!--Device-unnamed-export abstract class FrameCallback--><!--Device-unnamed-export abstract class FrameCallback-End-->

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

## onFrame

```TypeScript
onFrame(frameTimeInNano: number): void
```

Called when the next frame is rendered.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameCallback-onFrame(frameTimeInNano: number): void--><!--Device-FrameCallback-onFrame(frameTimeInNano: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| frameTimeInNano | number | Yes | Time when the rendering of the next frame starts, in nanoseconds.<br>Value range: [0, +∞) |

## onIdle

```TypeScript
onIdle(timeLeftInNano: number): void
```

Called after the rendering of the subsequent frame has finished and there is more than 1 millisecond left before the next VSync signal. If the time left is not more than 1 millisecond, the execution of this API will be deferred to a later frame.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FrameCallback-onIdle(timeLeftInNano: number): void--><!--Device-FrameCallback-onIdle(timeLeftInNano: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeLeftInNano | number | Yes | Remaining idle time for the current frame, in nanoseconds.<br>Value range: [0, +∞) |

