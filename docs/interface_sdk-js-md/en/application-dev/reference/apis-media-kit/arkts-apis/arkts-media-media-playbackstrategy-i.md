# PlaybackStrategy

Provides preferred playback settings for player.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-media-interface PlaybackStrategy--><!--Device-media-interface PlaybackStrategy-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## enableSuperResolution

```TypeScript
enableSuperResolution?: boolean
```

Enable super-resolution feature. default is false.Must enable super-resolution feature before calling \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ and \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PlaybackStrategy-enableSuperResolution?: boolean--><!--Device-PlaybackStrategy-enableSuperResolution?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## keepDecodingOnMute

```TypeScript
keepDecodingOnMute?: boolean
```

Indicates whether to keep the decoder working when closing the media,which is used to facilitate quick opening of the media. Currently only supports video

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PlaybackStrategy-keepDecodingOnMute?: boolean--><!--Device-PlaybackStrategy-keepDecodingOnMute?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## mutedMediaType

```TypeScript
mutedMediaType?: MediaType
```

mute the specified media stream when playing.

**Type:** MediaType

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PlaybackStrategy-mutedMediaType?: MediaType--><!--Device-PlaybackStrategy-mutedMediaType?: MediaType-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## preferredAudioLanguage

```TypeScript
preferredAudioLanguage?: string
```

Audio language.

**Type:** string

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-PlaybackStrategy-preferredAudioLanguage?: string--><!--Device-PlaybackStrategy-preferredAudioLanguage?: string-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## preferredBufferDuration

```TypeScript
preferredBufferDuration?: int
```

Chooses a preferred buffer duration.

\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_The preferred buffer duration in the playback policy, is used to set the buffer size. For details,see [Online Video Frame Freezing Optimization Practice]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_

**Type:** int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PlaybackStrategy-preferredBufferDuration?: int--><!--Device-PlaybackStrategy-preferredBufferDuration?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## preferredBufferDurationForPlaying

```TypeScript
preferredBufferDurationForPlaying?: double
```

Customize the buffering threshold for start or restart playing. The unit is second.

**Type:** double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PlaybackStrategy-preferredBufferDurationForPlaying?: double--><!--Device-PlaybackStrategy-preferredBufferDurationForPlaying?: double-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## preferredHdr

```TypeScript
preferredHdr?: boolean
```

If true, the player should choose HDR stream if exist.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PlaybackStrategy-preferredHdr?: boolean--><!--Device-PlaybackStrategy-preferredHdr?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## preferredHeight

```TypeScript
preferredHeight?: int
```

Choose a stream with height close to it.

**Type:** int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PlaybackStrategy-preferredHeight?: int--><!--Device-PlaybackStrategy-preferredHeight?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## preferredSubtitleLanguage

```TypeScript
preferredSubtitleLanguage?: string
```

Subtitle language.

**Type:** string

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-PlaybackStrategy-preferredSubtitleLanguage?: string--><!--Device-PlaybackStrategy-preferredSubtitleLanguage?: string-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## preferredWidth

```TypeScript
preferredWidth?: int
```

Choose a stream with width close to it.

**Type:** int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PlaybackStrategy-preferredWidth?: int--><!--Device-PlaybackStrategy-preferredWidth?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## showFirstFrameOnPrepare

```TypeScript
showFirstFrameOnPrepare?: boolean
```

Show first frame on prepare.

**Type:** boolean

**Since:** 17

**ArkTS mode:** ArkTS-Dyn since version 17; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-PlaybackStrategy-showFirstFrameOnPrepare?: boolean--><!--Device-PlaybackStrategy-showFirstFrameOnPrepare?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## thresholdForAutoQuickPlay

```TypeScript
thresholdForAutoQuickPlay?: double
```

set max buffering threshold for liveStreaming or avplayer while change the speed, in s.It is recommended that the value be 2 seconds greater than the starting waterline.

**Type:** double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PlaybackStrategy-thresholdForAutoQuickPlay?: double--><!--Device-PlaybackStrategy-thresholdForAutoQuickPlay?: double-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

