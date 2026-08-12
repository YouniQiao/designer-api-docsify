# getPrinterInfoById (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## getPrinterInfoById

```TypeScript
function getPrinterInfoById(printerId: string): Promise<PrinterInfo>
```

Obtains printer information based on the printer ID. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function getPrinterInfoById(printerId: string): Promise<PrinterInfo>--><!--Device-print-function getPrinterInfoById(printerId: string): Promise<PrinterInfo>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PrinterInfo](arkts-basicservices-print-printerinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerId : string = '1';
print.getPrinterInfoById(printerId).then((printerInfo : print.PrinterInfo) => {
    console.info('getPrinterInfoById data : ' + JSON.stringify(printerInfo));
}).catch((error: BusinessError) => {
    console.error('getPrinterInfoById error : ' + JSON.stringify(error));
})
```
