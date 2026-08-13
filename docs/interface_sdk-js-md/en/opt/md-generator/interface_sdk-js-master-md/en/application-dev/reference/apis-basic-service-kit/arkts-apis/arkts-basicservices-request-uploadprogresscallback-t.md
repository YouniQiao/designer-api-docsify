# UploadProgressCallback

```TypeScript
export type UploadProgressCallback = (uploadedSize: number, totalSize: number) => void
```

The callback function for the download progress event.

**Since:** 23

**Deprecated since:** -1

<!--Device-request-export type UploadProgressCallback = (uploadedSize: long, totalSize: long) => void--><!--Device-request-export type UploadProgressCallback = (uploadedSize: long, totalSize: long) => void-End-->

**System capability:** SystemCapability.MiscServices.Upload

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uploadedSize | number | Yes |
| totalSize | number | Yes |
