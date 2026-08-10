# authPrintJob (System API)

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## authPrintJob

```TypeScript
function authPrintJob(jobId: string, userName: string, password: string): Promise<boolean>
```

验证打印作业。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function authPrintJob(jobId: string, userName: string, password: string): Promise<boolean>--><!--Device-print-function authPrintJob(jobId: string, userName: string, password: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobId | string | Yes | 打印作业ID。 &lt;br&gt;要打印的作业ID。 |
| userName | string | Yes | 用户名。 &lt;br&gt;用户名。 |
| password | string | Yes | 用户密码。 &lt;br&gt;用户密码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13100006 | Can not find the print job. |
| 201 | the application does not have permission to call this function. |
| 202 | not system application. |

