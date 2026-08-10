# TorchStatusInfo

手电筒回调返回的接口实例，表示手电筒状态信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-camera-interface TorchStatusInfo--><!--Device-camera-interface TorchStatusInfo-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## isTorchActive

```TypeScript
readonly isTorchActive: boolean
```

手电筒是否被激活。true表示手电筒被激活，false表示手电筒未被激活。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-TorchStatusInfo-readonly isTorchActive: boolean--><!--Device-TorchStatusInfo-readonly isTorchActive: boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## isTorchAvailable

```TypeScript
readonly isTorchAvailable: boolean
```

手电筒是否可用。true表示手电筒可用，false表示手电筒不可用。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-TorchStatusInfo-readonly isTorchAvailable: boolean--><!--Device-TorchStatusInfo-readonly isTorchAvailable: boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## torchLevel

```TypeScript
readonly torchLevel: double
```

手电筒亮度等级，取值范围为[0,1]，越靠近1，亮度越大。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-TorchStatusInfo-readonly torchLevel: double--><!--Device-TorchStatusInfo-readonly torchLevel: double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

