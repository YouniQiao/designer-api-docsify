# hasCall

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## hasCall

```TypeScript
function hasCall(callback: AsyncCallback<boolean>): void
```

判断是否存在通话。使用callback异步回调。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## hasCall

```TypeScript
function hasCall(): Promise<boolean>
```

判断是否存在通话。使用Promise异步回调。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.CallManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
