# off_deviceConnect

## Modules to Import

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
```

## off_deviceConnect

```TypeScript
function off(type: 'deviceConnect', callback?: Callback<ContinuationResult>): void
```

Unsubscribes from device connection events. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [off](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#off_deviceStateChange)(type: 'deviceStateChange', callback?: Callback&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt;)

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function off(type: 'deviceConnect', callback?: Callback<ContinuationResult>): void--><!--Device-continuationManager-function off(type: 'deviceConnect', callback?: Callback<ContinuationResult>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceConnect' | Yes | Event type. The value is fixed at **deviceConnect**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ContinuationResult&gt; | No | Callback invoked when a device is selected from the device list provided by the device selection module. This callback returns the device ID, type, and name. |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

continuationManager.off("deviceConnect", (data) => {
  console.info('onDeviceConnect deviceId: ' + JSON.stringify(data.id));
  console.info('onDeviceConnect deviceType: ' + JSON.stringify(data.type));
  console.info('onDeviceConnect deviceName: ' + JSON.stringify(data.name));
});
```

