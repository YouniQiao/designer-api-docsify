# readSync

## Modules to Import

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## readSync

```TypeScript
function readSync(portId: number, buffer: Uint8Array, timeout?: number): number
```

Reads data from the serial port device synchronously.

**Since:** 19

<!--Device-serialManager-function readSync(portId: int, buffer: Uint8Array, timeout?: int): int--><!--Device-serialManager-function readSync(portId: int, buffer: Uint8Array, timeout?: int): int-End-->

**System capability:** SystemCapability.USB.USBManager.Serial

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| portId | number | Yes |
| buffer | Uint8Array | Yes |
| timeout | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [31400007](../../apis-basic-services-kit/errorcode-usb.md#31400007-io-exception) |
| [31400006](../../apis-basic-services-kit/errorcode-usb.md#31400006-data-transfer-timeout) |
| [31400005](../../apis-basic-services-kit/errorcode-usb.md#31400005-device-not-opened) |
| [31400003](../../apis-basic-services-kit/errorcode-usb.md#31400003-port-number-not-exist) |
| [31400001](../../apis-basic-services-kit/errorcode-usb.md#31400001-serial-port-service-error) |

## Examples

The following sample code shows the basic process for calling the readSync API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

```TypeScript
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function readSync() {
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

  // Read data synchronously.
  let readSyncBuffer: Uint8Array = new Uint8Array(64);
  try {
    serialManager.readSync(portId, readSyncBuffer, 2000);
    console.info('readSync usbSerial success, readSyncBuffer: ' + readSyncBuffer.toString());
  } catch (error) {
    console.error('readSync usbSerial error, ' + JSON.stringify(error));
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
