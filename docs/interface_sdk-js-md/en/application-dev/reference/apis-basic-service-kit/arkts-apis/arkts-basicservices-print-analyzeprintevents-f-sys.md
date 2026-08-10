# analyzePrintEvents (System API)

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## analyzePrintEvents

```TypeScript
function analyzePrintEvents(printerId: string, eventType: string): Promise<string>
```

分析打印事件。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function analyzePrintEvents(printerId: string, eventType: string): Promise<string>--><!--Device-print-function analyzePrintEvents(printerId: string, eventType: string): Promise<string>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| printerId | string | Yes | 打印机ID。 &lt;br&gt;要分析的打印机ID。 |
| eventType | string | Yes | 前卫类型。 &lt;br&gt;需要分析的事件类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | the application does not have permission to call this function. |
| 202 | not system application. |

