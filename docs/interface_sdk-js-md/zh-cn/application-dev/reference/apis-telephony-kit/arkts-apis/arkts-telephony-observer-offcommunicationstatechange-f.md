# offCommunicationStateChange

## 导入模块

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## offCommunicationStateChange

```TypeScript
function offCommunicationStateChange(callback: Callback<boolean>, options?: ObserverOptions): void
```

取消订阅5A网络状态变化事件，使用callback异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.GET_NETWORK_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
