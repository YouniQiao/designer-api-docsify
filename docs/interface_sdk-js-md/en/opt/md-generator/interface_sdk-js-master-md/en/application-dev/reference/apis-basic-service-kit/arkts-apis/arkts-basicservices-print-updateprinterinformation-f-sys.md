# updatePrinterInformation (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## updatePrinterInformation

```TypeScript
function updatePrinterInformation(printerInformation: PrinterInformation): Promise<void>
```

Updates the information of a printer in the system. This API uses a promise to return the result. Currently, only the **alias** and **options** fields of [PrinterInformation](arkts-basicservices-print-printerinformation-i.md#PrinterInformation) can be updated.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 24+: ohos.permission.MANAGE_PRINT_JOB or ohos.permission.ENTERPRISE_MANAGE_PRINT
- API version 18 - 23: ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function updatePrinterInformation(printerInformation: PrinterInformation): Promise<void>--><!--Device-print-function updatePrinterInformation(printerInformation: PrinterInformation): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerInformation | [PrinterInformation](arkts-basicservices-print-printerinformation-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let testPageSize : print.PrintPageSize = {
    id : 'ISO_A4',
    name : 'iso_a4_210x297mm',
    width : 8268,
    height : 11692
};

let testCapability : print.PrinterCapabilities = {
    supportedPageSizes : [testPageSize],
    supportedColorModes : [print.PrintColorMode.COLOR_MODE_MONOCHROME],
    supportedDuplexModes : [print.PrintDuplexMode.DUPLEX_MODE_NONE],
    supportedMediaTypes : ['stationery'],
    supportedQualities : [print.PrintQuality.QUALITY_NORMAL],
    supportedOrientations : [print.PrintOrientationMode.ORIENTATION_MODE_PORTRAIT],
    options : 'testOptions'
};

let printerInformation : print.PrinterInformation = {
    printerId : 'testPrinterId',
    printerName : 'testPrinterName',
    printerStatus : 0,
    description : 'testDesc',
    capability : testCapability,
    uri : 'testUri',
    printerMake : 'testPrinterMake',
    options : 'testOptions'
};
print.updatePrinterInformation(printerInformation).then(() => {
    console.info('updatePrinterInformation success');
}).catch((error: BusinessError) => {
    console.error('updatePrinterInformation error : ' + JSON.stringify(error));
})
```
