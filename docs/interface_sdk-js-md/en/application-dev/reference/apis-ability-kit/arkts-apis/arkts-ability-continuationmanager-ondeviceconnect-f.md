# on_deviceConnect

## Modules to Import

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
```

## on_deviceConnect('deviceConnect')

```TypeScript
function on(type: 'deviceConnect', callback: Callback<ContinuationResult>): void
```

Subscribes to device connection events. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#on_devicestatechangedevicestatechange)(type: 'deviceStateChange', callback: Callback&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt;)

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function on(type: 'deviceConnect', callback: Callback<ContinuationResult>): void--><!--Device-continuationManager-function on(type: 'deviceConnect', callback: Callback<ContinuationResult>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceConnect' | Yes | Event type. The value is fixed at **deviceConnect**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;ContinuationResult&gt; | Yes | Callback invoked when a device is selected from the device list provided by the device selection module. This callback returns the device ID, type, and name. |

**Examples**

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

continuationManager.on("deviceConnect", (data) => {
  console.info('onDeviceConnect deviceId: ' + JSON.stringify(data.id));
  console.info('onDeviceConnect deviceType: ' + JSON.stringify(data.type));
  console.info('onDeviceConnect deviceName: ' + JSON.stringify(data.name));
});
```

