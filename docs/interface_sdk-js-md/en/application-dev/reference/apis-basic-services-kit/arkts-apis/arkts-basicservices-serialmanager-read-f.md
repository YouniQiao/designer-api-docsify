# read

## Modules to Import

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## read

```TypeScript
function read(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>
```

Reads data from the serial port device asynchronously. This API uses a promise to return the result.

**Since:** 19

**System capability:** SystemCapability.USB.USBManager.Serial

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [portId](arkts-basicservices-serialmanager-serialport-i.md) | number | Yes |
| buffer | Uint8Array | Yes |
| timeout | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [31400001](../errorcode-usb.md#31400001-serial-port-service-error) |
| [31400003](../errorcode-usb.md#31400003-port-number-not-exist) |
| [31400005](../errorcode-usb.md#31400005-device-not-opened) |
| [31400006](../errorcode-usb.md#31400006-data-transfer-timeout) |
| [31400007](../errorcode-usb.md#31400007-io-exception) |
