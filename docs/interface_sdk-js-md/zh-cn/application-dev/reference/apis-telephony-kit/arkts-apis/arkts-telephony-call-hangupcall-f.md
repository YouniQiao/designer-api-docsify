# hangUpCall

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## hangUpCall

```TypeScript
function hangUpCall(callback: AsyncCallback<void>): void
```

挂断电话。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ANSWER_CALL or ohos.permission.SET_TELEPHONY_STATE or ohos.permission.MANAGE_CALL_FOR_DEVICES

**系统能力：** SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
