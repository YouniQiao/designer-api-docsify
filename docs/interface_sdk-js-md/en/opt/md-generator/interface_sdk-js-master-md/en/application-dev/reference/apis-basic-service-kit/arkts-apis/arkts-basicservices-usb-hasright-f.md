# hasRight

## Modules to Import

```TypeScript
import { usb } from '@kit.BasicServicesKit';
```

## hasRight

```TypeScript
function hasRight(deviceName: string): boolean
```

Checks whether the application has the permission to access the device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [hasRight](arkts-basicservices-usbmanager-hasright-f.md#hasRight)

<!--Device-usb-function hasRight(deviceName: string): boolean--><!--Device-usb-function hasRight(deviceName: string): boolean-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let devicesName= "1-1";
let bool = usb.hasRight(devicesName);
console.info(`hasRight = ${bool}`);
```
