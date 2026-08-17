# getPortList (System API)

## Modules to Import

```TypeScript
import { usbManager } from 'usbManager';
```

## getPortList

```TypeScript
function getPortList(): Array<USBPort>
```

Obtains the list of all physical USB ports. When the developer mode is disabled, **undefined** may be returned if no device is connected. Check whether the return value of the API is empty.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function getPortList(): Array<USBPort>--><!--Device-usbManager-function getPortList(): Array<USBPort>-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;USBPort&gt; | List of physical USB ports. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 18 and later |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Normal application do not have permission to use system api. |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-service-exception) | Service exception. Possible causes:  <br>1. No accessory is plugged in.<br>**Applicable version:** 23 and later |

