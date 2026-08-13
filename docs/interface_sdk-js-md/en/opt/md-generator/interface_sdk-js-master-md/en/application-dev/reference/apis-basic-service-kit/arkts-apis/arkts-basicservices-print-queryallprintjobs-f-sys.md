# queryAllPrintJobs (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## queryAllPrintJobs

```TypeScript
function queryAllPrintJobs(callback: AsyncCallback<void>): void
```

Queries all print jobs. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 11

**Substitutes:** null

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function queryAllPrintJobs(callback: AsyncCallback<void>): void--><!--Device-print-function queryAllPrintJobs(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## queryAllPrintJobs

```TypeScript
function queryAllPrintJobs(): Promise<void>
```

Queries all print jobs. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 11

**Substitutes:** null

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function queryAllPrintJobs(): Promise<void>--><!--Device-print-function queryAllPrintJobs(): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
