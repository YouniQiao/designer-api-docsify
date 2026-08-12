# offPrinterInfoQuery (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## offPrinterInfoQuery

```TypeScript
function offPrinterInfoQuery(callback?: PrinterInfoQueryCallback): void
```

Unregister event callback for the printer info queried.

**Since:** 24

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function offPrinterInfoQuery(callback?: PrinterInfoQueryCallback): void--><!--Device-print-function offPrinterInfoQuery(callback?: PrinterInfoQueryCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [PrinterInfoQueryCallback](arkts-basicservices-print-printerinfoquerycallback-t-sys.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
