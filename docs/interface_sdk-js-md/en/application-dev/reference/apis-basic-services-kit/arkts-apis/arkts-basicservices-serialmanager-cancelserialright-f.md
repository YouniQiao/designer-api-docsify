# cancelSerialRight

## Modules to Import

```TypeScript
import { serialManager } from '@kit.BasicServicesKit';
```

## cancelSerialRight

```TypeScript
function cancelSerialRight(portId: number): void
```

Cancels the permission to access the serial port device when the application is running. This API is used to close the enabled serial port device.

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
| [14400005](../errorcode-usb.md#14400005-database-operation-exception) |  |
| [31400001](../errorcode-usb.md#31400001-serial-port-service-error) |  |
| [31400002](../errorcode-usb.md#31400002-no-serial-port-device-access-permission) |  |
| [31400003](../errorcode-usb.md#31400003-port-number-not-exist) |  |

**Examples**

```TypeScript
> NOTE
> 
> The following sample code shows the basic process for calling the cancelSerialRight API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.
```
