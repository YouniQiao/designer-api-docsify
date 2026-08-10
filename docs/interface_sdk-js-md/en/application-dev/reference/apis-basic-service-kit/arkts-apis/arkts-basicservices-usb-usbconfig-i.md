# USBConfig

USB配置，一个[USBDevice](arkts-basicservices-usb-usbdevice-i.md)中可以含有多个配置。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

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

配置的属性。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.attributes](arkts-basicservices-usbmanager-usbconfiguration-i.md#attributes)

<!--Device-USBConfig-attributes: number--><!--Device-USBConfig-attributes: number-End-->

**System capability:** SystemCapability.USB.USBManager

## id

```TypeScript
id: number
```

配置的唯一标识。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.id](arkts-basicservices-usbmanager-usbconfiguration-i.md#id)

<!--Device-USBConfig-id: number--><!--Device-USBConfig-id: number-End-->

**System capability:** SystemCapability.USB.USBManager

## interfaces

```TypeScript
interfaces: Array<USBInterface>
```

配置支持的接口属性。

**Type:** Array&lt;USBInterface&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.interfaces](arkts-basicservices-usbmanager-usbconfiguration-i.md#interfaces)

<!--Device-USBConfig-interfaces: Array<USBInterface>--><!--Device-USBConfig-interfaces: Array<USBInterface>-End-->

**System capability:** SystemCapability.USB.USBManager

## isRemoteWakeup

```TypeScript
isRemoteWakeup: boolean
```

检查当前配置是否支持远程唤醒。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.isRemoteWakeup](arkts-basicservices-usbmanager-usbconfiguration-i.md#isremotewakeup)

<!--Device-USBConfig-isRemoteWakeup: boolean--><!--Device-USBConfig-isRemoteWakeup: boolean-End-->

**System capability:** SystemCapability.USB.USBManager

## isSelfPowered

```TypeScript
isSelfPowered: boolean
```

检查当前配置是否支持独立电源。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.isSelfPowered](arkts-basicservices-usbmanager-usbconfiguration-i.md#isselfpowered)

<!--Device-USBConfig-isSelfPowered: boolean--><!--Device-USBConfig-isSelfPowered: boolean-End-->

**System capability:** SystemCapability.USB.USBManager

## maxPower

```TypeScript
maxPower: number
```

最大功耗，以毫安为单位。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.maxPower](arkts-basicservices-usbmanager-usbconfiguration-i.md#maxpower)

<!--Device-USBConfig-maxPower: number--><!--Device-USBConfig-maxPower: number-End-->

**System capability:** SystemCapability.USB.USBManager

## name

```TypeScript
name: string
```

配置的名称，可以为空。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.USBConfiguration.name](arkts-basicservices-usbmanager-usbconfiguration-i.md#name)

<!--Device-USBConfig-name: string--><!--Device-USBConfig-name: string-End-->

**System capability:** SystemCapability.USB.USBManager

