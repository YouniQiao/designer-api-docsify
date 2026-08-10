# queryPrinterInfoByIp (System API)

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## queryPrinterInfoByIp

```TypeScript
function queryPrinterInfoByIp(printerIp: string): Promise<void>
```

根据ip查询打印机信息。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function queryPrinterInfoByIp(printerIp: string): Promise<void>--><!--Device-print-function queryPrinterInfoByIp(printerIp: string): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| printerIp | string | Yes | 打印机IP。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13100005 | Invalid printer IP. |
| 201 | the application does not have permission to call this function. |
| 202 | not system application. |

