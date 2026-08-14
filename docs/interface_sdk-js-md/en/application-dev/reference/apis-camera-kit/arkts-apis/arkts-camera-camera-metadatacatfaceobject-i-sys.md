# MetadataCatFaceObject (System API)

Cat face metadata detected by the camera, which is extended from [MetadataObject](arkts-camera-camera-metadataobject-i.md#MetadataObject). It serves as the data source of the camera information in [CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput). It is obtained by calling metadataOutput. [on('metadataObjectsAvailable')](arkts-camera-camera-metadataoutput-i.md#on_metadataObjectsAvailable).

**Inheritance/Implementation:** MetadataCatFaceObject extends [MetadataObject](arkts-camera-camera-metadataobject-i.md#MetadataObject)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface MetadataCatFaceObject--><!--Device-camera-interface MetadataCatFaceObject-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'camera';
```

## leftEyeBoundingBox

```TypeScript
readonly leftEyeBoundingBox: Rect
```

Left eye area.

**Type:** Rect

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataCatFaceObject-readonly leftEyeBoundingBox: Rect--><!--Device-MetadataCatFaceObject-readonly leftEyeBoundingBox: Rect-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## rightEyeBoundingBox

```TypeScript
readonly rightEyeBoundingBox: Rect
```

Right eye area.

**Type:** Rect

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataCatFaceObject-readonly rightEyeBoundingBox: Rect--><!--Device-MetadataCatFaceObject-readonly rightEyeBoundingBox: Rect-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

