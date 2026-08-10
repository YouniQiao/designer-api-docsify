# DeviceBasicInfo

分布式设备基本信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-distributedDeviceManager-interface DeviceBasicInfo--><!--Device-distributedDeviceManager-interface DeviceBasicInfo-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## Modules to Import

```TypeScript
import { distributedDeviceManager } from 'kits/@kit.DistributedServiceKit';
```

## deviceId

```TypeScript
deviceId: string
```

设备标识符。实际值为udid-hash与appid和盐值基于sha256方式进行混淆后的值。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DeviceBasicInfo-deviceId: string--><!--Device-DeviceBasicInfo-deviceId: string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## deviceName

```TypeScript
deviceName: string
```

设备名称。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DeviceBasicInfo-deviceName: string--><!--Device-DeviceBasicInfo-deviceName: string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## deviceType

```TypeScript
deviceType: string
```

[设备类型](arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getdevicetype)。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DeviceBasicInfo-deviceType: string--><!--Device-DeviceBasicInfo-deviceType: string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## networkId

```TypeScript
networkId?: string
```

设备网络标识。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DeviceBasicInfo-networkId?: string--><!--Device-DeviceBasicInfo-networkId?: string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

