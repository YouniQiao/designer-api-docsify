# cancelSerialRight

## Modules to Import

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## cancelSerialRight

```TypeScript
function cancelSerialRight(portId: number): void
```

Cancels the permission to access the serial port device when the application is running. This API is used to close the enabled serial port device.

**Since:** 19

**System capability:** SystemCapability.USB.USBManager.Serial

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [portId](arkts-basicservices-serialmanager-serialport-i.md) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14400005](../errorcode-usb.md#14400005-database-operation-exception) |
| [31400001](../errorcode-usb.md#31400001-serial-port-service-error) |
| [31400002](../errorcode-usb.md#31400002-no-serial-port-device-access-permission) |
| [31400003](../errorcode-usb.md#31400003-port-number-not-exist) |
