# setPrinterPreferences (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## setPrinterPreferences

```TypeScript
function setPrinterPreferences(printerId: string, printerPreferences: PrinterPreferences): Promise<void>
```

Sets the printer preferences. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function setPrinterPreferences(printerId: string, printerPreferences: PrinterPreferences): Promise<void>--><!--Device-print-function setPrinterPreferences(printerId: string, printerPreferences: PrinterPreferences): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerId | string | Yes |
| printerPreferences | [PrinterPreferences](arkts-basicservices-print-printerpreferences-i.md) | Yes |

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

let printerId : string = 'testPrinterId';
let preferences : print.PrinterPreferences = {
    defaultDuplexMode: print.PrintDuplexMode.DUPLEX_MODE_NONE
};
print.setPrinterPreferences(printerId, preferences).then(() => {
    console.info('setPrinterPreferences success');
}).catch((error: BusinessError) => {
    console.error('setPrinterPreferences error : ' + JSON.stringify(error));
})
```
