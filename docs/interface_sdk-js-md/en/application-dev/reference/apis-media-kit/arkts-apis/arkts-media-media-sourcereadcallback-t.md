# SourceReadCallback

```TypeScript
type SourceReadCallback = (uuid: long, requestedOffset: long, requestedLength: long) => void
```

This callback function is implemented by applications to handle resource read requests. When data is available, applications should push it to the player using the   
[respondData](arkts-media-media-mediasourceloadingrequest-i.md#responddata)API of the corresponding MediaSourceLoadingRequest object.

> **NOTE：**
> 
> The client must return the handle immediately after processing the request.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-media-type SourceReadCallback = (uuid: long, requestedOffset: long, requestedLength: long) => void--><!--Device-media-type SourceReadCallback = (uuid: long, requestedOffset: long, requestedLength: long) => void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | ID for the resource handle. |
| requestedOffset | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | Offset of the current media data relative to the start of the resource. |
| requestedLength | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | Length of the current request. The value **-1** indicates reaching the end of the resource. After pushing the data, call [finishLoading](arkts-media-media-mediasourceloadingrequest-i.md#finishloading) to notify the player that the push is complete. |

