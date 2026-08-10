# MetadataObject

相机元能力信息，[CameraInput](arkts-camera-camera-camerainput-i.md)相机信息中的数据来源，通过metadataOutput.on('metadataObjectsAvailable')接口获取。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-camera-interface MetadataObject--><!--Device-camera-interface MetadataObject-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## confidence

```TypeScript
readonly confidence: double
```

Confidence of the detection, with a value range of [0, 1].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-MetadataObject-readonly confidence: double--><!--Device-MetadataObject-readonly confidence: double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## objectId

```TypeScript
readonly objectId: int
```

Metadata object ID.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-MetadataObject-readonly objectId: int--><!--Device-MetadataObject-readonly objectId: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

