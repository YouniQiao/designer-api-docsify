# onExtInfoChange（系统接口）

## onExtInfoChange

```TypeScript
function onExtInfoChange(callback: ExtInfoChangeCallback): void
```

Register event callback for the information change of print extension.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function onExtInfoChange(callback: ExtInfoChangeCallback): void--><!--Device-print-function onExtInfoChange(callback: ExtInfoChangeCallback): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ExtInfoChangeCallback](arkts-basicservices-print-extinfochangecallback-t-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
