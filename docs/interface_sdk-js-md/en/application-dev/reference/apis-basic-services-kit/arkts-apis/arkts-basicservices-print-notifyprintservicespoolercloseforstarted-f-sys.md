# notifyPrintServiceSpoolerCloseForStarted (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## notifyPrintServiceSpoolerCloseForStarted

```TypeScript
function notifyPrintServiceSpoolerCloseForStarted(jobId: string, callback: AsyncCallback<void>): void
```

Notify print service the information.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function notifyPrintServiceSpoolerCloseForStarted(jobId: string, callback: AsyncCallback<void>): void--><!--Device-print-function notifyPrintServiceSpoolerCloseForStarted(jobId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobId | string | Yes | Indicates id of the print job. |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | The callback function for indicating the result of API execution. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application |


## notifyPrintServiceSpoolerCloseForStarted

```TypeScript
function notifyPrintServiceSpoolerCloseForStarted(jobId: string): Promise<void>
```

Notify print service the information.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function notifyPrintServiceSpoolerCloseForStarted(jobId: string): Promise<void>--><!--Device-print-function notifyPrintServiceSpoolerCloseForStarted(jobId: string): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobId | string | Yes | Indicates id of the print job. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application |

