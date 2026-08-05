# MetadataBasicFaceObject

Basic face metadata detected by the camera, which is extended from [MetadataObject]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. It serves as the data source of the camera information in [CameraInput]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_. It is obtained by calling metadataOutput. [on('metadataObjectsAvailable')]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_.

**Inheritance/Implementation:** MetadataBasicFaceObject extends [MetadataObject](arkts-camera-camera-metadataobject-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-camera-interface MetadataBasicFaceObject extends MetadataObject--><!--Device-camera-interface MetadataBasicFaceObject extends MetadataObject-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## leftEyeBoundingBox

```TypeScript
readonly leftEyeBoundingBox?: Rect
```

Left eye area.

**Type:** Rect

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataBasicFaceObject-readonly leftEyeBoundingBox?: Rect--><!--Device-MetadataBasicFaceObject-readonly leftEyeBoundingBox?: Rect-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## pitchAngle

```TypeScript
readonly pitchAngle?: int
```

Pitch angle. The value range is [-90, 90], with the positive direction being downwards.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataBasicFaceObject-readonly pitchAngle?: int--><!--Device-MetadataBasicFaceObject-readonly pitchAngle?: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## rightEyeBoundingBox

```TypeScript
readonly rightEyeBoundingBox?: Rect
```

Right eye area.

**Type:** Rect

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataBasicFaceObject-readonly rightEyeBoundingBox?: Rect--><!--Device-MetadataBasicFaceObject-readonly rightEyeBoundingBox?: Rect-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## rollAngle

```TypeScript
readonly rollAngle?: int
```

Roll angle. The value range is [-180, 180], with the positive direction being clockwise.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataBasicFaceObject-readonly rollAngle?: int--><!--Device-MetadataBasicFaceObject-readonly rollAngle?: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## yawAngle

```TypeScript
readonly yawAngle?: int
```

Yaw angle. The value range is [-90, 90], with the positive direction being rightwards.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataBasicFaceObject-readonly yawAngle?: int--><!--Device-MetadataBasicFaceObject-readonly yawAngle?: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

