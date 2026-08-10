# OnBackupSizeReport (System API)

```TypeScript
type OnBackupSizeReport = (reportInfo: string) => void
```

返回应用备份数据量信息的回调函数。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-backup-type OnBackupSizeReport = (reportInfo: string) => void--><!--Device-backup-type OnBackupSizeReport = (reportInfo: string) => void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reportInfo | string | Yes | 框架扫描到的应用待备份数据量信息，为JSON格式字符串。 |

