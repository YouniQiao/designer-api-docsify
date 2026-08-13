# setDeviceFunctions (System API)

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## setDeviceFunctions

```TypeScript
function setDeviceFunctions(funcs: FunctionType): Promise<void>
```

Sets the current USB function list in Device mode. This API uses a promise to return the result.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function setDeviceFunctions(funcs: FunctionType): Promise<void>--><!--Device-usbManager-function setDeviceFunctions(funcs: FunctionType): Promise<void>-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| funcs | [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [14400002](../../apis-basic-services-kit/errorcode-usb.md#14400002-hdc-disabled) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14400006](../../apis-basic-services-kit/errorcode-usb.md#14400006-usb-device-function-unsupported) |


## setDeviceFunctions

```TypeScript
function setDeviceFunctions(funcs: number): Promise<void>
```

Sets the current USB function list in Device mode.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function setDeviceFunctions(funcs: int): Promise<void>--><!--Device-usbManager-function setDeviceFunctions(funcs: int): Promise<void>-End-->

**System capability:** SystemCapability.USB.USBManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| funcs | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [14400002](../../apis-basic-services-kit/errorcode-usb.md#14400002-hdc-disabled) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14400006](../../apis-basic-services-kit/errorcode-usb.md#14400006-usb-device-function-unsupported) |
