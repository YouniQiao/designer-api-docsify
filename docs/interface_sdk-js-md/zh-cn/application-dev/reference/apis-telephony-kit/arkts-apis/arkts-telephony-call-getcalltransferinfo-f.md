# getCallTransferInfo

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## getCallTransferInfo

```TypeScript
function getCallTransferInfo(type: CallTransferType, number: string): Promise<CallTransferResult>
```

获取电话号码的呼叫转移状态。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.GET_CALL_TRANSFER_INFO

**系统能力：** SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [CallTransferType](arkts-telephony-call-calltransfertype-e.md) | 是 |
| number | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CallTransferResult](arkts-telephony-call-calltransferresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8401002](../errorcode-telephony.md#8401002-输入号码错误) |
| [8401003](../errorcode-telephony.md#8401003-操作频繁) |
