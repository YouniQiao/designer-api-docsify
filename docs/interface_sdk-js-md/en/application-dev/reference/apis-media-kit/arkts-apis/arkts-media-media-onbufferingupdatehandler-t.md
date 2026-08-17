# OnBufferingUpdateHandler

```TypeScript
type OnBufferingUpdateHandler = (infoType: BufferingInfoType, value: int) => void
```

Describes the callback invoked for the buffering update event.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-media-type OnBufferingUpdateHandler = (infoType: BufferingInfoType, value: int) => void--><!--Device-media-type OnBufferingUpdateHandler = (infoType: BufferingInfoType, value: int) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| infoType | [BufferingInfoType](arkts-media-media-bufferinginfotype-e.md) | Yes | Buffering information type. |
| value | int | Yes | Value of the buffering information type. |

