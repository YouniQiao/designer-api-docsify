# OnFileReadyBatch (System API)

```TypeScript
type OnFileReadyBatch = (error: BusinessError<void>, files: Array<File>) => void
```

Function that returns array of file handle.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-backup-type OnFileReadyBatch = (error: BusinessError<void>, files: Array<File>) => void--><!--Device-backup-type OnFileReadyBatch = (error: BusinessError<void>, files: Array<File>) => void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| error | [BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&lt;void&gt; | Yes |
| files | Array&lt;File&gt; | Yes |
