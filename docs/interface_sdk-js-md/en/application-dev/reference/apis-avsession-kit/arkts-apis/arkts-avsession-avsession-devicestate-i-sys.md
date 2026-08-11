# DeviceState (System API)

Device state used to describe states including discovery, authentication and other scenes.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-avSession-interface DeviceState--><!--Device-avSession-interface DeviceState-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## deviceId

```TypeScript
readonly deviceId: string
```

Unique device descriptor.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DeviceState-readonly deviceId: string--><!--Device-DeviceState-readonly deviceId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## deviceState

```TypeScript
readonly deviceState: int
```

Device connection state.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DeviceState-readonly deviceState: int--><!--Device-DeviceState-readonly deviceState: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## radarErrorCode

```TypeScript
readonly radarErrorCode: int
```

System radar error code returned by cast+services.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DeviceState-readonly radarErrorCode: int--><!--Device-DeviceState-readonly radarErrorCode: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## reasonCode

```TypeScript
readonly reasonCode: int
```

Reason for connection failure, for example, user cancellation and timeout.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DeviceState-readonly reasonCode: int--><!--Device-DeviceState-readonly reasonCode: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

