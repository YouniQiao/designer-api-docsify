# GestureRecognizerJudgeBeginCallback

```TypeScript
export type GestureRecognizerJudgeBeginCallback = (event: BaseGestureEvent, current: GestureRecognizer, recognizers: Array<GestureRecognizer>, touchRecognizers?: Array<TouchRecognizer>) => GestureJudgeResult
```

Defines the callback type used in onGestureRecognizerJudgeBegin.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type GestureRecognizerJudgeBeginCallback = (event: BaseGestureEvent, current: GestureRecognizer, recognizers: Array<GestureRecognizer>, touchRecognizers?: Array<TouchRecognizer>) => GestureJudgeResult--><!--Device-unnamed-export type GestureRecognizerJudgeBeginCallback = (event: BaseGestureEvent, current: GestureRecognizer, recognizers: Array<GestureRecognizer>, touchRecognizers?: Array<TouchRecognizer>) => GestureJudgeResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [BaseGestureEvent](../../apis-arkui/arkts-apis/arkts-arkui-basegestureevent-i.md) | Yes | the event information |
| current | [GestureRecognizer](../../apis-arkui/arkts-apis/arkts-arkui-gesturerecognizer-c.md) | Yes | the current gesture recognizer of the component |
| recognizers | Array&lt;[GestureRecognizer](../../apis-arkui/arkts-apis/arkts-arkui-gesturerecognizer-c.md)&gt; | Yes | the gesture recognizers of the component on the response chain |
| touchRecognizers | Array&lt;[TouchRecognizer](../../apis-arkui/arkts-apis/arkts-arkui-touchrecognizer-c.md)&gt; | No | the touch recognizers of the component on the response chain |

**Return value:**

| Type | Description |
| --- | --- |
| [GestureJudgeResult](../../apis-arkui/arkts-apis/arkts-arkui-gesturejudgeresult-e.md) | the gesture judge result |

