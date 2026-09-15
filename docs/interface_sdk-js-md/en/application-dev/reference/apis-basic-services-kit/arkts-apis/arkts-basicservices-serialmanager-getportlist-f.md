# getPortList

## Modules to Import

```TypeScript
import { serialManager } from '@kit.BasicServicesKit';
```

## getPortList

```TypeScript
function getPortList(): Readonly<SerialPort>[]
```

Obtains the serial port device list, including the device name and port number.

**Since:** 19

**System capability:** SystemCapability.USB.USBManager.Serial

**Return value:**

| Type | Description |
| --- | --- |
| Readonly&lt;[SerialPort](arkts-basicservices-serialmanager-serialport-i.md)&gt;[] | Serial port information list. |

**Examples**

```TypeScript
> NOTE
> 
> The following sample code shows the basic process for calling the getPortList API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.
```
