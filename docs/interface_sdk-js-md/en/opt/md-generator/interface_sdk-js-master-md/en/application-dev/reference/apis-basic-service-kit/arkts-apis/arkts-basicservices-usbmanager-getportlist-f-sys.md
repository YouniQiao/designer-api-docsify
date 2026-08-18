# getPortList (System API)

## Modules to Import

```TypeScript
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

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;USBPort & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-service-exception) |
