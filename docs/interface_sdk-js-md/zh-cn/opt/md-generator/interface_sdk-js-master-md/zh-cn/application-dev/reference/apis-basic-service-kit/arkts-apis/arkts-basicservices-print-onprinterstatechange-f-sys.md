# onPrinterStateChange（系统接口）

## 导入模块

```TypeScript
```

## onPrinterStateChange

```TypeScript
function onPrinterStateChange(callback: PrinterStateChangeCallback): void
```

Register event callback for the state change of printer.

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function onPrinterStateChange(callback: PrinterStateChangeCallback): void--><!--Device-print-function onPrinterStateChange(callback: PrinterStateChangeCallback): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [PrinterStateChangeCallback](arkts-basicservices-print-printerstatechangecallback-t-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
