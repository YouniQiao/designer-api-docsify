# DownloadProgressCallback

```TypeScript
export type DownloadProgressCallback = (receivedSize: long, totalSize: long) => void
```

The callback function for the download progress event.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.MiscServices.Download

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| receivedSize | long | Yes |
| totalSize | long | Yes |
