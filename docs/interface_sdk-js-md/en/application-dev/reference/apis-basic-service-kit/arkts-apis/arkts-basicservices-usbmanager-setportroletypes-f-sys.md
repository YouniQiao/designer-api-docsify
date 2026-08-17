# setPortRoleTypes (System API)

## Modules to Import

```TypeScript
import { usbManager } from 'usbManager';
```

## setPortRoleTypes

```TypeScript
function setPortRoleTypes(portId: int, powerRole: PowerRoleType, dataRole: DataRoleType): Promise<void>
```

Sets the role types supported by a specified port, which can be **powerRole** (for charging) and **dataRole** (for data transfer). This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function setPortRoleTypes(portId: int, powerRole: PowerRoleType, dataRole: DataRoleType): Promise<void>--><!--Device-usbManager-function setPortRoleTypes(portId: int, powerRole: PowerRoleType, dataRole: DataRoleType): Promise<void>-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| portId | int | Yes | Port number. |
| powerRole | PowerRoleType | Yes | Role for charging. |
| dataRole | DataRoleType | Yes | Role for data transfer. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:  <br>1.Mandatory parameters are left unspecified.  <br>2.Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported.<br>**Applicable version:** 18 and later |
| [14400003](../../apis-basic-services-kit/errorcode-usb.md#14400003-port-role-switching-unsupported) | Unsupported operation. The current device does not support port role switching. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 18 and later |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Normal application do not have permission to use system api. |

