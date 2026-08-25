# releaseDeviceManager

## Modules to Import

```TypeScript
import { distributedDeviceManager } from 'kits/@kit.DistributedServiceKit';
```

## releaseDeviceManager

```TypeScript
function releaseDeviceManager(deviceManager: DeviceManager): void
```

Releases a **DeviceManager** instance that is no longer used.

**Since:** 10

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceManager | [DeviceManager](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11600101](../errorcode-device-manager.md#11600101-service-invoking-exception) |
