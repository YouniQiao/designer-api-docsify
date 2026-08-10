# ErrorInfo

错误信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface ErrorInfo<T extends Error = BusinessError>--><!--Device-unnamed-export interface ErrorInfo<T extends Error = BusinessError>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## errorCode

```TypeScript
errorCode: T
```

错误码。errorCode的类型T为[BusinessError](../../../reference/apis-basic-services-kit/js-apis-base.md)类型。

**Type:** T

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ErrorInfo-errorCode: T--><!--Device-ErrorInfo-errorCode: T-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## errorType

```TypeScript
errorType?: ErrorType
```

表示错误发生阶段。

**Type:** [ErrorType](arkts-media-soundpool-errortype-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ErrorInfo-errorType?: ErrorType--><!--Device-ErrorInfo-errorType?: ErrorType-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## soundId

```TypeScript
soundId?: int
```

发生错误的资源ID，load方法能够获取soundId。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ErrorInfo-soundId?: int--><!--Device-ErrorInfo-soundId?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## streamId

```TypeScript
streamId?: int
```

发生错误的音频流ID，play方法能够获取streamId。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ErrorInfo-streamId?: int--><!--Device-ErrorInfo-streamId?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

