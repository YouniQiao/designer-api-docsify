# GestureRecognizerJudgeBeginCallback

```TypeScript
declare type GestureRecognizerJudgeBeginCallback = (event: BaseGestureEvent, current: GestureRecognizer, recognizers: Array<GestureRecognizer>,
  touchRecognizers?: Array<TouchRecognizer>) => GestureJudgeResult
```

Represents a custom gesture recognizer judgment callback type.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [BaseGestureEvent](../arkts-apis/arkts-arkui-basegestureevent-i.md) | Yes |
| current | [GestureRecognizer](../arkts-apis/arkts-arkui-gesturerecognizer-c.md) | Yes |
| recognizers | Array&lt;[GestureRecognizer](../arkts-apis/arkts-arkui-gesturerecognizer-c.md)&gt; | Yes |
| touchRecognizers | Array&lt;[TouchRecognizer](../arkts-apis/arkts-arkui-touchrecognizer-c.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GestureJudgeResult](../arkts-apis/arkts-arkui-gesturejudgeresult-e.md) |
