# USBDriverInfo (System API)

Defines detailed information about the USB device driver. It is inherited from [DriverInfo](arkts-driverdevelopment-devicemanager-driverinfo-i-sys.md).

**Inheritance/Implementation:** USBDriverInfo extends [DriverInfo](arkts-driverdevelopment-devicemanager-driverinfo-i-sys.md)

**Since:** 23

<!--Device-deviceManager-interface USBDriverInfo--><!--Device-deviceManager-interface USBDriverInfo-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { deviceManager } from '@kit.DriverDevelopmentKit';
```

## productIdList

```TypeScript
productIdList: Array<int>
```

Product ID list of the USB devices supported by the driver.

**Type:** Array&lt;int&gt;

**Since:** 23

<!--Device-USBDriverInfo-productIdList: Array<int>--><!--Device-USBDriverInfo-productIdList: Array<int>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

## vendorIdList

```TypeScript
vendorIdList: Array<int>
```

Vendor ID list of the USB devices supported by the driver.

**Type:** Array&lt;int&gt;

**Since:** 23

<!--Device-USBDriverInfo-vendorIdList: Array<int>--><!--Device-USBDriverInfo-vendorIdList: Array<int>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

