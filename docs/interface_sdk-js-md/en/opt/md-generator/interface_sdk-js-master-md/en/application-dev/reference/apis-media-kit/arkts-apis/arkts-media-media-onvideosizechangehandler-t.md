# OnVideoSizeChangeHandler

```TypeScript
type OnVideoSizeChangeHandler = (width: number, height: number) => void
```

Describes the callback invoked for the video size change event.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-media-type OnVideoSizeChangeHandler = (width: int, height: int) => void--><!--Device-media-type OnVideoSizeChangeHandler = (width: int, height: int) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |
