# OnBufferingUpdateHandler

```TypeScript
type OnBufferingUpdateHandler = (infoType: BufferingInfoType, value: number) => void
```

Describes the callback invoked for the buffering update event.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-media-type OnBufferingUpdateHandler = (infoType: BufferingInfoType, value: int) => void--><!--Device-media-type OnBufferingUpdateHandler = (infoType: BufferingInfoType, value: int) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| infoType | [BufferingInfoType](arkts-media-media-bufferinginfotype-e.md) | Yes |
| value | number | Yes |
