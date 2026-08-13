# releaseDeviceManager

## Modules to Import

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
```

## releaseDeviceManager

```TypeScript
function releaseDeviceManager(deviceManager: DeviceManager): void
```

Releases a **DeviceManager** instance that is no longer used.

**Since:** 23

**Deprecated since:** -1

<!--Device-distributedDeviceManager-function releaseDeviceManager(deviceManager: DeviceManager): void--><!--Device-distributedDeviceManager-function releaseDeviceManager(deviceManager: DeviceManager): void-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceManager | [DeviceManager](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11600101](../../apis-distributedservice-kit/errorcode-device-manager.md#11600101-service-invoking-exception) |

## Examples

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  distributedDeviceManager.releaseDeviceManager(dmInstance);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('release device manager errCode:' + e.code + ',errMessage:' + e.message);
}
```
