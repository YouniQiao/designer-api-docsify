# requestRight

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## requestRight

```TypeScript
function requestRight(deviceName: string): Promise<boolean>
```

Requests the temporary permission for the application to access a USB device. This API uses a promise to return the result. System applications are granted the device access permission by default, and you do not need to apply for the permission separately.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md#requestright)

<!--Device-usb-function requestRight(deviceName: string): Promise<boolean>--><!--Device-usb-function requestRight(deviceName: string): Promise<boolean>-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
let devicesName= "1-1";
usb.requestRight(devicesName).then((ret) => {
  console.info(`requestRight = ${ret}`);
});
```
