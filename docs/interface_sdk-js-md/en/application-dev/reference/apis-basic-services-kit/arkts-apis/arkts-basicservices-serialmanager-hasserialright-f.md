# hasSerialRight

## Modules to Import

```TypeScript
import { serialManager } from '@kit.BasicServicesKit';
```

## hasSerialRight

```TypeScript
function hasSerialRight(portId: int): boolean
```

Checks whether the application has the permission to access the serial port device. When an application is restarted after exits, you need to request the permission from the user again.

**Since:** 23

<!--Device-serialManager-function hasSerialRight(portId: int): boolean--><!--Device-serialManager-function hasSerialRight(portId: int): boolean-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| portId | int | Yes | Port number of the target device, which is obtained from the serial port parameter SerialPort returned by [getPortList](arkts-basicservices-serialmanager-getportlist-f.md). |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The value **true** indicates that the permission is authorized, and **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |  |
| [31400003](../errorcode-usb.md#31400003-port-number-not-exist) |  |
| [14400005](../errorcode-usb.md#14400005-database-operation-exception) |  |
| [31400001](../errorcode-usb.md#31400001-serial-port-service-error) |  |

**Examples**

The following sample code shows the basic process for calling the hasSerialRight API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

```TypeScript
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function hasSerialRight() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('portList: ', JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // Check whether the device can be accessed by the application.
  if (serialManager.hasSerialRight(portId)) {
    console.info('The serial port is accessible');
  } else {
    console.info('No permission to access the serial port');
  }
}
```

