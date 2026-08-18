# read

## Modules to Import

```TypeScript
import { serialManager } from '@kit.BasicServicesKit';
```

## read

```TypeScript
function read(portId: int, buffer: Uint8Array, timeout?: int): Promise<int>
```

Reads data from the serial port device asynchronously. This API uses a promise to return the result.

**Since:** 23

<!--Device-serialManager-function read(portId: int, buffer: Uint8Array, timeout?: int): Promise<int>--><!--Device-serialManager-function read(portId: int, buffer: Uint8Array, timeout?: int): Promise<int>-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| portId | int | Yes | Port number of the target device, which is obtained from the serial port parameter SerialPort returned by [getPortList](arkts-basicservices-serialmanager-getportlist-f.md). |
| buffer | Uint8Array | Yes | Buffer for reading data, with a maximum length of 8192 bytes. |
| timeout | int | No | Timeout interval.Unit: milliseconds. If the API has no data in the buffer of the target port, it returns the result after waiting for the specified time. The default value **0** indicates that the API returns the result without waiting. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the length of the data read. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |  |
| [31400007](../errorcode-usb.md#31400007-io-exception) |  |
| [31400006](../errorcode-usb.md#31400006-data-transfer-timeout) |  |
| [31400005](../errorcode-usb.md#31400005-device-not-opened) |  |
| [31400003](../errorcode-usb.md#31400003-port-number-not-exist) |  |
| [31400001](../errorcode-usb.md#31400001-serial-port-service-error) |  |

**Examples**

The following sample code shows the basic process for calling the read API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

```TypeScript
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function read() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // Check whether the device can be accessed by the application.
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // If the application does not have the access permission and is not granted by the user, the application exits.
        console.info('user is not granted the operation  permission');
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

  // Read data asynchronously.
  let readBuffer: Uint8Array = new Uint8Array(64);
  serialManager.read(portId, readBuffer, 2000).then((size: number) => {
    console.info('read usbSerial success, readBuffer: ' + readBuffer.toString());
  }).catch((error: Error) => {
    console.error('read usbSerial error, ' + JSON.stringify(error));
  })
}
```

