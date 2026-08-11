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

## audioCapabilities

```TypeScript
audioCapabilities?: AudioCapabilities
```

Audio capabilities supported by the device.

**Type:** [AudioCapabilities](arkts-avsession-avsession-audiocapabilities-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DeviceInfo-audioCapabilities?: AudioCapabilities--><!--Device-DeviceInfo-audioCapabilities?: AudioCapabilities-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## castCategory

```TypeScript
castCategory: AVCastCategory
```

The playback type supported by the device. See {@link AVCastCategory}

**Type:** [AVCastCategory](arkts-avsession-avsession-avcastcategory-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DeviceInfo-castCategory: AVCastCategory--><!--Device-DeviceInfo-castCategory: AVCastCategory-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## deviceId

```TypeScript
deviceId: string
```

Audio device id.The length of the audioDeviceId array is greater than 1if output to multiple devices at the same time.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DeviceInfo-deviceId: string--><!--Device-DeviceInfo-deviceId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## deviceName

```TypeScript
deviceName: string
```

Device name. The length of the deviceName array is greater than 1if output to multiple devices at the same time.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DeviceInfo-deviceName: string--><!--Device-DeviceInfo-deviceName: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## deviceType

```TypeScript
deviceType: DeviceType
```

device type.

**Type:** [DeviceType](arkts-avsession-avsession-devicetype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DeviceInfo-deviceType: DeviceType--><!--Device-DeviceInfo-deviceType: DeviceType-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## manufacturer

```TypeScript
manufacturer?: string
```

Device manufacturer.

**Type:** string

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-DeviceInfo-manufacturer?: string--><!--Device-DeviceInfo-manufacturer?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## modelName

```TypeScript
modelName?: string
```

Device model name.

**Type:** string

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-DeviceInfo-modelName?: string--><!--Device-DeviceInfo-modelName?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## supportedDrmCapabilities

```TypeScript
supportedDrmCapabilities?: Array<string>
```

The drm capability supported by current device, each drm is represented by uuid.

**Type:** Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DeviceInfo-supportedDrmCapabilities?: Array<string>--><!--Device-DeviceInfo-supportedDrmCapabilities?: Array<string>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## supportedProtocols

```TypeScript
supportedProtocols?: int
```

The protocols supported by current device, can be union of {@link ProtocolType}.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DeviceInfo-supportedProtocols?: int--><!--Device-DeviceInfo-supportedProtocols?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## supportedPullClients

```TypeScript
supportedPullClients?: Array<int>
```

Whether the device supports pull-end playback, including a collection of pull-end client IDs.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DeviceInfo-supportedPullClients?: Array<int>--><!--Device-DeviceInfo-supportedPullClients?: Array<int>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

