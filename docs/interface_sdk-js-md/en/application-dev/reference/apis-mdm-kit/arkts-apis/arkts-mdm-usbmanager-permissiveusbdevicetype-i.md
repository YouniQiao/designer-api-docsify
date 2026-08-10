# PermissiveUsbDeviceType

USB设备类型信息，支持部分字段匹配。

- 与[UsbDeviceType](arkts-mdm-usbmanager-usbdevicetype-i.md)相比，本接口的subClass、protocol、descriptor字段为可选字段，实现更灵活的USB设备禁用策略。  
- 支持仅根据baseClass字段进行匹配。  
- 支持配置多个字段，多个字段同时满足才匹配。  
- 可通过[getDevices](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-usbmanager-getdevices-f.md/arkts-basicservices-usbmanager-getdevices-f.md#getdevices)接口获取已接入主设备的USB设备列表，并从返回值列表中查找当前设备的类型信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-usbManager-export interface PermissiveUsbDeviceType--><!--Device-usbManager-export interface PermissiveUsbDeviceType-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.MDMKit';
```

## baseClass

```TypeScript
baseClass: number
```

类型编码。取值范围为[0, 255]。若descriptor为DEVICE，则本字段取USBDevice.clazz字段值；若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.clazz字段值。

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissiveUsbDeviceType-baseClass: number--><!--Device-PermissiveUsbDeviceType-baseClass: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## descriptor

```TypeScript
descriptor?: Descriptor
```

USB描述符。若USBDevice.clazz字段值为0，则须在[defined-class-codes](https://www.usb.org/defined-class-codes)中的Base Class列查找USBDevice.configs.interfaces.clazz字段值，查找结果所在行所对应的Descriptor Usage列就表示当前应该传入的descriptor类型（若Descriptor Usage列为Both，表示两种类型都可以传入，需要设备级禁用时传入DEVICE，需要接口级禁用时传入INTERFACE）；若USBDevice.clazz字段值为其他值，则须在  
[defined-class-codes](https://www.usb.org/defined-class-codes)中的Base Class列查找该值，查找结果所在行所对应的Descriptor Usage列就表示当前应该传入的descriptor类型（若Descriptor Usage列为Both，表示两种类型都可以传入，需要设备级禁用时传入DEVICE，需要接口级禁用时传入INTERFACE）。

**Type:** [Descriptor](arkts-mdm-usbmanager-descriptor-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissiveUsbDeviceType-descriptor?: Descriptor--><!--Device-PermissiveUsbDeviceType-descriptor?: Descriptor-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## protocol

```TypeScript
protocol?: number
```

协议编码。取值范围为[0, 255]。若descriptor为DEVICE，则本字段取USBDevice.protocol字段值；若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.protocol字段值。

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissiveUsbDeviceType-protocol?: number--><!--Device-PermissiveUsbDeviceType-protocol?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## subClass

```TypeScript
subClass?: number
```

子类型编码。取值范围为[0, 255]。若descriptor为DEVICE，则本字段取USBDevice.subClass字段值；若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.subClass字段值。

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissiveUsbDeviceType-subClass?: number--><!--Device-PermissiveUsbDeviceType-subClass?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

