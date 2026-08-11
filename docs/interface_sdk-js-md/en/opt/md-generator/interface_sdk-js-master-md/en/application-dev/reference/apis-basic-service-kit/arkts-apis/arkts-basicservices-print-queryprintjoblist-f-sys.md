# queryPrintJobList (System API)

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## queryPrintJobList

```TypeScript
function queryPrintJobList(callback: AsyncCallback<Array<PrintJob>>): void
```

Queries all print jobs. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function queryPrintJobList(callback: AsyncCallback<Array<PrintJob>>): void--><!--Device-print-function queryPrintJobList(callback: AsyncCallback<Array<PrintJob>>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;PrintJob&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.queryPrintJobList((err: BusinessError, printJobs : print.PrintJob[]) => {
    if (err) {
        console.error('queryPrintJobList failed, because : ' + JSON.stringify(err));
    } else {
        console.info('queryPrintJobList success, data : ' + JSON.stringify(printJobs));
    }
})
```


## queryPrintJobList

```TypeScript
function queryPrintJobList(): Promise<Array<PrintJob>>
```

Queries all print jobs. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function queryPrintJobList(): Promise<Array<PrintJob>>--><!--Device-print-function queryPrintJobList(): Promise<Array<PrintJob>>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;PrintJob&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.queryPrintJobList().then((printJobs : print.PrintJob[]) => {
    console.info('queryPrintJobList success, data : ' + JSON.stringify(printJobs));
}).catch((error: BusinessError) => {
    console.error('queryPrintJobList failed, error : ' + JSON.stringify(error));
})
```
