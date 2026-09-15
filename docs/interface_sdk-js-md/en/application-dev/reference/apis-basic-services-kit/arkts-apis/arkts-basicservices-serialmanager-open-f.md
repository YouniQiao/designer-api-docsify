# open

## Modules to Import

```TypeScript
import { serialManager } from '@kit.BasicServicesKit';
```

## open

```TypeScript
function open(portId: number): void
```

Opens a serial port device.

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
| [31400002](../errorcode-usb.md#31400002-no-serial-port-device-access-permission) |  |
| [31400003](../errorcode-usb.md#31400003-port-number-not-exist) |  |
| [31400004](../errorcode-usb.md#31400004-port-in-use) |  |

**Examples**

```TypeScript
> NOTE
> 
> The following sample code shows the basic process for calling the open API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.
```
