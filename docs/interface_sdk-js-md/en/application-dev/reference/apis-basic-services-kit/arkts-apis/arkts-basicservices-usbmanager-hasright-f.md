# hasRight

## Modules to Import

```TypeScript
import usbManager from '@kit.BasicServicesKit';
import serialManager from '@kit.BasicServicesKit.serial';
```

## hasRight

```TypeScript
function hasRight(deviceName: string): boolean
```

Checks whether the application has the permission to access the device. Checks whether the user, for example, the application or system, has the device access permissions. The value ** true** is returned if the user has the device access permissions; the value **false** is returned otherwise.

**Since:** 9

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceName | string | Yes | Device name, which is name of USBDevice, obtained from the device list returned by [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md). |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the application has the permission to access the device; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified.  2.Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |

**Examples**

```TypeScript
function hasRight(): boolean {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return false;
  }

  let device: usbManager.USBDevice = devicesList?.[0];
  usbManager.requestRight(device.name);
  let right: boolean = usbManager.hasRight(device.name);
  console.info(`${right}`);
  return right;
}
```
