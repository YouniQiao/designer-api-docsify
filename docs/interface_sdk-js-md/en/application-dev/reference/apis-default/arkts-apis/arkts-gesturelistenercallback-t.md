# GestureListenerCallback

```TypeScript
export declare type GestureListenerCallback = (info: GestureTriggerInfo) => void
```

Defines the callback type used in UIObserver to monitor specific gesture triggered information.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type GestureListenerCallback = (info: GestureTriggerInfo) => void--><!--Device-unnamed-export declare type GestureListenerCallback = (info: GestureTriggerInfo) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [GestureTriggerInfo](arkts-arkui-uicontext-gesturetriggerinfo-i.md) | Yes | the gesture details triggered with user interaction |

