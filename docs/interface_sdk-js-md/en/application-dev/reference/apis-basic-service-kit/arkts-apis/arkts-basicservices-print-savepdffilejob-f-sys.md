# savePdfFileJob (System API)

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## savePdfFileJob

```TypeScript
function savePdfFileJob(jobId: string, fd: int): Promise<void>
```

保存打印作业的pdf文件。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function savePdfFileJob(jobId: string, fd: int): Promise<void>--><!--Device-print-function savePdfFileJob(jobId: string, fd: int): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobId | string | Yes | 打印作业ID。 |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文件描述符。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13100007 | Save file failed. |
| 13100006 | Invalid job ID. |
| 201 | the application does not have permission to call this function. |
| 202 | not system application. |

