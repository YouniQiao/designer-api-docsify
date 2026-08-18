# DataCallback(跨设备唤醒与消息传输)（系统接口）

```TypeScript
type DataCallback = (deviceId: string, msg: ArrayBuffer) => void
```

数据接收回调函数类型。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-conversation-type DataCallback = (deviceId: string, msg: ArrayBuffer) => void--><!--Device-conversation-type DataCallback = (deviceId: string, msg: ArrayBuffer) => void-End-->

**系统能力：** SystemCapability.Communication.SoftBus.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| msg | ArrayBuffer | 是 |
