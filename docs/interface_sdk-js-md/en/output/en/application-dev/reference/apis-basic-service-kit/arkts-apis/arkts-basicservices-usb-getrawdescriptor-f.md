# getRawDescriptor

## getRawDescriptor

```TypeScript
function getRawDescriptor(pipe: USBDevicePipe): Uint8Array
```

Obtains the raw USB descriptor. Before you do this, call [usb.getDevices]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to obtain the USB device list, call [usb.requestRight]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to request the device access permission, and call [usb.connectDevice]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ to obtain **devicepipe** as an input parameter.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.getRawDescriptor](arkts-basicservices-usbmanager-getrawdescriptor-f.md#getrawdescriptor)

<!--Device-usb-function getRawDescriptor(pipe: USBDevicePipe): Uint8Array--><!--Device-usb-function getRawDescriptor(pipe: USBDevicePipe): Uint8Array-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Device pipe, which is used to determine the bus number and device address. |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | Returns the raw USB descriptor if the operation is successful; returns **undefined** |

**Example**

```TypeScript
let ret = usb.getRawDescriptor(devicepipe);
```

