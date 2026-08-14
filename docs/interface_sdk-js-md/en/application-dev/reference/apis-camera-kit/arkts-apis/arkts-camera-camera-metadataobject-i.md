# MetadataObject

Describes the camera metadata, which is the data source of [CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput). The metadata is obtained through **metadataOutput.on('metadataObjectsAvailable')**.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface MetadataObject--><!--Device-camera-interface MetadataObject-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'camera';
```

## boundingBox

```TypeScript
readonly boundingBox: Rect
```

Metadata rectangle.

**Type:** Rect

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataObject-readonly boundingBox: Rect--><!--Device-MetadataObject-readonly boundingBox: Rect-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## isLockFocusTracked

```TypeScript
readonly isLockFocusTracked?: boolean
```

Whether the focus is locked and being tracked currently.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataObject-readonly isLockFocusTracked?: boolean--><!--Device-MetadataObject-readonly isLockFocusTracked?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## timestamp

```TypeScript
readonly timestamp: int
```

Timestamp, in ns.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataObject-readonly timestamp: int--><!--Device-MetadataObject-readonly timestamp: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## type

```TypeScript
readonly type: MetadataObjectType
```

Metadata object type.

**Type:** [MetadataObjectType](arkts-camera-camera-metadataobjecttype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataObject-readonly type: MetadataObjectType--><!--Device-MetadataObject-readonly type: MetadataObjectType-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

