# TouchTestDoneCallback

```TypeScript
export type TouchTestDoneCallback = (event: BaseGestureEvent, recognizers: Array<GestureRecognizer>) => void
```

Defines the callback type used in onTouchTestDone. When the user touch down, the system performs hit test process to collect all gesture recognizers based on the press location, when the collection is completed, and before gesture begin to be recognizing, the callback is triggered, you can get all recognizer's information from this callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type TouchTestDoneCallback = (event: BaseGestureEvent, recognizers: Array<GestureRecognizer>) => void--><!--Device-unnamed-export type TouchTestDoneCallback = (event: BaseGestureEvent, recognizers: Array<GestureRecognizer>) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [BaseGestureEvent](../../apis-arkui/arkts-apis/arkts-arkui-basegestureevent-i.md) | Yes | the event information, basicly is the touch down information |
| recognizers | Array&lt;[GestureRecognizer](../../apis-arkui/arkts-apis/arkts-arkui-gesturerecognizer-c.md)&gt; | Yes | the gesture recognizers of the component on the response chain |

