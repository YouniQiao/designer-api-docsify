# onPrinterChange

## 导入模块

```TypeScript
```

## onPrinterChange

```TypeScript
function onPrinterChange(callback: PrinterChangeCallback): void
```

Register event callback for the change of printer.

**起始版本：** 23

**需要权限：** ohos.permission.PRINT

<!--Device-print-function onPrinterChange(callback: PrinterChangeCallback): void--><!--Device-print-function onPrinterChange(callback: PrinterChangeCallback): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
