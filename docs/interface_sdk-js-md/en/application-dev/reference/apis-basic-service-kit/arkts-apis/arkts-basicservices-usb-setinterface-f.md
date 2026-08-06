# setInterface

## setInterface

```TypeScript
function setInterface(pipe: USBDevicePipe, iface: USBInterface): number
```

Sets a USB interface.

Before you do this, call [usb.getDevices]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to obtain the USB device list and interfaces, call  
[usb.requestRight]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to request the device access permission, call  
[usb.connectDevice]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ to obtain **devicepipe** as an input parameter, and call  
[usb.claimInterface]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ to claim the USB interface.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.setInterface](arkts-basicservices-usbmanager-setinterface-f.md#setinterface)

<!--Device-usb-function setInterface(pipe: USBDevicePipe, iface: USBInterface): number--><!--Device-usb-function setInterface(pipe: USBDevicePipe, iface: USBInterface): number-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Device pipe, which is used to determine the bus number and device address. |
| iface | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | USB interface to set. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns **0** if the USB interface is successfully set; returns an error code otherwise. |

**Example**

```TypeScript
let ret = usb.setInterface(devicepipe, interfaces);
console.info(`setInterface = ${ret}`);
```

