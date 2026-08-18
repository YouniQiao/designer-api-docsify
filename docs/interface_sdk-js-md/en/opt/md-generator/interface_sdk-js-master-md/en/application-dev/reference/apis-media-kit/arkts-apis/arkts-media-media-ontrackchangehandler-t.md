# OnTrackChangeHandler

```TypeScript
type OnTrackChangeHandler = (index: number, isSelected: boolean) => void
```

Describes the callback invoked for the track change event.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-media-type OnTrackChangeHandler = (index: int, isSelected: boolean) => void--><!--Device-media-type OnTrackChangeHandler = (index: int, isSelected: boolean) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| isSelected | boolean | Yes |
