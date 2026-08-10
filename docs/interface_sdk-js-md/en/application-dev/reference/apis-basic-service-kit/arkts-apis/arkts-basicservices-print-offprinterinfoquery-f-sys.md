# offPrinterInfoQuery (System API)

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## offPrinterInfoQuery

```TypeScript
function offPrinterInfoQuery(callback?: PrinterInfoQueryCallback): void
```

查询到的打印机信息的Unregister事件回调。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function offPrinterInfoQuery(callback?: PrinterInfoQueryCallback): void--><!--Device-print-function offPrinterInfoQuery(callback?: PrinterInfoQueryCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PrinterInfoQueryCallback](arkts-basicservices-print-printerinfoquerycallback-t-sys.md) | No | 查询到的打印机信息的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 202 | not system application. |

