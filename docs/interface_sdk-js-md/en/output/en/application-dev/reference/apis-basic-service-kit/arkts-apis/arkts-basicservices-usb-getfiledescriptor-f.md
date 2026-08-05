# getFileDescriptor

## getFileDescriptor

```TypeScript
function getFileDescriptor(pipe: USBDevicePipe): number
```

Obtains the file descriptor. Before you do this, call [usb.getDevices]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to obtain the USB device list, call [usb.requestRight]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to request the device access permission, and call [usb.connectDevice]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ to obtain **devicepipe** as an input parameter.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.getFileDescriptor](arkts-basicservices-usbmanager-getfiledescriptor-f.md#getfiledescriptor)

<!--Device-usb-function getFileDescriptor(pipe: USBDevicePipe): number--><!--Device-usb-function getFileDescriptor(pipe: USBDevicePipe): number-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Device pipe, which is used to determine the bus number and device address. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the file descriptor of the USB device if the operation is successful; returns **-1** |

**Example**

```TypeScript
let ret = usb.getFileDescriptor(devicepipe);
```

