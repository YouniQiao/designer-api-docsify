# claimInterface

## claimInterface

```TypeScript
function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number
```

Claims a USB interface.

Before you do this, call [usb.getDevices]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to obtain the USB device list and USB interfaces,call [usb.requestRight]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to request the device access permission, and call  
[usb.connectDevice]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ to obtain **devicepipe** as an input parameter.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md#claiminterface)

<!--Device-usb-function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number--><!--Device-usb-function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Device pipe, which is used to determine the bus number and device address. |
| iface | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | USB interface, which is used to determine the index of the interface to claim. |
| force | boolean | No | Whether to forcibly claim the USB interface. The default value is **false**, indicating not to forcibly claim the USB interface. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns **0** if the USB interface is successfully claimed; returns an error code otherwise. |

**Example**

```TypeScript
let ret = usb.claimInterface(devicepipe, interfaces);
console.info(`claimInterface = ${ret}`);
```

