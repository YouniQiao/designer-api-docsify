# OnProcess (System API)

```TypeScript
type OnProcess = (bundleName: string, process: string) => void
```

function that returns backup datasize by bundleName. Callback called when the backup_sa service return result information. The first return string parameter indicates the result of the bundle.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-backup-type OnProcess = (bundleName: string, process: string) => void--><!--Device-backup-type OnProcess = (bundleName: string, process: string) => void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| process | string | Yes |
