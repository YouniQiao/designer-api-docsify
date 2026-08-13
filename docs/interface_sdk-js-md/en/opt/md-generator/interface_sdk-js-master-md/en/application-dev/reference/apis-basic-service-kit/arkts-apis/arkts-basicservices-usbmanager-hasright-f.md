# hasRight

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## hasRight

```TypeScript
function hasRight(deviceName: string): boolean
```

Checks whether the application has the permission to access the device. Checks whether the user, for example, the application or system, has the device access permissions. The value ** true** is returned if the user has the device access permissions; the value **false** is returned otherwise.

**Since:** 23

**Deprecated since:** -1

<!--Device-usbManager-function hasRight(deviceName: string): boolean--><!--Device-usbManager-function hasRight(deviceName: string): boolean-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## Examples

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
