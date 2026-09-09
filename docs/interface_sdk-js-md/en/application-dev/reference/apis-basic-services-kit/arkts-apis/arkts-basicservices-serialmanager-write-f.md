# write

## Modules to Import

```TypeScript
import { serialManager } from '@kit.BasicServicesKit';
```

## write

```TypeScript
function write(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>
```

Writes data to the serial port device asynchronously. The length of data written each time cannot exceed 4 KB; otherwise, data loss may occur. You are advised to write long data in multiple packets. This API uses a promise to return the result.

**Since:** 19

**System capability:** SystemCapability.USB.USBManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| portId | number | Yes | Port number of the target device, which is obtained from the serial port parameter SerialPort returned by [getPortList](arkts-basicservices-serialmanager-getportlist-f.md). |
| buffer | Uint8Array | Yes | Buffer for writing data, with a maximum length of 4 KB. |
| timeout | number | No | Timeout interval.Unit: milliseconds. Whether the buffer of the target port is writable within the specified time. If yes, the API is processed properly; otherwise, a timeout message is returned after the specified time. The default value **0** indicates that the API returns the result immediately when the target port is not writable. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the length of the data written. |

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
> 
> The following sample code shows the basic process for calling the write API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

```TypeScript
import { JSON } from '@kit.ArkTS';
import { buffer } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the serial port list.
async function writeExample() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (!portList || portList.length === 0) {
    console.error('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // Check whether the device can be accessed by the application.
  if (!serialManager.hasSerialRight(portId)) {
    let result = await serialManager.requestSerialRight(portId);
    if (!result) {
      // If the app does not have the access permission and the user does not grant the permission, the app exits.
      console.error('user is not granted the operation permission');
      return;
    } else {
      console.info('grant permission successfully');
    }
  }

  // Open a serial port device.
  try {
    serialManager.open(portId);
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed to open usbSerial. Code: ${err.code}, message: ${err.message}`);
  }

  // Write data asynchronously.
  try {
    let writeBuffer: Uint8Array = new Uint8Array(buffer.from('Hello World', 'utf-8').buffer);
    let size: number = await serialManager.write(portId, writeBuffer, 2000);
    if (size > 0) {
      console.info('write usbSerial success, writeBuffer: ' + writeBuffer.toString());
    }
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed to write usbSerial. Code: ${err.code}, message: ${err.message}`);
  }

  // Close the serial port device.
  try {
    serialManager.close(portId);
    console.info('close usbSerial success, portId: ' + portId);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed to close usbSerial. Code: ${err.code}, message: ${err.message}`);
  }
}
```
