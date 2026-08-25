# open

## Modules to Import

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## open

```TypeScript
function open(portId: number): void
```

Opens a serial port device.

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
| [31400001](../errorcode-usb.md#31400001-serial-port-service-error) |
| [31400002](../errorcode-usb.md#31400002-no-serial-port-device-access-permission) |
| [31400003](../errorcode-usb.md#31400003-port-number-not-exist) |
| [31400004](../errorcode-usb.md#31400004-port-in-use) |
