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

## boundingBox

```TypeScript
readonly boundingBox: Rect
```

metadata 区域框。

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataObject-readonly boundingBox: Rect--><!--Device-MetadataObject-readonly boundingBox: Rect-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## isLockFocusTracked

```TypeScript
readonly isLockFocusTracked?: boolean
```

是否已锁定焦点跟踪。true表示已锁定，false表示未锁定。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MetadataObject-readonly isLockFocusTracked?: boolean--><!--Device-MetadataObject-readonly isLockFocusTracked?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## timestamp

```TypeScript
readonly timestamp: int
```

当前时间戳。单位为纳秒（ns）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataObject-readonly timestamp: int--><!--Device-MetadataObject-readonly timestamp: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## type

```TypeScript
readonly type: MetadataObjectType
```

metadata 类型。

**Type:** [MetadataObjectType](arkts-camera-camera-metadataobjecttype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-MetadataObject-readonly type: MetadataObjectType--><!--Device-MetadataObject-readonly type: MetadataObjectType-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

