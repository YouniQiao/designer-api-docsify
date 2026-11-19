# offDropDetect

## 导入模块

```TypeScript
import { deviceStatus } from '@kit.MultimodalAwarenessKit';
```

## offDropDetect

```TypeScript
function offDropDetect(callback?: Callback<DropDetectionStatus>): void
```

取消订阅设备跌落检测事件。用于应用在退出页面或不再需要监听跌落事件的场景。调用后释放相关资源。若未调用onDropDetect()就调用offDropDetect()，该方法会抛出异常。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceStatus-function offDropDetect(callback?: Callback<DropDetectionStatus>): void--><!--Device-deviceStatus-function offDropDetect(callback?: Callback<DropDetectionStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DeviceStatus

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DropDetectionStatus](arkts-multimodalawareness-devicestatus-dropdetectionstatus-e.md)&gt; | 否 | 回调函数，返回设备跌落检测状态信息。需要取消监听的回调函数，需与订阅时传入的回调函数一致。<br> 若不填，则取消当前监听该事件的所有回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br> 1. The hardware does not support the capability; <br> 2. The chip does not support the capability; <br> 3. A dependent service feature is not supported. |
| [32500001](../errorcode-deviceStatus.md#32500001-服务异常) | Service exception. |
| [32500003](../errorcode-deviceStatus.md#32500003-取消订阅失败) | Unsubscription failed. |
