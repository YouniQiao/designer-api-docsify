# onPrinterInfoQuery (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## onPrinterInfoQuery

```TypeScript
function onPrinterInfoQuery(callback: PrinterInfoQueryCallback): void
```

Register event callback for the printer info queried.

**Since:** 24

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function onPrinterInfoQuery(callback: PrinterInfoQueryCallback): void--><!--Device-print-function onPrinterInfoQuery(callback: PrinterInfoQueryCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PrinterInfoQueryCallback](arkts-basicservices-print-printerinfoquerycallback-t-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
