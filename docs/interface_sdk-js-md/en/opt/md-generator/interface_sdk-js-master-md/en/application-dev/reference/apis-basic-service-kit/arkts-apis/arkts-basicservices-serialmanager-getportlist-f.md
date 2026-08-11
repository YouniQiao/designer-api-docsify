# getPortList

## Modules to Import

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## getPortList

```TypeScript
function getPortList(): Readonly<SerialPort>[]
```

Obtains the serial port device list, including the device name and port number.

**Since:** 19

<!--Device-serialManager-function getPortList(): Readonly<SerialPort>[]--><!--Device-serialManager-function getPortList(): Readonly<SerialPort>[]-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Readonly](../../apis-default/arkts-apis/arkts-readonly-t.md)&lt;SerialPort&gt;[] |

## Examples

The following sample code shows the basic process for calling the getPortList API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

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
