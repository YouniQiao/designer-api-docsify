# BindTargetResult

Bind target result.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.DistributedHardware.DeviceManager

## Modules to Import

```TypeScript
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
```

## deviceId

```TypeScript
deviceId: string
```

Device identifier. The actual value is udid-hash confused with appid and salt value based on sha256. This id remains unchanged after application installation. If the application is uninstalled and reinstalled, the obtained ID will change.

**Type:** string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.DistributedHardware.DeviceManager
