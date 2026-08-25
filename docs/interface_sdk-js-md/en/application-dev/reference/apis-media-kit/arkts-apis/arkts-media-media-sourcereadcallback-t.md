# SourceReadCallback

```TypeScript
type SourceReadCallback = (uuid: long, requestedOffset: long, requestedLength: long) => void
```

This callback function is implemented by applications to handle resource read requests. When data is available, applications should push it to the player using the [respondData](arkts-media-media-mediasourceloadingrequest-i.md#responddata) API of the corresponding MediaSourceLoadingRequest object.

> **NOTE：**&gt;
> The client must return the handle immediately after processing the request.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uuid | ArkTS-Dyn: number<br>ArkTS-Sta：long | Yes |
| requestedOffset | ArkTS-Dyn: number<br>ArkTS-Sta：long | Yes |
| requestedLength | ArkTS-Dyn: number<br>ArkTS-Sta：long | Yes |

**Examples**

```TypeScript
let sourceReadCallback: media.SourceReadCallback = (uuid: number, requestedOffset: number, requestedLength: number) => {
  console.info(`Reading resource with handle ${uuid}, offset: ${requestedOffset}, length: ${requestedLength}`);
  // Check whether the UUID is valid and store the read request. Avoid blocking the request while pushing data and header information.
};
```
