# getCallState

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## getCallState

```TypeScript
function getCallState(callback: AsyncCallback<CallState>): void
```

获取当前通话状态。使用callback异步回调。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CallState&gt; | 是 |


## getCallState

```TypeScript
function getCallState(): Promise<CallState>
```

获取当前通话状态。使用Promise异步回调。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.CallManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;CallState & gt; |
