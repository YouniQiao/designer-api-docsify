# updateConnectStatus

## Modules to Import

```TypeScript
import { continuationManager } from 'kits/@kit.AbilityKit';
```

## updateConnectStatus

```TypeScript
function updateConnectStatus(
    token: number,
    deviceId: string,
    status: DeviceConnectState,
    callback: AsyncCallback<void>
  ): void
```

Instructs the device selection module to update the device connection state. This API uses an asynchronous callback  to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function updateConnectStatus(    token: number,    deviceId: string,    status: DeviceConnectState,    callback: AsyncCallback<void>  ): void--><!--Device-continuationManager-function updateConnectStatus(    token: number,    deviceId: string,    status: DeviceConnectState,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | number | Yes |
| deviceId | string | Yes |
| status | [DeviceConnectState](arkts-ability-continuationmanager-deviceconnectstate-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
let deviceId: string = "test deviceId";
continuationManager.updateConnectStatus(token, deviceId, continuationManager.DeviceConnectState.CONNECTED, (err) => {
  if (err.code != 0) {
    console.error('updateConnectStatus failed, cause: ' + JSON.stringify(err));
    return;
  }
  console.info('updateConnectStatus finished. ');
});
```


## updateConnectStatus

```TypeScript
function updateConnectStatus(token: number, deviceId: string, status: DeviceConnectState): Promise<void>
```

Instructs the device selection module to update the device connection state. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function updateConnectStatus(token: number, deviceId: string, status: DeviceConnectState): Promise<void>--><!--Device-continuationManager-function updateConnectStatus(token: number, deviceId: string, status: DeviceConnectState): Promise<void>-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | number | Yes |
| deviceId | string | Yes |
| status | [DeviceConnectState](arkts-ability-continuationmanager-deviceconnectstate-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = 1;
let deviceId: string = "test deviceId";
continuationManager.updateConnectStatus(token, deviceId, continuationManager.DeviceConnectState.CONNECTED)
  .then(() => {
    console.info('updateConnectStatus finished. ');
  })
  .catch((err: BusinessError) => {
    console.error('updateConnectStatus failed, cause: ' + JSON.stringify(err));
});
```
