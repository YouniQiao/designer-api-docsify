# queryDevices

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## queryDevices

```TypeScript
function queryDevices(busType?: number): Array<Readonly<Device>>
```

Queries the list of peripheral devices. If the device has no peripheral device connected, an empty list is returned.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| busType | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;Readonly & lt;Device & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [22900001](../errorcode-deviceManager.md#22900001-externaldevicemanager-service-exception-or-bustype-parameter-error) |
