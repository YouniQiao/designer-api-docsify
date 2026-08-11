# getDeviceFunctions (System API)

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## getDeviceFunctions

```TypeScript
function getDeviceFunctions(): FunctionType
```

Obtains the numeric mask combination for the USB function list in Device mode. When the developer mode is disabled,  
 **undefined** may be returned if no device is connected. Check whether the return value of the API is empty.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function getDeviceFunctions(): FunctionType--><!--Device-usbManager-function getDeviceFunctions(): FunctionType-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) | Numeric mask combination for the USB function list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.<br>**Applicable version:** 18 and later |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 18 and later |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Normal application do not have permission to use system api. |


## getDeviceFunctions

```TypeScript
function getDeviceFunctions(): int
```

Obtains the numeric mask combination for the current USB function list in Device mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function getDeviceFunctions(): int--><!--Device-usbManager-function getDeviceFunctions(): int-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| int | the numeric mask combination for the current USB function list in FunctionType. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Normal application do not have permission to use system api. |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-service-exception) | Service exception. Possible causes: &lt;br&gt;1. No accessory is plugged in. |

