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
| Readonly&lt;SerialPort&gt;[] | Serial port information list. |

**Examples**

> NOTE

```TypeScript
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port device list.
function getPortList() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (!portList || portList.length === 0) {
    console.error('usbSerial portList is empty');
    return;
  }
}
```
