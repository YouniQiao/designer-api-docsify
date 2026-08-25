# ErrorInfo

Describes the error information.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## errorCode

```TypeScript
errorCode: T
```

Error code. The type of **errorCode** is [BusinessError](../../../reference/apis-basic-services-kit/js-apis-base.md).

**Type:** T

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## errorType

```TypeScript
errorType?: ErrorType
```

Stage at which the error occurred.

**Type:** [ErrorType](arkts-media-soundpool-errortype-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## soundId

```TypeScript
soundId?: int
```

ID of the resource where the error occurred. It can be obtained by calling **load**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## streamId

```TypeScript
streamId?: int
```

ID of the audio stream where the error occurred. It can be obtained by calling **play**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Media.SoundPool
