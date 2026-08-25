# getDefaultSmsSlotId

## 导入模块

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## getDefaultSmsSlotId

```TypeScript
function getDefaultSmsSlotId(callback: AsyncCallback<number>): void
```

获取发送短信的默认SIM卡槽ID。使用callback异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.SmsMms

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## getDefaultSmsSlotId

```TypeScript
function getDefaultSmsSlotId(): Promise<number>
```

获取发送短信的默认SIM卡槽ID。使用Promise异步回调。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.SmsMms

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
