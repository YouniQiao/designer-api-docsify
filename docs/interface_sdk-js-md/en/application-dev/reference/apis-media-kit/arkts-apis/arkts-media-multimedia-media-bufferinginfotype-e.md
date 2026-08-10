# BufferingInfoType

缓存事件类型枚举。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-enum BufferingInfoType--><!--Device-unnamed-enum BufferingInfoType-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## BUFFERING_START

```TypeScript
BUFFERING_START = 1
```

表示开始缓冲。当上报BUFFERING_START时，播放器会暂停播放。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BufferingInfoType-BUFFERING_START = 1--><!--Device-BufferingInfoType-BUFFERING_START = 1-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## BUFFERING_END

```TypeScript
BUFFERING_END = 2
```

表示结束缓冲。当上报BUFFERING_END时，播放器会恢复播放。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BufferingInfoType-BUFFERING_END = 2--><!--Device-BufferingInfoType-BUFFERING_END = 2-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## BUFFERING_PERCENT

```TypeScript
BUFFERING_PERCENT = 3
```

表示缓冲百分比。可参考该事件感知缓冲进度。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BufferingInfoType-BUFFERING_PERCENT = 3--><!--Device-BufferingInfoType-BUFFERING_PERCENT = 3-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## CACHED_DURATION

```TypeScript
CACHED_DURATION = 4
```

表示已缓冲数据预估可播放时长，单位为毫秒（ms）。缓冲区中的数据变化量大于500ms，上报一次。可参考该事件做进度条。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BufferingInfoType-CACHED_DURATION = 4--><!--Device-BufferingInfoType-CACHED_DURATION = 4-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

