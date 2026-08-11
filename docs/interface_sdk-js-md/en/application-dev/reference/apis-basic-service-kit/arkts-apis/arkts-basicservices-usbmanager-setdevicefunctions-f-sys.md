# setDeviceFunctions (System API)

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## setDeviceFunctions

```TypeScript
function setDeviceFunctions(funcs: FunctionType): Promise<void>
```

Sets the current USB function list in Device mode. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function setDeviceFunctions(funcs: FunctionType): Promise<void>--><!--Device-usbManager-function setDeviceFunctions(funcs: FunctionType): Promise<void>-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| funcs | [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) | Yes | USB function list in numeric mask format. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:  &lt;br&gt;1.Mandatory parameters are left unspecified.  &lt;br&gt;2.Incorrect parameter types. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.<br>**Applicable version:** 18 and later |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 18 and later |
| [14400002](../../apis-basic-services-kit/errorcode-usb.md#14400002-hdc-disabled) | Permission denied. The HDC is disabled by the system. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Normal application do not have permission to use system api. |
| [14400006](../../apis-basic-services-kit/errorcode-usb.md#14400006-usb-device-function-unsupported) | Unsupported operation. The function is not supported. |


## setDeviceFunctions

```TypeScript
function setDeviceFunctions(funcs: int): Promise<void>
```

Sets the current USB function list in Device mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function setDeviceFunctions(funcs: int): Promise<void>--><!--Device-usbManager-function setDeviceFunctions(funcs: int): Promise<void>-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| funcs | int | Yes | numeric mask combination of the supported function list. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [14400002](../../apis-basic-services-kit/errorcode-usb.md#14400002-hdc-disabled) | Permission denied. The HDC is disabled by the system. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Normal application do not have permission to use system api. |
| [14400006](../../apis-basic-services-kit/errorcode-usb.md#14400006-usb-device-function-unsupported) | Unsupported operation. The function is not supported. |

