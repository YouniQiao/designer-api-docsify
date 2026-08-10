# stopDiscoverPrinter

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## stopDiscoverPrinter

```TypeScript
function stopDiscoverPrinter(callback: AsyncCallback<void>): void
```

停止发现打印机，使用callback异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 20+: ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
- API version 10 - 19: ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function stopDiscoverPrinter(callback: AsyncCallback<void>): void--><!--Device-print-function stopDiscoverPrinter(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 停止发现打印机的异步回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 202 | not system application<br>**Applicable version:** 10 - 19 |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.stopDiscoverPrinter((err: BusinessError) => {
    if (err) {
        console.error('failed to stop Discover Printer because : ' + JSON.stringify(err));
    } else {
        console.info('stop Discover Printer success');
    }
})
```


## stopDiscoverPrinter

```TypeScript
function stopDiscoverPrinter(): Promise<void>
```

停止发现打印机，使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 20+: ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
- API version 10 - 19: ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function stopDiscoverPrinter(): Promise<void>--><!--Device-print-function stopDiscoverPrinter(): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 202 | not system application<br>**Applicable version:** 10 - 19 |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.stopDiscoverPrinter().then(() => {
    console.info('stop Discovery success');
}).catch((error: BusinessError) => {
    console.error('failed to stop Discovery because : ' + JSON.stringify(error));
})
```

