# savePdfFileJob (System API)

## Modules to Import

```TypeScript
```

## savePdfFileJob

```TypeScript
function savePdfFileJob(jobId: string, fd: number): Promise<void>
```

Save the pdf file for a print job.

**Since:** 24

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function savePdfFileJob(jobId: string, fd: int): Promise<void>--><!--Device-print-function savePdfFileJob(jobId: string, fd: int): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| jobId | string | Yes |
| fd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13100007 |
| [13100006](../../apis-basic-services-kit/errorcode-print.md#13100006-invalid-print-job) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
