# MetadataFaceObject

Face metadata detected by the camera, which is extended from [MetadataObject](arkts-camera-camera-metadataobject-i.md). It serves as the data source of the camera information in [CameraInput](arkts-camera-camera-camerainput-i.md). It is obtained by calling metadataOutput.  
[on('metadataObjectsAvailable')](camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback&lt;Array<MetadataObject>&gt;&lt;MetadataObject&gt;>)).

**Inheritance/Implementation:** MetadataFaceObject extends [MetadataObject](arkts-camera-camera-metadataobject-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-camera-interface MetadataFaceObject extends MetadataObject--><!--Device-camera-interface MetadataFaceObject extends MetadataObject-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## emotion

```TypeScript
readonly emotion: Emotion
```

Detected emotion.

**Type:** [Emotion](arkts-camera-camera-emotion-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataFaceObject-readonly emotion: Emotion--><!--Device-MetadataFaceObject-readonly emotion: Emotion-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## emotionConfidence

```TypeScript
readonly emotionConfidence: double
```

Emotion detection confidence. The value range is [0, 1].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataFaceObject-readonly emotionConfidence: double--><!--Device-MetadataFaceObject-readonly emotionConfidence: double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## leftEyeBoundingBox

```TypeScript
readonly leftEyeBoundingBox: Rect
```

Left eye area.

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataFaceObject-readonly leftEyeBoundingBox: Rect--><!--Device-MetadataFaceObject-readonly leftEyeBoundingBox: Rect-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## pitchAngle

```TypeScript
readonly pitchAngle: int
```

Pitch angle. The value range is [-90, 90], with the positive direction being downwards.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataFaceObject-readonly pitchAngle: int--><!--Device-MetadataFaceObject-readonly pitchAngle: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## rightEyeBoundingBox

```TypeScript
readonly rightEyeBoundingBox: Rect
```

Right eye area.

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataFaceObject-readonly rightEyeBoundingBox: Rect--><!--Device-MetadataFaceObject-readonly rightEyeBoundingBox: Rect-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## rollAngle

```TypeScript
readonly rollAngle: int
```

Roll angle. The value range is [-180, 180], with the positive direction being clockwise.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataFaceObject-readonly rollAngle: int--><!--Device-MetadataFaceObject-readonly rollAngle: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## yawAngle

```TypeScript
readonly yawAngle: int
```

Yaw angle. The value range is [-90, 90], with the positive direction being rightwards.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataFaceObject-readonly yawAngle: int--><!--Device-MetadataFaceObject-readonly yawAngle: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

