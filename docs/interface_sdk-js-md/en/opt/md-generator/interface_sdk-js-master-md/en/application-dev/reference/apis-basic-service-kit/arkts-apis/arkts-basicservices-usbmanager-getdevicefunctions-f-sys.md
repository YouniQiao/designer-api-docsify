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

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function getDeviceFunctions(): FunctionType--><!--Device-usbManager-function getDeviceFunctions(): FunctionType-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
