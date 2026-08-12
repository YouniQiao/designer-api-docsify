# onPrinterStateChange（系统接口）

## onPrinterStateChange

```TypeScript
function onPrinterStateChange(callback: PrinterStateChangeCallback): void
```

Register event callback for the state change of printer.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function onPrinterStateChange(callback: PrinterStateChangeCallback): void--><!--Device-print-function onPrinterStateChange(callback: PrinterStateChangeCallback): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [PrinterStateChangeCallback](arkts-basicservices-print-printerstatechangecallback-t-sys.md) | 是 | The callback function for state change of printer. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | the application does not have permission to call this function. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | not system application |

