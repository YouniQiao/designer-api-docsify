# SourceCloseCallback

```TypeScript
type SourceCloseCallback = (uuid: long) => void
```

This callback function is implemented by applications to release related resources. &gt; **NOTE：**&gt; &gt; The client must return the handle immediately after processing the request.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-media-type SourceCloseCallback = (uuid: long) => void--><!--Device-media-type SourceCloseCallback = (uuid: long) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | long | Yes | ID for the resource handle. |

