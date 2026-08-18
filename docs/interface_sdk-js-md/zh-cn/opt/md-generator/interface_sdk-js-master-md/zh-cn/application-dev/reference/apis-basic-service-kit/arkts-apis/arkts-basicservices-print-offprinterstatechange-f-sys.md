# offPrinterStateChange（系统接口）

## 导入模块

```TypeScript
```

## offPrinterStateChange

```TypeScript
function offPrinterStateChange(callback?: Callback<boolean>): void
```

Unregister event callback for the state change of printer.

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function offPrinterStateChange(callback?: Callback<boolean>): void--><!--Device-print-function offPrinterStateChange(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
