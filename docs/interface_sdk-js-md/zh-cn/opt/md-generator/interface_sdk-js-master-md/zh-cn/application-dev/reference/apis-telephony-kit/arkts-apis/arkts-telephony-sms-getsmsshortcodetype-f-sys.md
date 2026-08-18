# getSmsShortCodeType（系统接口）

## 导入模块

```TypeScript
```

## getSmsShortCodeType

```TypeScript
function getSmsShortCodeType(slotId: number, destAddr: string): Promise<SmsShortCodeType>
```

获取拟发送短信的目标地址短码类型

**起始版本：** 23

**需要权限：** ohos.permission.SEND_MESSAGES

<!--Device-sms-function getSmsShortCodeType(slotId: int, destAddr: string): Promise<SmsShortCodeType>--><!--Device-sms-function getSmsShortCodeType(slotId: int, destAddr: string): Promise<SmsShortCodeType>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| destAddr | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SmsShortCodeType](arkts-telephony-sms-smsshortcodetype-e-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300004](../errorcode-telephony.md#8300004-未识别sim卡) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
