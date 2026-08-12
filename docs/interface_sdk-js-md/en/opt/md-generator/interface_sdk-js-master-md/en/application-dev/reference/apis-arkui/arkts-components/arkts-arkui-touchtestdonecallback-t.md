# TouchTestDoneCallback

```TypeScript
declare type TouchTestDoneCallback = (event: BaseGestureEvent, recognizers: Array<GestureRecognizer>) => void
```

Represents the callback type for dynamically specifying gesture recognizer participation in gesture processing.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-unnamed-declare type TouchTestDoneCallback = (event: BaseGestureEvent, recognizers: Array<GestureRecognizer>) => void--><!--Device-unnamed-declare type TouchTestDoneCallback = (event: BaseGestureEvent, recognizers: Array<GestureRecognizer>) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [BaseGestureEvent](../arkts-apis/arkts-arkui-basegestureevent-i.md) | Yes |
| recognizers | Array&lt;[GestureRecognizer](../arkts-apis/arkts-arkui-gesturerecognizer-c.md)&gt; | Yes |
