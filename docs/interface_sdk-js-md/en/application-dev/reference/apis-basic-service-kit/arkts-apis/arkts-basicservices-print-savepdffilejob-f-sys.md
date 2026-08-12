# savePdfFileJob (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## savePdfFileJob

```TypeScript
function savePdfFileJob(jobId: string, fd: int): Promise<void>
```

Save the pdf file for a print job.

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
| jobId | string | Yes | Indicates the print job ID. &lt;br&gt;The print job ID to which the file to be saved belongs. |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the fd. &lt;br&gt;Fd of the file to be saved. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13100007 | Save file failed. |
| [13100006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-print.md#13100006-invalid-print-job) | Invalid job ID. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

