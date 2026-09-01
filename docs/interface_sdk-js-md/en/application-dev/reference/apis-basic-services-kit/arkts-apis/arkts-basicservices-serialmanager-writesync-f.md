# writeSync

## Modules to Import

```TypeScript
import { serialManager } from '@kit.BasicServicesKit';
```

## writeSync

```TypeScript
function writeSync(portId: number, buffer: Uint8Array, timeout?: number): number
```

Writes data to the serial port device synchronously. The length of data written each time cannot exceed 4 KB; otherwise, data loss may occur. You are advised to write number data in multiple packets.

**Since:** 19

**System capability:** SystemCapability.USB.USBManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| portId | number | Yes | Port number of the target device, which is obtained from the serial port parameter SerialPort returned by [getPortList](arkts-basicservices-serialmanager-getportlist-f.md). |
| buffer | Uint8Array | Yes | Destination buffer for writing data, with a maximum length of 4 KB. |
| timeout | number | No | Timeout interval.Unit: milliseconds. Whether the buffer of the target port is writable within the specified time. If yes, the API is processed properly; otherwise, a timeout message is returned after the specified time. The default value **0** indicates that the API returns the result immediately when the target port is not writable. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Length of the data written. |

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

> NOTE

```TypeScript
import { JSON } from '@kit.ArkTS';
import { buffer } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function writeSync() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (!portList || portList.length === 0) {
    console.error('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // Check whether the device can be accessed by the application.
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // If the application does not have the access permission and the user does not grant the permission, the application exits.
        console.error('user is not granted the operation permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // Open a serial port device.
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
  }

  // Write data synchronously.
  let writeSyncBuffer: Uint8Array = new Uint8Array(buffer.from('Hello World', 'utf-8').buffer)
  try {
    serialManager.writeSync(portId, writeSyncBuffer, 2000);
    console.info('writeSync usbSerial success, writeSyncBuffer: ' + writeSyncBuffer.toString());
  } catch (error) {
    console.error('writeSync usbSerial error, ' + JSON.stringify(error));
  }
  
  // Close the serial port device.
  try {
    serialManager.close(portId);
    console.info('close usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('close usbSerial error, ' + JSON.stringify(error));
  }
}
```
