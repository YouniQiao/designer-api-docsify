# USBInterface

一个[USBConfig](arkts-basicservices-usb-usbconfig-i.md)中可以含有多个USBInterface，每个USBInterface提供一个功能。

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

在同一个接口中的多个描述符中进行切换设置。

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

设备类型。

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

当前接口所包含的端点。

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

接口的唯一标识。

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

接口名称。

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

接口的协议。

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

设备子类。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBInterface.subClass](arkts-basicservices-usbmanager-usbinterface-i.md#subclass)

<!--Device-USBInterface-subClass: number--><!--Device-USBInterface-subClass: number-End-->

**System capability:** SystemCapability.USB.USBManager

