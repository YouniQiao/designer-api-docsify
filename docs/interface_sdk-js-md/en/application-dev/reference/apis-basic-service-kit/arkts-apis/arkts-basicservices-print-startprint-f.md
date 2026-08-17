# startPrint

## Modules to Import

```TypeScript
import { print } from 'print';
```

## startPrint

```TypeScript
function startPrint(job: PrintJobData): Promise<void>
```

Prints a file or binary data. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.PRINT

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function startPrint(job: PrintJobData): Promise<void>--><!--Device-print-function startPrint(job: PrintJobData): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| job | [PrintJobData](arkts-basicservices-print-printjobdata-i.md) | Yes | Print job data. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |

