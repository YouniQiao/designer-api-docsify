# readSync

## Modules to Import

```TypeScript
import { serialManager } from '@kit.BasicServicesKit';
```

## readSync

```TypeScript
function readSync(portId: number, buffer: Uint8Array, timeout?: number): number
```

Reads data from the serial port device synchronously.

**Since:** 19

**System capability:** SystemCapability.USB.USBManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| portId | number | Yes | Port number of the target device, which is obtained from the serial port parameter SerialPort returned by [getPortList](arkts-basicservices-serialmanager-getportlist-f.md). |
| buffer | Uint8Array | Yes | Buffer for reading data, with a maximum length of 8192 bytes. |
| timeout | number | No | Timeout interval.Unit: milliseconds. If the API has no data in the buffer of the target port, it returns the result after waiting for the specified time. The default value **0** indicates that the API returns the result without waiting. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Length of the data read. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |  |
| [31400001](../errorcode-usb.md#31400001-serial-port-service-error) |  |
| [31400003](../errorcode-usb.md#31400003-port-number-not-exist) |  |
| [31400005](../errorcode-usb.md#31400005-device-not-opened) |  |
| [31400006](../errorcode-usb.md#31400006-data-transfer-timeout) |  |
| [31400007](../errorcode-usb.md#31400007-io-exception) |  |

**Examples**

```TypeScript
> NOTE
> 
> The following sample code shows the basic process for calling the readSync API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.
```
