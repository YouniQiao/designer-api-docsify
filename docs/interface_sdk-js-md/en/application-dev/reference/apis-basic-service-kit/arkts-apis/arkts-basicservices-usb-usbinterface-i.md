# USBInterface

Represents a USB interface. One [USBConfig](arkts-basicservices-usb-usbconfig-i.md) can contain multiple **USBInterface** instances,each providing a specific function.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBInterface](arkts-basicservices-usbmanager-usbinterface-i.md)

<!--Device-usb-interface USBInterface--><!--Device-usb-interface USBInterface-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## alternateSetting

```TypeScript
alternateSetting: number
```

Settings for alternating between descriptors of the same USB interface.

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBInterface.alternateSetting](arkts-basicservices-usbmanager-usbinterface-i.md#alternatesetting)

<!--Device-USBInterface-alternateSetting: number--><!--Device-USBInterface-alternateSetting: number-End-->

**System capability:** SystemCapability.USB.USBManager

## clazz

```TypeScript
clazz: number
```

Device type.

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBInterface.clazz](arkts-basicservices-usbmanager-usbinterface-i.md#clazz)

<!--Device-USBInterface-clazz: number--><!--Device-USBInterface-clazz: number-End-->

**System capability:** SystemCapability.USB.USBManager

## endpoints

```TypeScript
endpoints: Array<USBEndpoint>
```

Endpoints that belong to the USB interface.

**Type:** Array&lt;USBEndpoint&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBInterface.endpoints](arkts-basicservices-usbmanager-usbinterface-i.md#endpoints)

<!--Device-USBInterface-endpoints: Array<USBEndpoint>--><!--Device-USBInterface-endpoints: Array<USBEndpoint>-End-->

**System capability:** SystemCapability.USB.USBManager

## id

```TypeScript
id: number
```

Unique ID of the USB interface.

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBInterface.id](arkts-basicservices-usbmanager-usbinterface-i.md#id)

<!--Device-USBInterface-id: number--><!--Device-USBInterface-id: number-End-->

**System capability:** SystemCapability.USB.USBManager

## name

```TypeScript
name: string
```

Interface name.

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBInterface.name](arkts-basicservices-usbmanager-usbinterface-i.md#name)

<!--Device-USBInterface-name: string--><!--Device-USBInterface-name: string-End-->

**System capability:** SystemCapability.USB.USBManager

## protocol

```TypeScript
protocol: number
```

Interface protocol.

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBInterface.protocol](arkts-basicservices-usbmanager-usbinterface-i.md#protocol)

<!--Device-USBInterface-protocol: number--><!--Device-USBInterface-protocol: number-End-->

**System capability:** SystemCapability.USB.USBManager

## subClass

```TypeScript
subClass: number
```

Device subclass.

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBInterface.subClass](arkts-basicservices-usbmanager-usbinterface-i.md#subclass)

<!--Device-USBInterface-subClass: number--><!--Device-USBInterface-subClass: number-End-->

**System capability:** SystemCapability.USB.USBManager

