# connectDevice

## connectDevice

```TypeScript
function connectDevice(device: USBDevice): Readonly<USBDevicePipe>
```

Connects to a USB device. Before you do this, call [usb.getDevices]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to obtain the USB device list, and then call [usb.requestRight]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to request the device access permission.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectdevice)

<!--Device-usb-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>--><!--Device-usb-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| device | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | USB device information. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;USBDevicePipe&gt; | USB device pipe for data transfer. |

**Example**

```TypeScript
let devicepipe= usb.connectDevice(device);
console.info(`devicepipe = ${devicepipe}`);
```

