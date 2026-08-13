# MetadataBasicFaceObject (System API)

Basic face metadata detected by the camera, which is extended from [MetadataObject](arkts-camera-camera-metadataobject-i.md#MetadataObject). It serves as the data source of the camera information in [CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput). It is obtained by calling metadataOutput. [on('metadataObjectsAvailable')](arkts-camera-camera-metadataoutput-i.md#on_metadataObjectsAvailable).

**Inheritance/Implementation:** MetadataBasicFaceObject extends [MetadataObject](arkts-camera-camera-metadataobject-i.md#MetadataObject)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface MetadataBasicFaceObject--><!--Device-camera-interface MetadataBasicFaceObject-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## leftEyeBoundingBox

```TypeScript
readonly leftEyeBoundingBox?: Rect
```

Left eye area.

**Type:** Rect

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataBasicFaceObject-readonly leftEyeBoundingBox?: Rect--><!--Device-MetadataBasicFaceObject-readonly leftEyeBoundingBox?: Rect-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## pitchAngle

```TypeScript
readonly pitchAngle?: int
```

Pitch angle. The value range is [-90, 90], with the positive direction being downwards.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataBasicFaceObject-readonly pitchAngle?: int--><!--Device-MetadataBasicFaceObject-readonly pitchAngle?: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## rightEyeBoundingBox

```TypeScript
readonly rightEyeBoundingBox?: Rect
```

Right eye area.

**Type:** Rect

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataBasicFaceObject-readonly rightEyeBoundingBox?: Rect--><!--Device-MetadataBasicFaceObject-readonly rightEyeBoundingBox?: Rect-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## rollAngle

```TypeScript
readonly rollAngle?: int
```

Roll angle. The value range is [-180, 180], with the positive direction being clockwise.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataBasicFaceObject-readonly rollAngle?: int--><!--Device-MetadataBasicFaceObject-readonly rollAngle?: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## yawAngle

```TypeScript
readonly yawAngle?: int
```

Yaw angle. The value range is [-90, 90], with the positive direction being rightwards.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataBasicFaceObject-readonly yawAngle?: int--><!--Device-MetadataBasicFaceObject-readonly yawAngle?: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

