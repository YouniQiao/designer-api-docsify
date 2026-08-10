# USBDriverInfo (System API)

USB设备驱动详细信息，继承自[DriverInfo](arkts-driverdevelopment-devicemanager-driverinfo-i-sys.md)。

**Inheritance/Implementation:** USBDriverInfo extends [DriverInfo](arkts-driverdevelopment-devicemanager-driverinfo-i-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-deviceManager-interface USBDriverInfo extends DriverInfo--><!--Device-deviceManager-interface USBDriverInfo extends DriverInfo-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## productIdList

```TypeScript
productIdList: Array<int>
```

驱动支持的USB设备product ID列表。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-USBDriverInfo-productIdList: Array<int>--><!--Device-USBDriverInfo-productIdList: Array<int>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

## vendorIdList

```TypeScript
vendorIdList: Array<int>
```

驱动支持的USB设备vendor ID列表。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-USBDriverInfo-vendorIdList: Array<int>--><!--Device-USBDriverInfo-vendorIdList: Array<int>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

