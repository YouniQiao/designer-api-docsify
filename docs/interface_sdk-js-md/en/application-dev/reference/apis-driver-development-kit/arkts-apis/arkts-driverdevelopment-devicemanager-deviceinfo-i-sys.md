# DeviceInfo (System API)

设备详细信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-deviceManager-interface DeviceInfo--><!--Device-deviceManager-interface DeviceInfo-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## deviceId

```TypeScript
deviceId: long
```

设备ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-DeviceInfo-deviceId: long--><!--Device-DeviceInfo-deviceId: long-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

## driverUid

```TypeScript
driverUid?: string
```

设备匹配的驱动UID。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-DeviceInfo-driverUid?: string--><!--Device-DeviceInfo-driverUid?: string-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

## isDriverMatched

```TypeScript
isDriverMatched: boolean
```

设备是否匹配到驱动。`true`：匹配到驱动；`false`：未匹配到驱动。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-DeviceInfo-isDriverMatched: boolean--><!--Device-DeviceInfo-isDriverMatched: boolean-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**System API:** This is a system API.

