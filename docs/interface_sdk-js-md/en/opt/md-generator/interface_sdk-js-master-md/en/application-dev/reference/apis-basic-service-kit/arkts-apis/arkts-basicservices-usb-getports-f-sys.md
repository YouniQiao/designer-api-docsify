# getPorts (System API)

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## getPorts

```TypeScript
function getPorts(): Array<USBPort>
```

Obtains the list of all physical USB ports.

**Since:** 9

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.getPorts](arkts-basicservices-usbmanager-getports-f-sys.md#getports)

<!--Device-usb-function getPorts(): Array<USBPort>--><!--Device-usb-function getPorts(): Array<USBPort>-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;USBPort&gt; |

## Examples

```TypeScript
let ret = usb.getPorts();
```
