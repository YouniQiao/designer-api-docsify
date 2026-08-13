# authPrintJob (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## authPrintJob

```TypeScript
function authPrintJob(jobId: string, userName: string, password: string): Promise<boolean>
```

Authenticate a print job.

**Since:** 24

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function authPrintJob(jobId: string, userName: string, password: string): Promise<boolean>--><!--Device-print-function authPrintJob(jobId: string, userName: string, password: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| jobId | string | Yes |
| userName | string | Yes |
| password | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [13100006](../../apis-basic-services-kit/errorcode-print.md#13100006-invalid-print-job) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
