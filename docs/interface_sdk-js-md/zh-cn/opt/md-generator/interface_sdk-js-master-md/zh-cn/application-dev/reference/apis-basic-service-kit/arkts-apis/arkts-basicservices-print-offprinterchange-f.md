# offPrinterChange

## offPrinterChange

```TypeScript
function offPrinterChange(callback?: PrinterChangeCallback): void
```

Unregister event callback for the change of printer.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PRINT

<!--Device-print-function offPrinterChange(callback?: PrinterChangeCallback): void--><!--Device-print-function offPrinterChange(callback?: PrinterChangeCallback): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
