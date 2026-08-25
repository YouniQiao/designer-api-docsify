# addSerialRight (System API)

## Modules to Import

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## addSerialRight

```TypeScript
function addSerialRight(tokenId: number, portId: number): void
```

Adds the permission to an application for accessing the serial port device. serialManager.requestSerialRight triggers a dialog box to request user authorization. addSerialRight does not trigger a dialog box but directly adds the device access permission for the application. After the application exits, the access permission on the serial port device is automatically removed. After the application is restarted, you need to request the permission again.

**Since:** 19

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

**System capability:** SystemCapability.USB.USBManager.Serial

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenId | number | Yes |
| [portId](arkts-basicservices-serialmanager-serialport-i.md) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14400005](../errorcode-usb.md#14400005-database-operation-exception) |
| [31400001](../errorcode-usb.md#31400001-serial-port-service-error) |
| [31400003](../errorcode-usb.md#31400003-port-number-not-exist) |
