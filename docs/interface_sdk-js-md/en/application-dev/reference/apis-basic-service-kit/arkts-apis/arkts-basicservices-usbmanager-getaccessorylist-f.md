# getAccessoryList

## Modules to Import

```TypeScript
import { usbManager } from 'usbManager';
```

## getAccessoryList

```TypeScript
function getAccessoryList(): Array<Readonly<USBAccessory>>
```

Obtains the list of USB accessories connected to the host.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-usbManager-function getAccessoryList(): Array<Readonly<USBAccessory>>--><!--Device-usbManager-function getAccessoryList(): Array<Readonly<USBAccessory>>-End-->

**System capability:** SystemCapability.USB.USBManager

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[Readonly](../../apis-na/arkts-apis/arkts-na-readonly-t.md)&lt;[USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md)&gt;&gt; | List of USB accessories (read-only). Currently, only one USB accessory is contained in the list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-service-exception) | Service exception. Possible causes:  <br>1. No accessory is plugged in. |

## Examples

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
  hilog.info(0, 'testTag ui', `getAccessoryList success, accList: ${JSON.stringify(accList)}`)
} catch (error) {
  hilog.info(0, 'testTag ui', `getAccessoryList error ${error.code}, message is ${error.message}`)
}
```

