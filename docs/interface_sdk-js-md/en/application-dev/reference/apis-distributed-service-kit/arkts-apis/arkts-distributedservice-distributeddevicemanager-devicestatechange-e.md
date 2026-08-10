# DeviceStateChange

表示设备状态。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-distributedDeviceManager-enum DeviceStateChange--><!--Device-distributedDeviceManager-enum DeviceStateChange-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## UNKNOWN

```TypeScript
UNKNOWN = 0
```

设备物理上线，此时状态未知，在状态更改为可用之前，分布式业务无法使用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DeviceStateChange-UNKNOWN = 0--><!--Device-DeviceStateChange-UNKNOWN = 0-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## AVAILABLE

```TypeScript
AVAILABLE = 1
```

设备可用状态，表示设备间信息已在分布式数据中同步完成，可以运行分布式业务。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DeviceStateChange-AVAILABLE = 1--><!--Device-DeviceStateChange-AVAILABLE = 1-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## UNAVAILABLE

```TypeScript
UNAVAILABLE = 2
```

设备物理下线，此时状态未知。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DeviceStateChange-UNAVAILABLE = 2--><!--Device-DeviceStateChange-UNAVAILABLE = 2-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

