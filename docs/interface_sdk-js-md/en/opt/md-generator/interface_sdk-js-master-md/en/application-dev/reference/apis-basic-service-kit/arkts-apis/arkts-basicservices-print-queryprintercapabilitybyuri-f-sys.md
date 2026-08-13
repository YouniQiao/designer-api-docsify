# queryPrinterCapabilityByUri (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## queryPrinterCapabilityByUri

```TypeScript
function queryPrinterCapabilityByUri(printerUri: string, printerId: string): Promise<PrinterCapabilities>
```

Query printer capabilityies by printer uri.

**Since:** 24

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function queryPrinterCapabilityByUri(printerUri: string, printerId: string): Promise<PrinterCapabilities>--><!--Device-print-function queryPrinterCapabilityByUri(printerUri: string, printerId: string): Promise<PrinterCapabilities>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerUri | string | Yes |
| printerId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PrinterCapabilities](arkts-basicservices-print-printercapabilities-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [13100005](../../apis-basic-services-kit/errorcode-print.md#13100005-invalid-printer) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
