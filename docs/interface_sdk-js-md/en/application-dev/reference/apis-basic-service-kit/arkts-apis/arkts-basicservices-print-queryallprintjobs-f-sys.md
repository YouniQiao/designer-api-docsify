# queryAllPrintJobs (System API)

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## queryAllPrintJobs

```TypeScript
function queryAllPrintJobs(callback: AsyncCallback<void>): void
```

查询所有打印任务，使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Deprecated since:** 11

**Substitutes:** [null]

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function queryAllPrintJobs(callback: AsyncCallback<void>): void--><!--Device-print-function queryAllPrintJobs(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 异步查询所有打印任务之后的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 202 | not system application |


## queryAllPrintJobs

```TypeScript
function queryAllPrintJobs(): Promise<void>
```

查询所有打印任务，使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Deprecated since:** 11

**Substitutes:** [null]

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function queryAllPrintJobs(): Promise<void>--><!--Device-print-function queryAllPrintJobs(): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 202 | not system application |

