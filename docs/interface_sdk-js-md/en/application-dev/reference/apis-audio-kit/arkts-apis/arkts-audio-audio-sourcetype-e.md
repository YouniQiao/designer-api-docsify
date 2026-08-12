# SourceType

Enumerates the types of audio streams captured.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-audio-enum SourceType--><!--Device-audio-enum SourceType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_INVALID

```TypeScript
SOURCE_TYPE_INVALID = -1
```

Invalid audio source.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_INVALID = -1--><!--Device-SourceType-SOURCE_TYPE_INVALID = -1-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_MIC

```TypeScript
SOURCE_TYPE_MIC = 0
```

Mic source.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_MIC = 0--><!--Device-SourceType-SOURCE_TYPE_MIC = 0-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_VOICE_RECOGNITION

```TypeScript
SOURCE_TYPE_VOICE_RECOGNITION = 1
```

Voice recognition source.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_VOICE_RECOGNITION = 1--><!--Device-SourceType-SOURCE_TYPE_VOICE_RECOGNITION = 1-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_PLAYBACK_CAPTURE

```TypeScript
SOURCE_TYPE_PLAYBACK_CAPTURE = 2
```

Playback capture source type.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 12

**Substitutes:** [OH_AVScreenCapture](OH_AVScreenCapture)

<!--Device-SourceType-SOURCE_TYPE_PLAYBACK_CAPTURE = 2--><!--Device-SourceType-SOURCE_TYPE_PLAYBACK_CAPTURE = 2-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## SOURCE_TYPE_VOICE_COMMUNICATION

```TypeScript
SOURCE_TYPE_VOICE_COMMUNICATION = 7
```

Voice communication source. (The 3A algorithm is not enabled if recording is started independently. It is enabled when the AudioRenderer of the [STREAM_USAGE_VOICE_COMMUNICATION](arkts-audio-audio-streamusage-e.md#StreamUsage) or  
[STREAM_USAGE_VIDEO_COMMUNICATION](arkts-audio-audio-streamusage-e.md#StreamUsage) type is also used to start playback.)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_VOICE_COMMUNICATION = 7--><!--Device-SourceType-SOURCE_TYPE_VOICE_COMMUNICATION = 7-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_VOICE_MESSAGE

```TypeScript
SOURCE_TYPE_VOICE_MESSAGE = 10
```

Voice message source.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_VOICE_MESSAGE = 10--><!--Device-SourceType-SOURCE_TYPE_VOICE_MESSAGE = 10-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_CAMCORDER

```TypeScript
SOURCE_TYPE_CAMCORDER = 13
```

Camcorder source type.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_CAMCORDER = 13--><!--Device-SourceType-SOURCE_TYPE_CAMCORDER = 13-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_UNPROCESSED

```TypeScript
SOURCE_TYPE_UNPROCESSED = 14
```

Unprocessed source type.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_UNPROCESSED = 14--><!--Device-SourceType-SOURCE_TYPE_UNPROCESSED = 14-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## SOURCE_TYPE_LIVE

```TypeScript
SOURCE_TYPE_LIVE = 17
```

Live broadcast source type.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-SourceType-SOURCE_TYPE_LIVE = 17--><!--Device-SourceType-SOURCE_TYPE_LIVE = 17-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

