# DeviceBasicInfo

Represents the basic information about a distributed device.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-distributedDeviceManager-interface DeviceBasicInfo--><!--Device-distributedDeviceManager-interface DeviceBasicInfo-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## deviceId

```TypeScript
deviceId: string
```

Device ID. The value is the result of obfuscating the udid-hash (hash value of the UDID), **appid**, and salt using the SHA-256 algorithm.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DeviceBasicInfo-deviceId: string--><!--Device-DeviceBasicInfo-deviceId: string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## deviceName

```TypeScript
deviceName: string
```

Device name.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DeviceBasicInfo-deviceName: string--><!--Device-DeviceBasicInfo-deviceName: string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## deviceType

```TypeScript
deviceType: string
```

[Device type]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DeviceBasicInfo-deviceType: string--><!--Device-DeviceBasicInfo-deviceType: string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## networkId

```TypeScript
networkId?: string
```

Network ID of the device.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DeviceBasicInfo-networkId?: string--><!--Device-DeviceBasicInfo-networkId?: string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

