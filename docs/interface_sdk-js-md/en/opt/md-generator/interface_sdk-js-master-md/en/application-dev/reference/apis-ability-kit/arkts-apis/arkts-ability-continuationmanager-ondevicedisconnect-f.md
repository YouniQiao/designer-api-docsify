# on_deviceDisconnect

## Modules to Import

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
```

## on_deviceDisconnect

```TypeScript
function on(type: 'deviceDisconnect', callback: Callback<string>): void
```

Subscribes to device disconnection events. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#on_deviceStateChange)(type: 'deviceStateChange', callback: Callback&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt;)

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function on(type: 'deviceDisconnect', callback: Callback<string>): void--><!--Device-continuationManager-function on(type: 'deviceDisconnect', callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deviceDisconnect' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

continuationManager.on("deviceDisconnect", (data) => {
  console.info('onDeviceDisconnect deviceId: ' + JSON.stringify(data));
});
```
