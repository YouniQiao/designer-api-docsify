# updatePrinterInDiscovery

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## updatePrinterInDiscovery

```TypeScript
function updatePrinterInDiscovery(printerInformation: PrinterInformation): Promise<void>
```

Updates the printer capabilities to the printer discovery list. This API uses a promise to return the result.

**Since:** 14

**Required permissions:** ohos.permission.PRINT

**System capability:** SystemCapability.Print.PrintFramework

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
