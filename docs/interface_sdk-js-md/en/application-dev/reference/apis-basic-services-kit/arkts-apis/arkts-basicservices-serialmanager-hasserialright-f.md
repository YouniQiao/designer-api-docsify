# hasSerialRight

## Modules to Import

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## hasSerialRight

```TypeScript
function hasSerialRight(portId: number): boolean
```

Checks whether the application has the permission to access the serial port device. When an application is restarted after exits, you need to request the permission from the user again.

**Since:** 19

**System capability:** SystemCapability.USB.USBManager.Serial

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [portId](arkts-basicservices-serialmanager-serialport-i.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14400005](../errorcode-usb.md#14400005-database-operation-exception) |
| [31400001](../errorcode-usb.md#31400001-serial-port-service-error) |
| [31400003](../errorcode-usb.md#31400003-port-number-not-exist) |
