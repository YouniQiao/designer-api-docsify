# setCBConfigList（系统接口）

## 导入模块

```TypeScript
```

## setCBConfigList

```TypeScript
function setCBConfigList(configs: CBConfigListConfigs): Promise<void>
```

打开小区广播列表

**起始版本：** 23

**需要权限：** ohos.permission.RECEIVE_SMS

<!--Device-sms-function setCBConfigList(configs: CBConfigListConfigs): Promise<void>--><!--Device-sms-function setCBConfigList(configs: CBConfigListConfigs): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| configs | [CBConfigListConfigs](arkts-telephony-sms-cbconfiglistconfigs-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
