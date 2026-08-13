# ErrorInfo

Describes the error information.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-export interface ErrorInfo--><!--Device-unnamed-export interface ErrorInfo-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## errorCode

```TypeScript
errorCode: T
```

Error code. The type of **errorCode** is BusinessError.

**Type:** T

**Since:** 23

**Deprecated since:** -1

<!--Device-ErrorInfo-errorCode: T--><!--Device-ErrorInfo-errorCode: T-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## errorType

```TypeScript
errorType?: ErrorType
```

Stage at which the error occurred.

**Type:** [ErrorType](arkts-media-soundpool-errortype-e.md)

**Since:** 23

**Deprecated since:** -1

<!--Device-ErrorInfo-errorType?: ErrorType--><!--Device-ErrorInfo-errorType?: ErrorType-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## soundId

```TypeScript
soundId?: number
```

ID of the resource where the error occurred. It can be obtained by calling **load**.

**Type:** number

**Since:** 23

**Deprecated since:** -1

<!--Device-ErrorInfo-soundId?: int--><!--Device-ErrorInfo-soundId?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## streamId

```TypeScript
streamId?: number
```

ID of the audio stream where the error occurred. It can be obtained by calling **play**.

**Type:** number

**Since:** 23

**Deprecated since:** -1

<!--Device-ErrorInfo-streamId?: int--><!--Device-ErrorInfo-streamId?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool
