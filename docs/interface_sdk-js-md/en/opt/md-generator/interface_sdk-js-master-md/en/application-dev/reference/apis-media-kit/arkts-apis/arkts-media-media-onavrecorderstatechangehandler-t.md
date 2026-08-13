# OnAVRecorderStateChangeHandler

```TypeScript
type OnAVRecorderStateChangeHandler = (state: AVRecorderState, reason: StateChangeReason) => void
```

Describes the callback invoked for the AVRecorder state change event.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-media-type OnAVRecorderStateChangeHandler = (state: AVRecorderState, reason: StateChangeReason) => void--><!--Device-media-type OnAVRecorderStateChangeHandler = (state: AVRecorderState, reason: StateChangeReason) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| state | [AVRecorderState](arkts-media-media-avrecorderstate-t.md) | Yes |
| reason | [StateChangeReason](arkts-media-media-statechangereason-e.md) | Yes |
