# PickerResult

相机选择器的处理结果。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cameraPicker-class PickerResult--><!--Device-cameraPicker-class PickerResult-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { cameraPicker } from 'kits/@kit.CameraKit';
```

## mediaType

```TypeScript
mediaType: PickerMediaType
```

返回的媒体类型。

**Type:** [PickerMediaType](arkts-camera-camerapicker-pickermediatype-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerResult-mediaType: PickerMediaType--><!--Device-PickerResult-mediaType: PickerMediaType-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## resultCode

```TypeScript
resultCode: int
```

处理的结果，成功返回0，失败返回-1。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerResult-resultCode: int--><!--Device-PickerResult-resultCode: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## resultUri

```TypeScript
resultUri: string
```

返回的uri地址。若saveUri为空，resultUri为公共媒体路径。若saveUri不为空且具备写权限，resultUri与saveUri相同。若saveUri不为空且不具备写权限，则无法获取到resultUri。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerResult-resultUri: string--><!--Device-PickerResult-resultUri: string-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

