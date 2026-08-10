# USBDeviceInfo (System API)

USB设备详细信息，继承自[DeviceInfo](arkts-driverdevelopment-devicemanager-deviceinfo-i-sys.md)。

**Inheritance/Implementation:** USBDeviceInfo extends [DeviceInfo](arkts-driverdevelopment-devicemanager-deviceinfo-i-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-deviceManager-interface USBDeviceInfo extends DeviceInfo--><!--Device-deviceManager-interface USBDeviceInfo extends DeviceInfo-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## interfaceDescList

```TypeScript
interfaceDescList: Array<Readonly<USBInterfaceDesc>>
```

USB设备接口描述符列表。

**Type:** Array&lt;Readonly&lt;USBInterfaceDesc&gt;&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-USBDeviceInfo-interfaceDescList: Array<Readonly<USBInterfaceDesc>>--><!--Device-USBDeviceInfo-interfaceDescList: Array<Readonly<USBInterfaceDesc>>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

## productId

```TypeScript
productId: int
```

USB设备Product ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-USBDeviceInfo-productId: int--><!--Device-USBDeviceInfo-productId: int-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

## vendorId

```TypeScript
vendorId: int
```

USB设备Vendor ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-USBDeviceInfo-vendorId: int--><!--Device-USBDeviceInfo-vendorId: int-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

