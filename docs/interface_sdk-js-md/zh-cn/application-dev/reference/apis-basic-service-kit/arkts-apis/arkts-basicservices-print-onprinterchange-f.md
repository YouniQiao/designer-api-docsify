# onPrinterChange

## 导入模块

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## onPrinterChange

```TypeScript
function onPrinterChange(callback: PrinterChangeCallback): void
```

Register event callback for the change of printer.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.PRINT

<!--Device-print-function onPrinterChange(callback: PrinterChangeCallback): void--><!--Device-print-function onPrinterChange(callback: PrinterChangeCallback): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | 是 | The callback function for change of printer. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 201 | the application does not have permission to call this function. |

