# onDropDetect

## 导入模块

```TypeScript
import { deviceStatus } from '@kit.MultimodalAwarenessKit';
```

## onDropDetect

```TypeScript
function onDropDetect(callback: Callback<DropDetectionStatus>): void
```

订阅设备跌落检测事件。当应用需要检测设备是否发生跌落时使用。调用onDropDetect订阅后，系统开始监听加速度传感器数据。当检测到符合跌落特征的加速度变化时，触发STATUS_DROPPED回调。同一回调实例不可重复订阅，需先调用offDropDetect取消后再订阅。建议在不需要监听时调用offDropDetect()取消订阅，释放资源。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceStatus-function onDropDetect(callback: Callback<DropDetectionStatus>): void--><!--Device-deviceStatus-function onDropDetect(callback: Callback<DropDetectionStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DeviceStatus

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DropDetectionStatus](arkts-multimodalawareness-devicestatus-dropdetectionstatus-e.md)&gt; | 是 | 回调函数，返回设备跌落检测状态信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br> 1. The hardware does not support the capability; <br> 2. The chip does not support the capability; <br> 3. A dependent service feature is not supported. |
| [32500001](../errorcode-deviceStatus.md#32500001-服务异常) | Service exception. |
| [32500002](../errorcode-deviceStatus.md#32500002-订阅失败) | Subscription failed. |
