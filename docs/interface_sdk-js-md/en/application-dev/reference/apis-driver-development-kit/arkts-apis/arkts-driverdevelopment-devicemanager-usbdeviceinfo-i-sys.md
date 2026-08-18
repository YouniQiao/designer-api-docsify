# USBDeviceInfo (System API)

Defines detailed information about the USB device. It is inherited from [DeviceInfo](arkts-driverdevelopment-devicemanager-deviceinfo-i-sys.md).

**Inheritance/Implementation:** USBDeviceInfo extends [DeviceInfo](arkts-driverdevelopment-devicemanager-deviceinfo-i-sys.md)

**Since:** 23

<!--Device-deviceManager-interface USBDeviceInfo--><!--Device-deviceManager-interface USBDeviceInfo-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { deviceManager } from '@kit.DriverDevelopmentKit';
```

## interfaceDescList

```TypeScript
interfaceDescList: Array<Readonly<USBInterfaceDesc>>
```

List of interface descriptors of the USB device.

**Type:** Array&lt;[Readonly](../../apis-na/arkts-apis/arkts-na-readonly-t.md)&lt;[USBInterfaceDesc](arkts-driverdevelopment-devicemanager-usbinterfacedesc-i-sys.md)&gt;&gt;

**Since:** 23

<!--Device-USBDeviceInfo-interfaceDescList: Array<Readonly<USBInterfaceDesc>>--><!--Device-USBDeviceInfo-interfaceDescList: Array<Readonly<USBInterfaceDesc>>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

## productId

```TypeScript
productId: int
```

Product ID of the USB device.

**Type:** int

**Since:** 23

<!--Device-USBDeviceInfo-productId: int--><!--Device-USBDeviceInfo-productId: int-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

## vendorId

```TypeScript
vendorId: int
```

Vendor ID of the USB device.

**Type:** int

**Since:** 23

<!--Device-USBDeviceInfo-vendorId: int--><!--Device-USBDeviceInfo-vendorId: int-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

