# SmartGestureController

Class SmartGestureController.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export declare class SmartGestureController--><!--Device-unnamed-export declare class SmartGestureController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## clearMonitors

```TypeScript
clearMonitors(): void
```

Clear the callback functions to monitor gesture events.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SmartGestureController-clearMonitors(): void--><!--Device-SmartGestureController-clearMonitors(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## clearSelected

```TypeScript
clearSelected(): void
```

Clear the current smart gesture selection.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SmartGestureController-clearSelected(): void--><!--Device-SmartGestureController-clearSelected(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableSmartTapAndSlideGestures

```TypeScript
enableSmartTapAndSlideGestures(enabled: boolean): void
```

Enable or disable smart tap and slide gestures for watch. This switch controls the new implementation of tap and slide gestures. When enabled, the new smart gesture handling pipeline is used. When disabled, the legacy implementation is used for compatibility.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SmartGestureController-enableSmartTapAndSlideGestures(enabled: boolean): void--><!--Device-SmartGestureController-enableSmartTapAndSlideGestures(enabled: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether to enable smart tap and slide gesture handling. |

## registerMonitor

```TypeScript
registerMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void
```

Register a callback function to monitor gesture events. This method enables the application to receive the processing intention of the current gesture and carry out customized intervention before the system processes the gesture event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SmartGestureController-registerMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void--><!--Device-SmartGestureController-registerMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| monitorCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[BaseGestureHandlingProposal](../../apis-arkui/arkts-apis/arkts-arkui-arkuiuicontext-basegesturehandlingproposal-c.md), [GestureHandlingResolution](../../apis-arkui/arkts-apis/arkts-arkui-arkuiuicontext-gesturehandlingresolution-c.md)&gt; | Yes | Callback function invoked when a gesture is recognized. |

## requestSelected

```TypeScript
requestSelected(id: string): void
```

Request smart gesture selection of a frame node by its identifier.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SmartGestureController-requestSelected(id: string): void--><!--Device-SmartGestureController-requestSelected(id: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | The identifier of the frame node to select. |

## unregisterMonitor

```TypeScript
unregisterMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void
```

Unregister a callback function to monitor gesture events.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SmartGestureController-unregisterMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void--><!--Device-SmartGestureController-unregisterMonitor(monitorCallback: Callback<BaseGestureHandlingProposal, GestureHandlingResolution>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| monitorCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[BaseGestureHandlingProposal](../../apis-arkui/arkts-apis/arkts-arkui-arkuiuicontext-basegesturehandlingproposal-c.md), [GestureHandlingResolution](../../apis-arkui/arkts-apis/arkts-arkui-arkuiuicontext-gesturehandlingresolution-c.md)&gt; | Yes | Callback function invoked when a gesture is recognized. |

