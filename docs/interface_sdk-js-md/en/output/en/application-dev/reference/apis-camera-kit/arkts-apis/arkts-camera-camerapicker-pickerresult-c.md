# PickerResult

Defines the processing result of the camera picker.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cameraPicker-class PickerResult--><!--Device-cameraPicker-class PickerResult-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## mediaType

```TypeScript
mediaType: PickerMediaType
```

Media type.

**Type:** PickerMediaType

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerResult-mediaType: PickerMediaType--><!--Device-PickerResult-mediaType: PickerMediaType-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## resultCode

```TypeScript
resultCode: int
```

Result code. The value **0** means that the processing is successful, and **-1** means that the processing fails.

**Type:** int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerResult-resultCode: int--><!--Device-PickerResult-resultCode: int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## resultUri

```TypeScript
resultUri: string
```

URI of the result. If **saveUri** is empty, **resultUri** is a public media path. If **saveUri** is not empty and the application has the write permission on the URI, the value of **resultUri** is the same as that of **saveUri**. If **saveUri** is not empty and the application does not have the write permission on the URI, **resultUri** cannot be obtained.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PickerResult-resultUri: string--><!--Device-PickerResult-resultUri: string-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

