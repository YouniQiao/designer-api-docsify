# CameraConcurrentInfo

相机的输出并发能力信息。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-camera-interface CameraConcurrentInfo--><!--Device-camera-interface CameraConcurrentInfo-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## device

```TypeScript
readonly device: CameraDevice
```

相机并发设备。

**Type:** [CameraDevice](arkts-camera-camera-cameradevice-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraConcurrentInfo-readonly device: CameraDevice--><!--Device-CameraConcurrentInfo-readonly device: CameraDevice-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## modes

```TypeScript
readonly modes: Array<SceneMode>
```

相机支持的模式。

**Type:** Array&lt;SceneMode&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraConcurrentInfo-readonly modes: Array<SceneMode>--><!--Device-CameraConcurrentInfo-readonly modes: Array<SceneMode>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## outputCapabilities

```TypeScript
readonly outputCapabilities: Array<CameraOutputCapability>
```

相机对应模式的输出能力集。

**Type:** Array&lt;CameraOutputCapability&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraConcurrentInfo-readonly outputCapabilities: Array<CameraOutputCapability>--><!--Device-CameraConcurrentInfo-readonly outputCapabilities: Array<CameraOutputCapability>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## type

```TypeScript
readonly type: CameraConcurrentType
```

镜头并发类型。

**Type:** [CameraConcurrentType](arkts-camera-camera-cameraconcurrenttype-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraConcurrentInfo-readonly type: CameraConcurrentType--><!--Device-CameraConcurrentInfo-readonly type: CameraConcurrentType-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

