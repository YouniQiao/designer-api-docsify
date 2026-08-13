# getAccessoryList

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## getAccessoryList

```TypeScript
function getAccessoryList(): Array<Readonly<USBAccessory>>
```

Obtains the list of USB accessories connected to the host.

**Since:** 23

**Deprecated since:** -1

<!--Device-usbManager-function getAccessoryList(): Array<Readonly<USBAccessory>>--><!--Device-usbManager-function getAccessoryList(): Array<Readonly<USBAccessory>>-End-->

**System capability:** SystemCapability.USB.USBManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[Readonly](../../apis-na/arkts-apis/arkts-na-readonly-t.md)&lt;[USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-service-exception) |

## Examples

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
  hilog.info(0, 'testTag ui', `getAccessoryList success, accList: ${JSON.stringify(accList)}`)
} catch (error) {
  hilog.error(0, 'testTag ui', `getAccessoryList error ${error.code}, message is ${error.message}`)
}
```
