# on_deviceDisconnect

## Modules to Import

```TypeScript
import { continuationManager } from 'continuationManager';
```

## on_deviceDisconnect

```TypeScript
function on(type: 'deviceDisconnect', callback: Callback<string>): void
```

Subscribes to device disconnection events. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#ondevicestatechange)(type: 'deviceStateChange', callback: Callback&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt;)

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function on(type: 'deviceDisconnect', callback: Callback<string>): void--><!--Device-continuationManager-function on(type: 'deviceDisconnect', callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceDisconnect' | Yes | Event type. The value is fixed at **deviceDisconnect**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes | Callback invoked when a device is unselected from the device list provided by the device selection module. This callback returns the device ID. |

**Examples**

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

continuationManager.on("deviceDisconnect", (data) => {
  console.info('onDeviceDisconnect deviceId: ' + JSON.stringify(data));
});
```

