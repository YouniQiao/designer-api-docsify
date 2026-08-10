# offPrinterChange

## 导入模块

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## offPrinterChange

```TypeScript
function offPrinterChange(callback?: PrinterChangeCallback): void
```

Unregister event callback for the change of printer.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.PRINT

<!--Device-print-function offPrinterChange(callback?: PrinterChangeCallback): void--><!--Device-print-function offPrinterChange(callback?: PrinterChangeCallback): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | 否 | The callback function for change of printer. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 201 | the application does not have permission to call this function. |

