# queryAllPrinterExtensionInfos (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## queryAllPrinterExtensionInfos

```TypeScript
function queryAllPrinterExtensionInfos(callback: AsyncCallback<Array<PrinterExtensionInfo>>): void
```

Obtains the information of all installed printer extensions. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function queryAllPrinterExtensionInfos(callback: AsyncCallback<Array<PrinterExtensionInfo>>): void--><!--Device-print-function queryAllPrinterExtensionInfos(callback: AsyncCallback<Array<PrinterExtensionInfo>>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[PrinterExtensionInfo](arkts-basicservices-print-printerextensioninfo-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.queryAllPrinterExtensionInfos((err: BusinessError, extensionInfos: print.PrinterExtensionInfo[]) => {
    if (err) {
        console.error('queryAllPrinterExtensionInfos err ' + JSON.stringify(err));
    } else {
        console.info('queryAllPrinterExtensionInfos success ' + JSON.stringify(extensionInfos));
    }
})
```


## queryAllPrinterExtensionInfos

```TypeScript
function queryAllPrinterExtensionInfos(): Promise<Array<PrinterExtensionInfo>>
```

Obtains the information of all installed printer extensions. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function queryAllPrinterExtensionInfos(): Promise<Array<PrinterExtensionInfo>>--><!--Device-print-function queryAllPrinterExtensionInfos(): Promise<Array<PrinterExtensionInfo>>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[PrinterExtensionInfo](arkts-basicservices-print-printerextensioninfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.queryAllPrinterExtensionInfos().then((extensionInfos: print.PrinterExtensionInfo[]) => {
    console.info('queryAllPrinterExtensionInfos success ' + JSON.stringify(extensionInfos));
    // ...
}).catch((error: BusinessError) => {
    console.error('failed to get AllPrinterExtension because ' + JSON.stringify(error));
})
```
