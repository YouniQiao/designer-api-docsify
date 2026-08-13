# on_deviceDisconnect

## on_deviceDisconnect

```TypeScript
function on(type: 'deviceDisconnect', callback: Callback<string>): void
```

异步方法，监听设备断开状态，使用Callback形式返回断开的设备信息。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [on](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#on_deviceStateChange)(type: 'deviceStateChange', callback: Callback&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-continuationManager-function on(type: 'deviceDisconnect', callback: Callback<string>): void--><!--Device-continuationManager-function on(type: 'deviceDisconnect', callback: Callback<string>): void-End-->

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceDisconnect' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 是 |

## 示例

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

continuationManager.on("deviceDisconnect", (data) => {
  console.info('onDeviceDisconnect deviceId: ' + JSON.stringify(data));
});
```
