# close

## Modules to Import

```TypeScript
import { serialManager } from '@kit.BasicServicesKit';
```

## close

```TypeScript
function close(portId: number): void
```

Closes the serial port device.

**Since:** 19

**System capability:** SystemCapability.USB.USBManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| portId | number | Yes | Port number of the target device, which is obtained from the serial port parameter SerialPort returned by [getPortList](arkts-basicservices-serialmanager-getportlist-f.md). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |  |
| [31400001](../errorcode-usb.md#31400001-serial-port-service-error) |  |
| [31400003](../errorcode-usb.md#31400003-port-number-not-exist) |  |
| [31400005](../errorcode-usb.md#31400005-device-not-opened) |  |

**Examples**

```TypeScript
> NOTE
> 
> The following sample code shows the basic process for calling the close API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.
```
