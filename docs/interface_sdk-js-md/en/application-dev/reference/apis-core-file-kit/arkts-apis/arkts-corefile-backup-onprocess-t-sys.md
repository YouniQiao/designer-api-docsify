# OnProcess (System API)

```TypeScript
type OnProcess = (bundleName: string, process: string) => void
```

返回应用备份数据量信息的回调函数。备份服务返回结果或进度信息时触发的回调。返回应用的处理结果或进度信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-backup-type OnProcess = (bundleName: string, process: string) => void--><!--Device-backup-type OnProcess = (bundleName: string, process: string) => void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 触发回调的应用名称。 |
| process | string | Yes | 应用备份或恢复的进度信息。 |

