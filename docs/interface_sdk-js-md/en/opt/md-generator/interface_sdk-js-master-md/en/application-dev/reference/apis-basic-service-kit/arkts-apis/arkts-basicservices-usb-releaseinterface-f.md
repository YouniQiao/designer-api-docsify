# releaseInterface

## Modules to Import

```TypeScript
```

## releaseInterface

```TypeScript
function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number
```

Releases a USB interface. Before you do this, ensure that you have claimed the interface by calling [usb.claimInterface](arkts-basicservices-usb-claiminterface-f.md#claiminterface).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [releaseInterface](arkts-basicservices-usbmanager-releaseinterface-f.md#releaseinterface)

<!--Device-usb-function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number--><!--Device-usb-function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes |
| iface | [USBInterface](arkts-basicservices-usb-usbinterface-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
let ret = usb.releaseInterface(devicepipe, interfaces);
console.info(`releaseInterface = ${ret}`);
```
