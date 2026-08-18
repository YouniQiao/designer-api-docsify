# offIccAccountInfoChange

## 导入模块

```TypeScript
```

## offIccAccountInfoChange

```TypeScript
function offIccAccountInfoChange(callback?: Callback<void>): void
```

Cancel to receive an ICC account change.

**起始版本：** 23

<!--Device-observer-function offIccAccountInfoChange(callback?: Callback<void>): void--><!--Device-observer-function offIccAccountInfoChange(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
