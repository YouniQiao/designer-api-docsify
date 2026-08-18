# AtomicServiceBar

interface AtomicServiceBar

**Since:** 11

<!--Device-unnamed-export interface AtomicServiceBar--><!--Device-unnamed-export interface AtomicServiceBar-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from '@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from '@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from '@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from '@kit.ArkUI';
```

## getBarRect

```TypeScript
getBarRect(): Frame
```

Get size and position of the bar.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-AtomicServiceBar-getBarRect(): Frame--><!--Device-AtomicServiceBar-getBarRect(): Frame-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Frame](arkts-arkui-graphics-frame-i.md) | The size and position of bar in vp relative to window. |

## onBarRectChange

```TypeScript
onBarRectChange(callback: Callback<Frame>): void
```

When size and position of the bar changed, callback will be called.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AtomicServiceBar-onBarRectChange(callback: Callback<Frame>): void--><!--Device-AtomicServiceBar-onBarRectChange(callback: Callback<Frame>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[Frame](arkts-arkui-graphics-frame-i.md)&gt; | Yes | Callback that param contains the Frame. The parameters of the callback function cannot be undefined or null. |

## setBackgroundColor

```TypeScript
setBackgroundColor(color: Nullable< Color | number | string>): void
```

Set the background color of the bar.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceBar-setBackgroundColor(color: Nullable< Color | number | string>): void--><!--Device-AtomicServiceBar-setBackgroundColor(color: Nullable< Color | number | string>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Nullable&lt;Color \| number \| string&gt; | Yes | the color to set, undefined indicates using default. |

## setIconColor

```TypeScript
setIconColor(color: Nullable< Color | number | string>): void
```

Set the color of the icon on the bar.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceBar-setIconColor(color: Nullable< Color | number | string>): void--><!--Device-AtomicServiceBar-setIconColor(color: Nullable< Color | number | string>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Nullable&lt;Color \| number \| string&gt; | Yes | the color to set to icon, undefined indicates using default. |

## setTitleContent

```TypeScript
setTitleContent(content: string): void
```

Set the title of the bar.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceBar-setTitleContent(content: string): void--><!--Device-AtomicServiceBar-setTitleContent(content: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | string | Yes | the content of the bar. |

## setTitleFontStyle

```TypeScript
setTitleFontStyle(font: FontStyle): void
```

Set the font style of the bar's title.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceBar-setTitleFontStyle(font: FontStyle): void--><!--Device-AtomicServiceBar-setTitleFontStyle(font: FontStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| font | FontStyle | Yes | the font style of the bar's title. |

## setVisible

```TypeScript
setVisible(visible: boolean): void
```

Set the visibility of the bar, except the icon.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AtomicServiceBar-setVisible(visible: boolean): void--><!--Device-AtomicServiceBar-setVisible(visible: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| visible | boolean | Yes | whether this bar is visible. |

