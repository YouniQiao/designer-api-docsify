# getDefaultVoiceSimId

## 导入模块

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getDefaultVoiceSimId

```TypeScript
function getDefaultVoiceSimId(callback: AsyncCallback<number>): void
```

获取默认语音业务的SIM卡ID。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300004](../errorcode-telephony.md#8300004-未识别sim卡) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [8301001](../errorcode-telephony.md#8301001-sim卡未激活) |


## getDefaultVoiceSimId

```TypeScript
function getDefaultVoiceSimId(): Promise<number>
```

获取默认语音业务的SIM卡ID。使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Telephony.CoreService

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300004](../errorcode-telephony.md#8300004-未识别sim卡) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [8301001](../errorcode-telephony.md#8301001-sim卡未激活) |
