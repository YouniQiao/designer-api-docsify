# OnBackupSizeReport (System API)

```TypeScript
type OnBackupSizeReport = (reportInfo: string) => void
```

function that returns backup datasize by bundleName.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-backup-type OnBackupSizeReport = (reportInfo: string) => void--><!--Device-backup-type OnBackupSizeReport = (reportInfo: string) => void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reportInfo | string | Yes | the scanned backup datasize infos. |

