# setDefaultPrinter (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## setDefaultPrinter

```TypeScript
function setDefaultPrinter(printerId: string, type: DefaultPrinterType): Promise<void>
```

Sets the default printer. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function setDefaultPrinter(printerId: string, type: DefaultPrinterType): Promise<void>--><!--Device-print-function setDefaultPrinter(printerId: string, type: DefaultPrinterType): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerId | string | Yes |
| type | [DefaultPrinterType](arkts-basicservices-print-defaultprintertype-e.md) | Yes |

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

let printerId : string = '1';
let type : print.DefaultPrinterType = print.DefaultPrinterType.DEFAULT_PRINTER_TYPE_SET_BY_USER;
print.setDefaultPrinter(printerId, type).then(() => {
    console.info('setDefaultPrinter success');
}).catch((error: BusinessError) => {
    console.error('setDefaultPrinter error : ' + JSON.stringify(error));
})
```
