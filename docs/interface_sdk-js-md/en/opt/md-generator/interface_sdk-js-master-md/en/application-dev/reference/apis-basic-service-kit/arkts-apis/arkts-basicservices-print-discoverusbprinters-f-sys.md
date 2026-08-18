# discoverUsbPrinters (System API)

## Modules to Import

```TypeScript
```

## discoverUsbPrinters

```TypeScript
function discoverUsbPrinters(): Promise<Array<PrinterInformation>>
```

Discovers USB printers. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function discoverUsbPrinters(): Promise<Array<PrinterInformation>>--><!--Device-print-function discoverUsbPrinters(): Promise<Array<PrinterInformation>>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[PrinterInformation](arkts-basicservices-print-printerinformation-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.discoverUsbPrinters().then((printers : print.PrinterInformation[]) => {
    console.info('discoverUsbPrinters data : ' + JSON.stringify(printers));
}).catch((error: BusinessError) => {
    console.error('discoverUsbPrinters error : ' + JSON.stringify(error));
})
```
