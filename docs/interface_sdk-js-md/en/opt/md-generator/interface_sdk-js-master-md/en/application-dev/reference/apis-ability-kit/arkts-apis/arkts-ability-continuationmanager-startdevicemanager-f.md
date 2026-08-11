# startDeviceManager

## Modules to Import

```TypeScript
import { continuationManager } from 'kits/@kit.AbilityKit';
```

## startDeviceManager

```TypeScript
function startDeviceManager(token: number, callback: AsyncCallback<void>): void
```

Starts the device selection module to show the list of available devices on the network. This API does not involve any filter parameters and uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.startDiscovering](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#startdiscovering)(discoverParam:

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function startDeviceManager(token: number, callback: AsyncCallback<void>): void--><!--Device-continuationManager-function startDeviceManager(token: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
continuationManager.startDeviceManager(token, (err) => {
  if (err.code != 0) {
    console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
    return;
  }
  console.info('startDeviceManager finished. ');
});
```


## startDeviceManager

```TypeScript
function startDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void
```

Starts the device selection module to show the list of available devices on the network. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.startDiscovering](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#startdiscovering)(discoverParam:

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function startDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void--><!--Device-continuationManager-function startDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | number | Yes |
| options | [ContinuationExtraParams](arkts-ability-continuationextraparams-continuationextraparams-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
continuationManager.startDeviceManager(
  token,
  {
    deviceType: ["00E"]
  },
  (err) => {
    if (err.code != 0) {
      console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('startDeviceManager finished. ');
});
```


## startDeviceManager

```TypeScript
function startDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>
```

Starts the device selection module to show the list of available devices on the network. This API uses a promise to  return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.startDiscovering](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#startdiscovering)(discoverParam:

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function startDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>--><!--Device-continuationManager-function startDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | number | Yes |
| options | [ContinuationExtraParams](arkts-ability-continuationextraparams-continuationextraparams-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
continuationManager.startDeviceManager(
  token,
  {
    deviceType: ["00E"]
  }).then(() => {
    console.info('startDeviceManager finished. ');
  }).catch((err: BusinessError) => {
    console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
});
```
