# AudioRecorderConfig

音频录制配置定义。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVRecorderConfig

<!--Device-unnamed-interface AudioRecorderConfig--><!--Device-unnamed-interface AudioRecorderConfig-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## audioEncodeBitRate

```TypeScript
audioEncodeBitRate?: number
```

音频编码比特率，单位为bit/s。

**Type:** number

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVRecorderProfile#audioBitrate

<!--Device-AudioRecorderConfig-audioEncodeBitRate?: number--><!--Device-AudioRecorderConfig-audioEncodeBitRate?: number-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## audioEncoder

```TypeScript
audioEncoder?: AudioEncoder
```

音频编码格式。默认值为DEFAULT，API8之后将废弃。请使用"audioEncoderMime"替代。

**Type:** [AudioEncoder](arkts-media-multimedia-media-audioencoder-e.md)

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.multimedia.media/media.AudioRecorderConfig.audioEncoderMime

<!--Device-AudioRecorderConfig-audioEncoder?: AudioEncoder--><!--Device-AudioRecorderConfig-audioEncoder?: AudioEncoder-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## audioEncoderMime

```TypeScript
audioEncoderMime?: CodecMimeType
```

音频编码格式MIME。用于替代audioEncoder。

**Type:** [CodecMimeType](arkts-media-multimedia-media-codecmimetype-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVRecorderProfile#audioCodec

<!--Device-AudioRecorderConfig-audioEncoderMime?: CodecMimeType--><!--Device-AudioRecorderConfig-audioEncoderMime?: CodecMimeType-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## audioSampleRate

```TypeScript
audioSampleRate?: number
```

音频采样率，单位为Hz。

**Type:** number

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVRecorderProfile#audioSampleRate

<!--Device-AudioRecorderConfig-audioSampleRate?: number--><!--Device-AudioRecorderConfig-audioSampleRate?: number-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## fileFormat

```TypeScript
fileFormat?: ContainerFormatType
```

输出文件格式，详见ContainerFormatType。用于替代"format"。

**Type:** [ContainerFormatType](arkts-media-multimedia-media-containerformattype-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVRecorderProfile#fileFormat

<!--Device-AudioRecorderConfig-fileFormat?: ContainerFormatType--><!--Device-AudioRecorderConfig-fileFormat?: ContainerFormatType-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## format

```TypeScript
format?: AudioOutputFormat
```

音频输出格式。默认值为DEFAULT。API8之后废弃，使用"fileFormat"替代。

**Type:** [AudioOutputFormat](arkts-media-multimedia-media-audiooutputformat-e.md)

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.multimedia.media/media.AudioRecorderConfig.fileFormat

<!--Device-AudioRecorderConfig-format?: AudioOutputFormat--><!--Device-AudioRecorderConfig-format?: AudioOutputFormat-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## location

```TypeScript
location?: Location
```

地理位置信息。

**Type:** [Location](../../apis-location-kit/arkts-apis/arkts-location-geolocationmanager-location-i.md)

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVMetadata#location

<!--Device-AudioRecorderConfig-location?: Location--><!--Device-AudioRecorderConfig-location?: Location-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## numberOfChannels

```TypeScript
numberOfChannels?: number
```

音频声道数。

**Type:** number

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVRecorderProfile#audioChannels

<!--Device-AudioRecorderConfig-numberOfChannels?: number--><!--Device-AudioRecorderConfig-numberOfChannels?: number-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## uri

```TypeScript
uri: string
```

音频输出URI。支持两种URI格式。格式：scheme + "://" + "context"。file格式：file://path fd格式：fd://fd

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.media/media.AVRecorderConfig#url

<!--Device-AudioRecorderConfig-uri: string--><!--Device-AudioRecorderConfig-uri: string-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

