# getDeviceFunctions (System API)

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
import { serialManager } from '@kit.BasicServicesKit';
```

## getDeviceFunctions

```TypeScript
function getDeviceFunctions(): FunctionType
```

Obtains the numeric mask combination for the USB function list in Device mode. When the developer mode is disabled, **undefined** may be returned if no device is connected. Check whether the return value of the API is empty.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function getDeviceFunctions(): FunctionType--><!--Device-usbManager-function getDeviceFunctions(): FunctionType-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| FunctionType | Numeric mask combination for the USB function list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 18 and later |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Normal application do not have permission to use system api. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |

**Examples**

```TypeScript
let ret: number = usbManager.getDeviceFunctions();
```


## getDeviceFunctions

```TypeScript
function getDeviceFunctions(): int
```

Obtains the numeric mask combination for the current USB function list in Device mode.

**Since:** 23

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Normal application do not have permission to use system api. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) |  |
| [14400004](../errorcode-usb.md#14400004-service-exception) |  |

**Examples**

See [getDeviceFunctions](#getdevicefunctions)

