# MetadataObject

Describes the camera metadata, which is the data source of [CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput). The metadata is obtained through **metadataOutput.on('metadataObjectsAvailable')**.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface MetadataObject--><!--Device-camera-interface MetadataObject-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## confidence

```TypeScript
readonly confidence: double
```

Confidence of the detection, with a value range of [0, 1].

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MetadataObject-readonly confidence: double--><!--Device-MetadataObject-readonly confidence: double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## objectId

```TypeScript
readonly objectId: int
```

Metadata object ID.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MetadataObject-readonly objectId: int--><!--Device-MetadataObject-readonly objectId: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

