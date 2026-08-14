# LuminanceSampler (System API)

Sets the background luminance color picking parameters, registers the luminance change listening callback, and unregisters the listening callback. > **NOTE：**> > In the following API examples, you must first use [getLuminanceSampler](arkts-arkui-arkui-uicontext-uicontext-c-sys.md#getLuminanceSampler) in > **UIContext** to obtain a **LuminanceSampler** object, and then call the APIs using the obtained object.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export class LuminanceSampler--><!--Device-unnamed-export class LuminanceSampler-End-->

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
```

## offBackgroundLuminanceChange

```TypeScript
offBackgroundLuminanceChange(samplingCallback?: Callback<number>): void
```

Unregisters the callback for listening to color picking. If no callback is specified, all listeners are canceled.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-LuminanceSampler-offBackgroundLuminanceChange(samplingCallback?: Callback<number>): void--><!--Device-LuminanceSampler-offBackgroundLuminanceChange(samplingCallback?: Callback<number>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| samplingCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No | Callback to unregister. |

## onBackgroundLuminanceChange

```TypeScript
onBackgroundLuminanceChange(samplingCallback: Callback<number>): void
```

Registers the callback for listening to color picking. The background luminance is divided into three ranges based on the luminance threshold and dark threshold set by the [setBackgroundLuminanceSamplingConfigs](#setBackgroundLuminanceSamplingConfigs) API: [0, Dark threshold], (Dark threshold, Luminance threshold], and (Luminance threshold, 255]. The callback is triggered when the background luminance range changes (or the listener callback is registered for the first time) and the interval between the current color picking and the last color picking reaches the specified interval, and the current background luminance is returned.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-LuminanceSampler-onBackgroundLuminanceChange(samplingCallback: Callback<number>): void--><!--Device-LuminanceSampler-onBackgroundLuminanceChange(samplingCallback: Callback<number>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| samplingCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes | Callback used to return the current background luminance.<br>Note: offBackgroundLuminanceChange cannot be called in the listening callback. |

## setBackgroundLuminanceSamplingConfigs

```TypeScript
setBackgroundLuminanceSamplingConfigs(configs: BackgroundLuminanceSamplingConfigs): void
```

Sets the color picking parameters. If the luminance threshold is not within the specified range or the dark threshold is greater than the luminance threshold, an exception is thrown.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-LuminanceSampler-setBackgroundLuminanceSamplingConfigs(configs: BackgroundLuminanceSamplingConfigs): void--><!--Device-LuminanceSampler-setBackgroundLuminanceSamplingConfigs(configs: BackgroundLuminanceSamplingConfigs): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| configs | [BackgroundLuminanceSamplingConfigs](arkts-arkui-arkui-uicontext-backgroundluminancesamplingconfigs-i-sys.md) | Yes | Color picking parameters. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../errorcode-internal.md#100001-internal-error) | Internal error. <br> 1. Incorrect parameter values. <br> 2. Incorrect parameters types. |

