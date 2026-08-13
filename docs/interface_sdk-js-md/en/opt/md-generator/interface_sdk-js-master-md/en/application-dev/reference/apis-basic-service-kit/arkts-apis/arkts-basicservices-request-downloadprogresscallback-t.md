# DownloadProgressCallback

```TypeScript
export type DownloadProgressCallback = (receivedSize: number, totalSize: number) => void
```

The callback function for the download progress event.

**Since:** 23

**Deprecated since:** -1

<!--Device-request-export type DownloadProgressCallback = (receivedSize: long, totalSize: long) => void--><!--Device-request-export type DownloadProgressCallback = (receivedSize: long, totalSize: long) => void-End-->

**System capability:** SystemCapability.MiscServices.Download

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| receivedSize | number | Yes |
| totalSize | number | Yes |
