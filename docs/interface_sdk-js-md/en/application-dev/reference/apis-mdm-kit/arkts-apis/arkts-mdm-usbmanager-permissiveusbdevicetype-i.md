# PermissiveUsbDeviceType

Permissive USB device Type.

**Since:** 26.0.0

<!--Device-usbManager-export interface PermissiveUsbDeviceType--><!--Device-usbManager-export interface PermissiveUsbDeviceType-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { usbManager } from '@kit.MDMKit';
```

## baseClass

```TypeScript
baseClass: number
```

The base class in USB class code information.The value must be an integer within [0,255].

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissiveUsbDeviceType-baseClass: number--><!--Device-PermissiveUsbDeviceType-baseClass: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## descriptor

```TypeScript
descriptor?: Descriptor
```

The descriptor that the class code is used in.

**Type:** Descriptor

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissiveUsbDeviceType-descriptor?: Descriptor--><!--Device-PermissiveUsbDeviceType-descriptor?: Descriptor-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## protocol

```TypeScript
protocol?: number
```

The protocol in USB class code information.The value must be an integer within [0,255].

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissiveUsbDeviceType-protocol?: number--><!--Device-PermissiveUsbDeviceType-protocol?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## subClass

```TypeScript
subClass?: number
```

The subclass in USB class code information.The value must be an integer within [0,255].

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PermissiveUsbDeviceType-subClass?: number--><!--Device-PermissiveUsbDeviceType-subClass?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

