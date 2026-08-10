# OnResultReport (System API)

```TypeScript
type OnResultReport = (bundleName: string, result: string) => void
```

备份服务返回结果信息时触发的回调。第一个字符串参数表示触发回调的应用名称。第二个字符串参数表示应用的处理结果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-backup-type OnResultReport = (bundleName: string, result: string) => void--><!--Device-backup-type OnResultReport = (bundleName: string, result: string) => void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 触发回调的应用名称。 |
| result | string | Yes | 应用备份或恢复的结果信息。 |

