# BindTargetResult

Bind target result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-distributedDeviceManager-interface BindTargetResult--><!--Device-distributedDeviceManager-interface BindTargetResult-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## deviceId

```TypeScript
deviceId: string
```

Device identifier. The actual value is udid-hash confused with appid and salt value based on sha256.This id remains unchanged after application installation. If the application is uninstalled and reinstalled,the obtained ID will change.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-BindTargetResult-deviceId: string--><!--Device-BindTargetResult-deviceId: string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

