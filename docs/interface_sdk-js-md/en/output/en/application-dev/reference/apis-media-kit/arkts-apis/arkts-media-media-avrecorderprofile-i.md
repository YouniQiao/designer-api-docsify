# AVRecorderProfile

Describes the audio and video recording profile.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-media-interface AVRecorderProfile--><!--Device-media-interface AVRecorderProfile-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## aacProfile

```TypeScript
aacProfile?: AacProfile
```

AAC profile for AAC audio encoder. If not set, use AAC\_LC profile as default.

**Type:** AacProfile

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVRecorderProfile-aacProfile?: AacProfile--><!--Device-AVRecorderProfile-aacProfile?: AacProfile-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## audioBitrate

```TypeScript
audioBitrate?: int
```

Audio encoding bit rate, in bit/s. This parameter is mandatory for audio recording.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Supported bit rate ranges: \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- Range [32000 - 500000] for the AAC encoding format.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_- Range [64000] for the G.711 μ-law encoding format. \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_- Range [8000, 16000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 320000] for the MP3 encoding format.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_When the MP3 encoding format is used, the mapping between the sampling rate and bit rate is as follows:\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_- When the sampling rate is lower than 16 kHZ, the bit rate range is [8000 - 64000].\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_- When the sampling rate ranges from 16 kHz to 32 kHz, the bit rate range is [8000 - 160000].\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_- When the sampling rate is greater than 32 kHz, the bit rate range is [32000 - 320000].\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_- Range [4750, 5150, 5900, 6700, 7400, 7950, 10200, 12200] for the AMR-NB encoding format.\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_- Range [6600, 8850, 12650, 14250, 15850, 18250, 19850, 23050, 23850] for the AMR-WB encoding format.\_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_**Atomic service API**: This API can be used in atomic services since API version 12.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderProfile-audioBitrate?: int--><!--Device-AVRecorderProfile-audioBitrate?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## audioChannels

```TypeScript
audioChannels?: int
```

Number of audio channels. This parameter is mandatory for audio recording.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_- Range [1 - 2] for the AAC encoding format.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- Range [1] for the G.711 μ-law encoding format.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_- Range [1 - 2] for the MP3 encoding format.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_- Range [1] for the AMR-NB and AMR-WB encoding formats.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_**Atomic service API**: This API can be used in atomic services since API version 12.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderProfile-audioChannels?: int--><!--Device-AVRecorderProfile-audioChannels?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## audioCodec

```TypeScript
audioCodec?: CodecMimeType
```

Audio encoding format. This parameter is mandatory for audio recording. Currently, AUDIO\_AAC, AUDIO\_MP3, AUDIO\_G711MU, AUDIO\_AMR\_NB, and AUDIO\_AMR\_WB are supported.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**Atomic service API**: This API can be used in atomic services since API version 12.

**Type:** CodecMimeType

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderProfile-audioCodec?: CodecMimeType--><!--Device-AVRecorderProfile-audioCodec?: CodecMimeType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## audioSampleRate

```TypeScript
audioSampleRate?: int
```

Audio sampling rate, in Hz. This parameter is mandatory for audio recording.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Supported sampling rate ranges: \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- Range [8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000] for the AAC encoding format.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_- Range [8000] for the G.711 μ-law encoding format.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_- Range [8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000] for the MP3 encoding format.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_- Range [8000] for the AMR-NB encoding format. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_- Range [16000] for the AMR-WB encoding format.\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_Variable bit rate. The bit rate is for reference only. \_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_**Atomic service API**: This API can be used in atomic services since API version 12.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderProfile-audioSampleRate?: int--><!--Device-AVRecorderProfile-audioSampleRate?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## enableBFrame

```TypeScript
enableBFrame?: boolean
```

Indicates whether enable B Frame. Default is disabled.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-enableBFrame?: boolean--><!--Device-AVRecorderProfile-enableBFrame?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## enableTemporalScale

```TypeScript
enableTemporalScale?: boolean
```

Whether temporal layered encoding is supported. This parameter is optional for video recording. The default value is **false**. If this parameter is set to **true**, some frames in the video output streams can be skipped without being encoded.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-enableTemporalScale?: boolean--><!--Device-AVRecorderProfile-enableTemporalScale?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## fileFormat

```TypeScript
fileFormat: ContainerFormatType
```

Container format of a file. This parameter is mandatory. Currently, the MP4, M4A, MP3, WAV, AMR, and AAC container formats are supported. The AUDIO\_MP3 encoding format cannot be used in the MP4 container format. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**Atomic service API**: This API can be used in atomic services since API version 12.

**Type:** ContainerFormatType

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderProfile-fileFormat: ContainerFormatType--><!--Device-AVRecorderProfile-fileFormat: ContainerFormatType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## isHdr

```TypeScript
isHdr?: boolean
```

HDR encoding. This parameter is optional for video recording. The default value is **false**, and there is no requirement on the encoding format. When **isHdr** is set to **true**, the encoding format must be **video/hevc**.

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-isHdr?: boolean--><!--Device-AVRecorderProfile-isHdr?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## videoBitrate

```TypeScript
videoBitrate?: int
```

Video encoding bit rate, in bit/s. This parameter is mandatory for video recording. The value range is [10000 - 100000000], in bit/s.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-videoBitrate?: int--><!--Device-AVRecorderProfile-videoBitrate?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## videoCodec

```TypeScript
videoCodec?: CodecMimeType
```

Video encoding format. This parameter is mandatory for video recording. Currently, VIDEO\_AVC and VIDEO\_HEVC is supported.

**Type:** CodecMimeType

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-videoCodec?: CodecMimeType--><!--Device-AVRecorderProfile-videoCodec?: CodecMimeType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## videoFrameHeight

```TypeScript
videoFrameHeight?: int
```

Height of a video frame, in px. This parameter is mandatory for video recording. The value range is [144 - 4096].

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-videoFrameHeight?: int--><!--Device-AVRecorderProfile-videoFrameHeight?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## videoFrameRate

```TypeScript
videoFrameRate?: int
```

Video frame rate, in fps. This parameter is mandatory for video recording. The value range is [1 - 60].

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-videoFrameRate?: int--><!--Device-AVRecorderProfile-videoFrameRate?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## videoFrameWidth

```TypeScript
videoFrameWidth?: int
```

Width of a video frame, in px. This parameter is mandatory for video recording. The value range is [176 - 4096].

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-videoFrameWidth?: int--><!--Device-AVRecorderProfile-videoFrameWidth?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

