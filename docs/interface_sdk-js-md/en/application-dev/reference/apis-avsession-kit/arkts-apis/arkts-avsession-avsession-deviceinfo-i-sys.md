# DeviceInfo

Device Information Definition

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-interface DeviceInfo--><!--Device-avSession-interface DeviceInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## authenticationStatus

```TypeScript
authenticationStatus?: int
```

Define different authentication status.0: Device not authenticated.1: Device already authenticated.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DeviceInfo-authenticationStatus?: int--><!--Device-DeviceInfo-authenticationStatus?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## hiPlayDeviceInfo

```TypeScript
hiPlayDeviceInfo?: HiPlayDeviceInfo
```

HiPlayDeviceInfo is used to obtain device-specific information for HiPlay.transmit info during casting.

**Type:** [HiPlayDeviceInfo](arkts-avsession-avsession-hiplaydeviceinfo-i-sys.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceInfo-hiPlayDeviceInfo?: HiPlayDeviceInfo--><!--Device-DeviceInfo-hiPlayDeviceInfo?: HiPlayDeviceInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## ipAddress

```TypeScript
ipAddress?: string
```

device ip address if available.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DeviceInfo-ipAddress?: string--><!--Device-DeviceInfo-ipAddress?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## isLegacy

```TypeScript
isLegacy?: boolean
```

Indicates the current device is legacy or not.

**Type:** boolean

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-DeviceInfo-isLegacy?: boolean--><!--Device-DeviceInfo-isLegacy?: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## mediumTypes

```TypeScript
mediumTypes?: int
```

Medium types used to discover devices.1: BLE2: COAP

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-DeviceInfo-mediumTypes?: int--><!--Device-DeviceInfo-mediumTypes?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## networkId

```TypeScript
networkId?: string
```

Network id.

**Type:** string

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-DeviceInfo-networkId?: string--><!--Device-DeviceInfo-networkId?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## providerId

```TypeScript
providerId?: int
```

device provider which supplies the route capability.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-DeviceInfo-providerId?: int--><!--Device-DeviceInfo-providerId?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

