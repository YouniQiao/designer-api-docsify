# authSmbDeviceAsRegisteredUser（系统接口）

## authSmbDeviceAsRegisteredUser

```TypeScript
function authSmbDeviceAsRegisteredUser(host: SharedHost, username: string, password: string): Promise<PrinterInformation[]>
```

以注册用户身份对SMB设备进行身份验证，并获取可用打印机。

**起始版本：** 24

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-print-function authSmbDeviceAsRegisteredUser(host: SharedHost, username: string, password: string): Promise<PrinterInformation[]>--><!--Device-print-function authSmbDeviceAsRegisteredUser(host: SharedHost, username: string, password: string): Promise<PrinterInformation[]>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| host | [SharedHost](arkts-basicservices-print-sharedhost-i.md) | 是 |
| [username](../../apis-arkts/arkts-apis/arkts-arkts-url-url-c.md) | string | 是 |
| password | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PrinterInformation](arkts-basicservices-print-printerinformation-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| 13100014 |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| 13100013 |
| 13100012 |
