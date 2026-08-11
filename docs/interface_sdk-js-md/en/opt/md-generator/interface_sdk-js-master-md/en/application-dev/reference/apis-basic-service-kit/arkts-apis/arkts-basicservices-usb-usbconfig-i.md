# USBConfig

Represents the USB configuration. One [USBDevice](arkts-basicservices-usb-usbdevice-i.md) can contain multiple **USBConfig**instances.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration](arkts-basicservices-usbmanager-usbconfiguration-i.md)

<!--Device-usb-interface USBConfig--><!--Device-usb-interface USBConfig-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## attributes

```TypeScript
attributes: number
```

Configuration attributes.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.attributes](arkts-basicservices-usbmanager-usbconfiguration-i.md#attributes)

<!--Device-USBConfig-attributes: number--><!--Device-USBConfig-attributes: number-End-->

**System capability:** SystemCapability.USB.USBManager

## id

```TypeScript
id: number
```

Unique ID of the USB configuration.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.id](arkts-basicservices-usbmanager-usbconfiguration-i.md#id)

<!--Device-USBConfig-id: number--><!--Device-USBConfig-id: number-End-->

**System capability:** SystemCapability.USB.USBManager

## interfaces

```TypeScript
interfaces: Array<USBInterface>
```

Supported interface attributes.

**Type:** Array&lt;USBInterface&gt;

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.interfaces](arkts-basicservices-usbmanager-usbconfiguration-i.md#interfaces)

<!--Device-USBConfig-interfaces: Array<USBInterface>--><!--Device-USBConfig-interfaces: Array<USBInterface>-End-->

**System capability:** SystemCapability.USB.USBManager

## isRemoteWakeup

```TypeScript
isRemoteWakeup: boolean
```

Support for remote wakeup.

**Type:** boolean

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.isRemoteWakeup](arkts-basicservices-usbmanager-usbconfiguration-i.md#isremotewakeup)

<!--Device-USBConfig-isRemoteWakeup: boolean--><!--Device-USBConfig-isRemoteWakeup: boolean-End-->

**System capability:** SystemCapability.USB.USBManager

## isSelfPowered

```TypeScript
isSelfPowered: boolean
```

Support for independent power supplies.

**Type:** boolean

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.isSelfPowered](arkts-basicservices-usbmanager-usbconfiguration-i.md#isselfpowered)

<!--Device-USBConfig-isSelfPowered: boolean--><!--Device-USBConfig-isSelfPowered: boolean-End-->

**System capability:** SystemCapability.USB.USBManager

## maxPower

```TypeScript
maxPower: number
```

Maximum power consumption, in mA.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.maxPower](arkts-basicservices-usbmanager-usbconfiguration-i.md#maxpower)

<!--Device-USBConfig-maxPower: number--><!--Device-USBConfig-maxPower: number-End-->

**System capability:** SystemCapability.USB.USBManager

## name

```TypeScript
name: string
```

Configuration name, which can be left empty.

**Type:** string

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.name](arkts-basicservices-usbmanager-usbconfiguration-i.md#name)

<!--Device-USBConfig-name: string--><!--Device-USBConfig-name: string-End-->

**System capability:** SystemCapability.USB.USBManager
