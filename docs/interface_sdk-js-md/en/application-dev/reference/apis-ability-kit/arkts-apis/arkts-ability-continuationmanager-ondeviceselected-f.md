# on_deviceSelected

## Modules to Import

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
```

## on_deviceSelected

```TypeScript
function on(type: 'deviceSelected', token: number, callback: Callback<Array<ContinuationResult>>): void
```

Subscribes to device connection events. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 22

**Substitutes:** [on](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#ondevicestatechange)(type: 'deviceStateChange', callback: Callback&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt;)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-continuationManager-function on(type: 'deviceSelected', token: number, callback: Callback<Array<ContinuationResult>>): void--><!--Device-continuationManager-function on(type: 'deviceSelected', token: number, callback: Callback<Array<ContinuationResult>>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceSelected' | Yes | Event type. The value is fixed at **deviceSelected**. |
| token | number | Yes | Token obtained after the registration of the continuation management service. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;ContinuationResult&gt;&gt; | Yes | Callback invoked when a device is selected from the device list provided by the device selection module. This callback returns the device ID, type, and name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [16600004](../errorcode-DistributedSchedule.md#16600004-the-specified-callback-has-been-registered) | The specified callback has been registered. |
| [16600001](../errorcode-DistributedSchedule.md#16600001-the-system-ability-works-abnormally) | The system ability works abnormally. |
| [16600002](../errorcode-DistributedSchedule.md#16600002-the-specified-token-or-callback-is-not-registered) | The specified token or callback is not registered. |

**Examples**

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.on("deviceSelected", token, (data) => {
    console.info('onDeviceSelected len: ' + data.length);
    for (let i = 0; i < data.length; i++) {
      console.info('onDeviceSelected deviceId: ' + JSON.stringify(data[i].id));
      console.info('onDeviceSelected deviceType: ' + JSON.stringify(data[i].type));
      console.info('onDeviceSelected deviceName: ' + JSON.stringify(data[i].name));
    }
  });
} catch (err) {
  console.error('on failed, cause: ' + JSON.stringify(err));
}
```

