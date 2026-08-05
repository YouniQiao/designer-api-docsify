# releaseInterface

## releaseInterface

```TypeScript
function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number
```

Releases a USB interface. Before you do this, ensure that you have claimed the interface by calling [usb.claimInterface]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.releaseInterface](arkts-basicservices-usbmanager-releaseinterface-f.md#releaseinterface)

<!--Device-usb-function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number--><!--Device-usb-function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Device pipe, which is used to determine the bus number and device address. |
| iface | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | USB interface, which is used to determine the index of the interface to release. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns **0** if the USB interface is successfully released; returns an error code otherwise. |

**Example**

```TypeScript
let ret = usb.releaseInterface(devicepipe, interfaces);
console.info(`releaseInterface = ${ret}`);
```

