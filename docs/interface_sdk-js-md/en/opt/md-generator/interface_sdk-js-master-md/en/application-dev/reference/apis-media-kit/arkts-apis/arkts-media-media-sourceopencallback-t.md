# SourceOpenCallback

```TypeScript
type SourceOpenCallback = (request: MediaSourceLoadingRequest) => number
```

This callback function is implemented by applications to handle resource open requests and return a unique handle for the opened resource. > **NOTE：**> > The client must return the handle immediately after processing the request.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-media-type SourceOpenCallback = (request: MediaSourceLoadingRequest) => long--><!--Device-media-type SourceOpenCallback = (request: MediaSourceLoadingRequest) => long-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [MediaSourceLoadingRequest](arkts-media-media-mediasourceloadingrequest-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
