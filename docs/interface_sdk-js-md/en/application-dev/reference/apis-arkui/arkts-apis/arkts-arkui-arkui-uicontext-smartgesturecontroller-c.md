# SmartGestureController

Provides the capability to enable smart gestures, monitor them, control the selection state, and dynamically determine smart gesture behavior. > **NOTE：**> > The following APIs must be called using a **SmartGestureController** instance obtained via > [getSmartGestureController()](arkts-arkui-arkui-uicontext-uicontext-c.md#getsmartgesturecontroller) in **UIContext**.

**Since:** 26.0.0

<!--Device-unnamed-export class SmartGestureController--><!--Device-unnamed-export class SmartGestureController-End-->

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

## clearMonitors

```TypeScript
clearMonitors(): void
```

Clears all monitoring callbacks registered for the current **UIContext**.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SmartGestureController-clearMonitors(): void--><!--Device-SmartGestureController-clearMonitors(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## clearSelected

```TypeScript
clearSelected(): void
```

Clears the currently selected node of smart gestures.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SmartGestureController-clearSelected(): void--><!--Device-SmartGestureController-clearSelected(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableSmartTapAndSlideGestures

```TypeScript
enableSmartTapAndSlideGestures(enabled: boolean): void
```

Sets whether to enable the tap and slide operations of smart gestures. > **NOTE：**> > - This API affects only the tap and slide smart gestures, not the wrist-turn gesture. > > - When disabled, the smartGestureShortcut > attribute on the component side is retained, but the tap and slide smart gestures will not be responded to.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SmartGestureController-enableSmartTapAndSlideGestures(enabled: boolean): void--><!--Device-SmartGestureController-enableSmartTapAndSlideGestures(enabled: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether to enable the tap and slide smart gesture handling. The value **true** means to enable it, and **false** means to disable it. |

## registerMonitor

```TypeScript
registerMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void
```

Registers a smart gesture monitoring callback. Before the system processes the current smart gesture, the application can receive the default action handling of the current gesture and apply custom intervention. The callback is used for asynchronous callbacks. > **NOTE：**> > - This API enables the application to receive the system's handling intent for the current smart gesture event > before it is processed by the system and apply custom intervention. > > - Users can customize the behavior of the current smart gesture through this callback. > > - Multiple monitoring callbacks can be registered. They are triggered in the reverse order of registration (the > last registered one is executed first). When a monitoring callback consumes the smart gesture event, that is, > when the return value [GestureHandlingResolution](arkts-arkui-arkui-uicontext-gesturehandlingresolution-c.md#gesturehandlingresolution).isConsumed is **true**, > subsequent monitoring callbacks will not be executed. > > - If the same callback is registered repeatedly, only the first registration takes effect; duplicate > registrations are ignored. > > - The return value of the callback must be a valid [GestureHandlingResolution](arkts-arkui-arkui-uicontext-gesturehandlingresolution-c.md#gesturehandlingresolution) > instance; otherwise, the modification will not take effect.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SmartGestureController-registerMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void--><!--Device-SmartGestureController-registerMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| monitorCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[BaseGestureHandlingProposal](arkts-arkui-arkui-uicontext-basegesturehandlingproposal-c.md), [GestureHandlingResolution](arkts-arkui-arkui-uicontext-gesturehandlingresolution-c.md)&gt; | Yes | Smart gesture monitoring callback. The callback parameter is the default action handling provided by the system, and the return value is used to declare whether to consume the current smart gesture and whether to replace the default action handling. |

## requestSelected

```TypeScript
requestSelected(id: string): void
```

Requests to set the specified component as the current smart gesture selected node. After successful selection, a selection prompt box is displayed. The style of the selection box varies by device. > **NOTE：**> > - The request takes effect only when all the following conditions are met: the target component can respond to > smart gestures, the component is visible on the screen, and the component has an > onClick event bound or a > TapGesture gesture bound. > > - Whether a component can respond to smart gestures is determined by **enabled** in > smartGestureShortcut.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SmartGestureController-requestSelected(id: string): void--><!--Device-SmartGestureController-requestSelected(id: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | Component id. |

## unregisterMonitor

```TypeScript
unregisterMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void
```

Unregisters a smart gesture monitoring callback.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SmartGestureController-unregisterMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void--><!--Device-SmartGestureController-unregisterMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| monitorCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[BaseGestureHandlingProposal](arkts-arkui-arkui-uicontext-basegesturehandlingproposal-c.md), [GestureHandlingResolution](arkts-arkui-arkui-uicontext-gesturehandlingresolution-c.md)&gt; | Yes | The smart gesture monitoring callback to unregister. |

