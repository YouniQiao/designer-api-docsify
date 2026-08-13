# LuminanceSampler (System API)

Sets the background luminance color picking parameters, registers the luminance change listening callback, and unregisters the listening callback. > **NOTE：**> > In the following API examples, you must first use [getLuminanceSampler](arkts-arkui-arkui-uicontext-uicontext-c-sys.md#getLuminanceSampler) in > **UIContext** to obtain a **LuminanceSampler** object, and then call the APIs using the obtained object.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-export class LuminanceSampler--><!--Device-unnamed-export class LuminanceSampler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CustomKeyboardContinueFeature, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from '@kit.ArkUI';
```

## offBackgroundLuminanceChange

```TypeScript
offBackgroundLuminanceChange(samplingCallback?: Callback<number>): void
```

Unregisters the callback for listening to color picking. If no callback is specified, all listeners are canceled.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-LuminanceSampler-offBackgroundLuminanceChange(samplingCallback?: Callback<number>): void--><!--Device-LuminanceSampler-offBackgroundLuminanceChange(samplingCallback?: Callback<number>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| samplingCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

## onBackgroundLuminanceChange

```TypeScript
onBackgroundLuminanceChange(samplingCallback: Callback<number>): void
```

Registers the callback for listening to color picking. The background luminance is divided into three ranges based on the luminance threshold and dark threshold set by the [setBackgroundLuminanceSamplingConfigs](#setBackgroundLuminanceSamplingConfigs) API: [0, Dark threshold], (Dark threshold, Luminance threshold], and (Luminance threshold, 255]. The callback is triggered when the background luminance range changes (or the listener callback is registered for the first time) and the interval between the current color picking and the last color picking reaches the specified interval, and the current background luminance is returned.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-LuminanceSampler-onBackgroundLuminanceChange(samplingCallback: Callback<number>): void--><!--Device-LuminanceSampler-onBackgroundLuminanceChange(samplingCallback: Callback<number>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| samplingCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## setBackgroundLuminanceSamplingConfigs

```TypeScript
setBackgroundLuminanceSamplingConfigs(configs: BackgroundLuminanceSamplingConfigs): void
```

Sets the color picking parameters. If the luminance threshold is not within the specified range or the dark threshold is greater than the luminance threshold, an exception is thrown.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-LuminanceSampler-setBackgroundLuminanceSamplingConfigs(configs: BackgroundLuminanceSamplingConfigs): void--><!--Device-LuminanceSampler-setBackgroundLuminanceSamplingConfigs(configs: BackgroundLuminanceSamplingConfigs): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| configs | [BackgroundLuminanceSamplingConfigs](arkts-arkui-arkui-uicontext-backgroundluminancesamplingconfigs-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
