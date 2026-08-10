# OnFileReadyBatch (System API)

```TypeScript
type OnFileReadyBatch = (error: BusinessError<void>, files: Array<File>) => void
```

一批文件准备好发送给客户端时触发的回调函数。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-backup-type OnFileReadyBatch = (error: BusinessError<void>, files: Array<File>) => void--><!--Device-backup-type OnFileReadyBatch = (error: BusinessError<void>, files: Array<File>) => void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| error | [BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-c.md)&lt;void&gt; | Yes | 获取文件句柄失败时返回的错误对象。 |
| files | Array&lt;File&gt; | Yes | 获取到的文件句柄数组。 |

