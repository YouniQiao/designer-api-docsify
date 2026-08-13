# DeviceState (System API)

Device state used to describe states including discovery, authentication and other scenes.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-avSession-interface DeviceState--><!--Device-avSession-interface DeviceState-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## deviceId

```TypeScript
readonly deviceId: string
```

Unique device descriptor.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-DeviceState-readonly deviceId: string--><!--Device-DeviceState-readonly deviceId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## deviceState

```TypeScript
readonly deviceState: int
```

Device connection state.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-DeviceState-readonly deviceState: int--><!--Device-DeviceState-readonly deviceState: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## radarErrorCode

```TypeScript
readonly radarErrorCode: int
```

System radar error code returned by cast+services.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-DeviceState-readonly radarErrorCode: int--><!--Device-DeviceState-readonly radarErrorCode: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## reasonCode

```TypeScript
readonly reasonCode: int
```

Reason for connection failure, for example, user cancellation and timeout.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-DeviceState-readonly reasonCode: int--><!--Device-DeviceState-readonly reasonCode: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

