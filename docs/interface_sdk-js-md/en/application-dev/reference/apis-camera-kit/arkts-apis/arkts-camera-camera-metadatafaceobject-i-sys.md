# MetadataFaceObject (System API)

Face metadata detected by the camera, which is extended from [MetadataObject](arkts-camera-camera-metadataobject-i.md#MetadataObject). It serves as the data source of the camera information in [CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput). It is obtained by calling metadataOutput. [on('metadataObjectsAvailable')](arkts-camera-camera-metadataoutput-i.md#on_metadataObjectsAvailable).

**Inheritance/Implementation:** MetadataFaceObject extends [MetadataObject](arkts-camera-camera-metadataobject-i.md#MetadataObject)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface MetadataFaceObject--><!--Device-camera-interface MetadataFaceObject-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## emotion

```TypeScript
readonly emotion: Emotion
```

Detected emotion.

**Type:** [Emotion](arkts-camera-camera-emotion-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataFaceObject-readonly emotion: Emotion--><!--Device-MetadataFaceObject-readonly emotion: Emotion-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## emotionConfidence

```TypeScript
readonly emotionConfidence: double
```

Emotion detection confidence. The value range is [0, 1].

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataFaceObject-readonly emotionConfidence: double--><!--Device-MetadataFaceObject-readonly emotionConfidence: double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

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

<!--Device-MetadataFaceObject-readonly leftEyeBoundingBox: Rect--><!--Device-MetadataFaceObject-readonly leftEyeBoundingBox: Rect-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## pitchAngle

```TypeScript
readonly pitchAngle: int
```

Pitch angle. The value range is [-90, 90], with the positive direction being downwards.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataFaceObject-readonly pitchAngle: int--><!--Device-MetadataFaceObject-readonly pitchAngle: int-End-->

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

<!--Device-MetadataFaceObject-readonly rightEyeBoundingBox: Rect--><!--Device-MetadataFaceObject-readonly rightEyeBoundingBox: Rect-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## rollAngle

```TypeScript
readonly rollAngle: int
```

Roll angle. The value range is [-180, 180], with the positive direction being clockwise.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataFaceObject-readonly rollAngle: int--><!--Device-MetadataFaceObject-readonly rollAngle: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## yawAngle

```TypeScript
readonly yawAngle: int
```

Yaw angle. The value range is [-90, 90], with the positive direction being rightwards.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataFaceObject-readonly yawAngle: int--><!--Device-MetadataFaceObject-readonly yawAngle: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

