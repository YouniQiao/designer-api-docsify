# OnAVRecorderStateChangeHandler

```TypeScript
type OnAVRecorderStateChangeHandler = (state: AVRecorderState, reason: StateChangeReason) => void
```

录制状态机切换事件回调方法。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-type OnAVRecorderStateChangeHandler = (state: AVRecorderState, reason: StateChangeReason) => void--><!--Device-unnamed-type OnAVRecorderStateChangeHandler = (state: AVRecorderState, reason: StateChangeReason) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [AVRecorderState](arkts-media-avrecorderstate-t.md) | Yes | 当前录制状态。 |
| reason | [StateChangeReason](arkts-media-media-statechangereason-e.md) | Yes | 当前录制状态的切换原因。 |

