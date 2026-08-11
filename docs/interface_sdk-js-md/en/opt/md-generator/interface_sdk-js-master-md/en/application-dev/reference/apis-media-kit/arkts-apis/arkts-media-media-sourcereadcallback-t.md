# SourceReadCallback

```TypeScript
type SourceReadCallback = (uuid: number, requestedOffset: number, requestedLength: number) => void
```

This callback function is implemented by applications to handle resource read requests. When data is available, applications should push it to the player using the   
[respondData](arkts-media-media-mediasourceloadingrequest-i.md#responddata)API of the corresponding MediaSourceLoadingRequest object.

> **NOTE：**
> 
> The client must return the handle immediately after processing the request.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-media-type SourceReadCallback = (uuid: long, requestedOffset: long, requestedLength: long) => void--><!--Device-media-type SourceReadCallback = (uuid: long, requestedOffset: long, requestedLength: long) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uuid | number | Yes |
| requestedOffset | number | Yes |
| requestedLength | number | Yes |
