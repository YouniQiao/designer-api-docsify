# AudioRecorderConfig

Provides the audio recorder configuration definitions.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [AVRecorderConfig](arkts-media-media-avrecorderconfig-i.md#AVRecorderConfig)

<!--Device-media-interface AudioRecorderConfig--><!--Device-media-interface AudioRecorderConfig-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## audioEncodeBitRate

```TypeScript
audioEncodeBitRate?: number
```

Audio encoding bit rate, in bit/s.

**Type:** number

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [audioBitrate](ohos.multimedia.media/media.AVRecorderProfile#audioBitrate)

<!--Device-AudioRecorderConfig-audioEncodeBitRate?: number--><!--Device-AudioRecorderConfig-audioEncodeBitRate?: number-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## audioEncoder

```TypeScript
audioEncoder?: AudioEncoder
```

Audio encoding format. The default value is DEFAULT, it will be deprecated after API8.use "audioEncoderMime" instead.

**Type:** [AudioEncoder](arkts-media-media-audioencoder-e.md)

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [audioEncoderMime](#audioEncoderMime)

<!--Device-AudioRecorderConfig-audioEncoder?: AudioEncoder--><!--Device-AudioRecorderConfig-audioEncoder?: AudioEncoder-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## audioEncoderMime

```TypeScript
audioEncoderMime?: CodecMimeType
```

audio encoding format MIME. it used to replace audioEncoder.

**Type:** [CodecMimeType](arkts-media-media-codecmimetype-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [audioCodec](ohos.multimedia.media/media.AVRecorderProfile#audioCodec)

<!--Device-AudioRecorderConfig-audioEncoderMime?: CodecMimeType--><!--Device-AudioRecorderConfig-audioEncoderMime?: CodecMimeType-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## audioSampleRate

```TypeScript
audioSampleRate?: number
```

Audio sampling rate, in Hz.

**Type:** number

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [audioSampleRate](ohos.multimedia.media/media.AVRecorderProfile#audioSampleRate)

<!--Device-AudioRecorderConfig-audioSampleRate?: number--><!--Device-AudioRecorderConfig-audioSampleRate?: number-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## fileFormat

```TypeScript
fileFormat?: ContainerFormatType
```

output file format. see @ContainerFormatType , it used to replace "format".

**Type:** [ContainerFormatType](arkts-media-media-containerformattype-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [fileFormat](ohos.multimedia.media/media.AVRecorderProfile#fileFormat)

<!--Device-AudioRecorderConfig-fileFormat?: ContainerFormatType--><!--Device-AudioRecorderConfig-fileFormat?: ContainerFormatType-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## format

```TypeScript
format?: AudioOutputFormat
```

Audio output format. The default value is DEFAULT, it will be deprecated after API8.it will be replaced with "fileFormat".

**Type:** [AudioOutputFormat](arkts-media-media-audiooutputformat-e.md)

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [fileFormat](ohos.multimedia.media/media.AudioRecorderConfig.fileFormat)

<!--Device-AudioRecorderConfig-format?: AudioOutputFormat--><!--Device-AudioRecorderConfig-format?: AudioOutputFormat-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## location

```TypeScript
location?: Location
```

Geographical location information.

**Type:** Location

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [location](ohos.multimedia.media/media.AVMetadata#location)

<!--Device-AudioRecorderConfig-location?: Location--><!--Device-AudioRecorderConfig-location?: Location-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## numberOfChannels

```TypeScript
numberOfChannels?: number
```

Number of audio channels.

**Type:** number

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [audioChannels](ohos.multimedia.media/media.AVRecorderProfile#audioChannels)

<!--Device-AudioRecorderConfig-numberOfChannels?: number--><!--Device-AudioRecorderConfig-numberOfChannels?: number-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## uri

```TypeScript
uri: string
```

Audio output uri.support two kind of uri now.format like: scheme + "://" + "context".file: file://path fd: fd://fd

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [url](ohos.multimedia.media/media.AVRecorderConfig#url)

<!--Device-AudioRecorderConfig-uri: string--><!--Device-AudioRecorderConfig-uri: string-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

