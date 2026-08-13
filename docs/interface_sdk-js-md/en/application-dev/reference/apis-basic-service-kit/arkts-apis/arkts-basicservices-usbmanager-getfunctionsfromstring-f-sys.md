# getFunctionsFromString (System API)

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## getFunctionsFromString

```TypeScript
function getFunctionsFromString(funcs: string): int
```

Converts the USB function list in the string format to a numeric mask in Device mode.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function getFunctionsFromString(funcs: string): int--><!--Device-usbManager-function getFunctionsFromString(funcs: string): int-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| funcs | string | Yes | Function list in string format. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Function list in numeric mask format after conversion. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  &lt;br&gt;1.Mandatory parameters are left unspecified.  &lt;br&gt;2.Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. .<br>**Applicable version:** 18 and later |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Normal application do not have permission to use system api. |

