# getStringFromFunctions (System API)

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## getStringFromFunctions

```TypeScript
function getStringFromFunctions(funcs: FunctionType): string
```

在设备模式下，将数字掩码形式的USB功能列表转化为字符串。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function getStringFromFunctions(funcs: FunctionType): string--><!--Device-usbManager-function getStringFromFunctions(funcs: FunctionType): string-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| funcs | [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) | Yes | 功能列表对应的数字掩码。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 转化后的字符串形式的功能列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes:  &lt;br&gt;1.Mandatory parameters are left unspecified.  &lt;br&gt;2.Incorrect parameter types. |
| 801 | Capability not supported.<br>**Applicable version:** 18 and later |
| 201 | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 18 and later |
| 202 | Permission denied. Normal application do not have permission to use system api. |


## getStringFromFunctions

```TypeScript
function getStringFromFunctions(funcs: int): string
```

Converts the numeric mask combination of a given USB function list to a string descriptor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function getStringFromFunctions(funcs: int): string--><!--Device-usbManager-function getStringFromFunctions(funcs: int): string-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| funcs | int | Yes | numeric mask combination of the function list. |

**Return value:**

| Type | Description |
| --- | --- |
| string | descriptor of the supported function list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Permission denied. Normal application do not have permission to use system api. |

