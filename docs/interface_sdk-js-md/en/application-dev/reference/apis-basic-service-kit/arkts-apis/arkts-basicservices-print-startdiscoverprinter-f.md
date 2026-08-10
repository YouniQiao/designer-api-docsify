# startDiscoverPrinter

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## startDiscoverPrinter

```TypeScript
function startDiscoverPrinter(extensionList: Array<string>, callback: AsyncCallback<void>): void
```

通过指定“打印扩展能力列表”来发现打印机，发现的打印机具备包含指定的打印扩展能力。如果指定空的打印扩展能力列表，则表示加载所有扩展能力。使用callback异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 20+: ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
- API version 10 - 19: ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function startDiscoverPrinter(extensionList: Array<string>, callback: AsyncCallback<void>): void--><!--Device-print-function startDiscoverPrinter(extensionList: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| extensionList | Array&lt;string&gt; | Yes | 要加载的 [打印扩展能力](arkts-basicservices-app-ability-printextensionability-printextensionability-c.md)列表，列表成员为打印扩展能力的包名，空列表表示加载所有扩展能力。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 异步开始发现打印机之后的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 202 | not system application<br>**Applicable version:** 10 - 19 |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Load all print extension abilities.
let extensionList: string[] = [];
// Specify the bundle name of your applications to load required print extension abilities during printer discovery.
// let extensionList: string[] = ['com.myapplication.test'];
print.startDiscoverPrinter(extensionList, (err: BusinessError) => {
    if (err) {
        console.error('failed to start Discover Printer because : ' + JSON.stringify(err));
    } else {
        console.info('start Discover Printer success');
    }
})
```


## startDiscoverPrinter

```TypeScript
function startDiscoverPrinter(extensionList: Array<string>): Promise<void>
```

通过指定“打印扩展能力列表”来发现打印机，发现的打印机具备包含指定的打印扩展能力。如果指定空的打印扩展能力列表，则表示加载所有扩展能力，使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 20+: ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
- API version 10 - 19: ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function startDiscoverPrinter(extensionList: Array<string>): Promise<void>--><!--Device-print-function startDiscoverPrinter(extensionList: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| extensionList | Array&lt;string&gt; | Yes | 要加载的 [打印扩展能力](arkts-basicservices-app-ability-printextensionability-printextensionability-c.md)列表，列表成员为打印扩展能力的包名，空列表表示加载所有扩展能力。 |

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

// Load all print extension abilities.
let extensionList: string[] = [];
// Specify the bundle name of your applications to load required print extension abilities during printer discovery.
// let extensionList: string[] = ['com.myapplication.test'];
print.startDiscoverPrinter(extensionList).then(() => {
    console.info('start Discovery success');
}).catch((error: BusinessError) => {
    console.error('failed to start Discovery because : ' + JSON.stringify(error));
})
```

