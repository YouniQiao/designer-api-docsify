# off_deviceDisconnect

## Modules to Import

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
```

## off('deviceDisconnect')

```TypeScript
function off(type: 'deviceDisconnect', callback?: Callback<string>): void
```

Unsubscribes from device disconnection events. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#offdevicestatechange)(type: 'deviceStateChange', callback?: Callback&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt;)

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function off(type: 'deviceDisconnect', callback?: Callback<string>): void--><!--Device-continuationManager-function off(type: 'deviceDisconnect', callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceDisconnect' | Yes | Event type. The value is fixed at **deviceDisconnect**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No | Callback invoked when a device is unselected from the device list provided by the device selection module. This callback returns the device ID. |

**Examples**

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

continuationManager.off("deviceDisconnect", (data) => {
  console.info('onDeviceDisconnect deviceId: ' + JSON.stringify(data));
});
```

