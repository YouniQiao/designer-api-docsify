# addPrinter

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## addPrinter

```TypeScript
function addPrinter(printerName: string, uri: string, ppdName?: string, options?: string): Promise<boolean>
```

Add a printer to system.

**Since:** 24

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINTER_DRIVER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerName | string | Yes |
| uri | string | Yes |
| [ppdName](arkts-basicservices-print-ppdinfo-i.md) | string | No |
| options | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [13100003](../errorcode-print.md#13100003-print-service-error) |
