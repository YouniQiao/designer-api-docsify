# AVRecorderProfile

音视频录制配置参数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-interface AVRecorderProfile--><!--Device-unnamed-interface AVRecorderProfile-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## aacProfile

```TypeScript
aacProfile?: AacProfile
```

AAC音频编码器的AAC profile。如果不设置，默认使用AAC_LC profile。

**Type:** [AacProfile](arkts-media-multimedia-media-aacprofile-e.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AVRecorderProfile-aacProfile?: AacProfile--><!--Device-AVRecorderProfile-aacProfile?: AacProfile-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## audioBitrate

```TypeScript
audioBitrate?: int
```

音频编码比特率，单位为bit/s。录制音频时该参数为必填参数。&lt;br&gt;支持的比特率范围：&lt;br&gt;- AAC编码格式范围 [32000 - 500000]。&lt;br&gt;- G.711 μ-law编码格式范围 [64000]。&lt;br&gt;- MP3编码格式范围 [8000, 16000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000,224000, 256000, 320000]。&lt;br&gt;使用MP3编码格式时，采样率和比特率的对应关系如下：&lt;br&gt;- 采样率低于16 kHz时，比特率范围为 [8000 - 64000]。&lt;br&gt;- 采样率在16 kHz至32 kHz之间时，比特率范围为 [8000 - 160000]。&lt;br&gt;- 采样率大于32 kHz时，比特率范围为 [32000 - 320000]。&lt;br&gt;- AMR-NB编码格式范围 [4750, 5150, 5900, 6700, 7400, 7950, 10200, 12200]。&lt;br&gt;- AMR-WB编码格式范围 [6600, 8850, 12650, 14250, 15850, 18250, 19850, 23050, 23850]。&lt;br&gt;**原子化服务API**：从API version 12开始，该接口支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderProfile-audioBitrate?: int--><!--Device-AVRecorderProfile-audioBitrate?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## audioChannels

```TypeScript
audioChannels?: int
```

音频声道数。录制音频时该参数为必填参数。&lt;br&gt;- AAC编码格式范围 [1 - 2]。&lt;br&gt;- G.711 μ-law编码格式范围 [1]。&lt;br&gt;- MP3编码格式范围 [1 - 2]。&lt;br&gt;- AMR-NB和AMR-WB编码格式范围 [1]。&lt;br&gt;**原子化服务API**：从API version 12开始，该接口支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderProfile-audioChannels?: int--><!--Device-AVRecorderProfile-audioChannels?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## audioCodec

```TypeScript
audioCodec?: CodecMimeType
```

音频编码格式。录制音频时该参数为必填参数。当前支持AUDIO_AAC、AUDIO_MP3、AUDIO_G711MU、AUDIO_AMR_NB和AUDIO_AMR_WB。&lt;br&gt;**原子化服务API**：从API version 12开始，该接口支持在原子化服务中使用。

**Type:** [CodecMimeType](arkts-media-multimedia-media-codecmimetype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderProfile-audioCodec?: CodecMimeType--><!--Device-AVRecorderProfile-audioCodec?: CodecMimeType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## audioSampleRate

```TypeScript
audioSampleRate?: int
```

音频采样率，单位为Hz。录制音频时该参数为必填参数。&lt;br&gt;支持的采样率范围：&lt;br&gt;- AAC编码格式范围 [8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000]。&lt;br&gt;- G.711 μ-law编码格式范围 [8000]。&lt;br&gt;- MP3编码格式范围 [8000, 11025, 12000, 16000,22050, 24000, 32000, 44100, 48000]。&lt;br&gt;- AMR-NB编码格式范围 [8000]。&lt;br&gt;- AMR-WB编码格式范围 [16000]。&lt;br&gt;可变比特率。比特率仅供参考。&lt;br&gt;**原子化服务API**：从API version 12开始，该接口支持在原子化服务中使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderProfile-audioSampleRate?: int--><!--Device-AVRecorderProfile-audioSampleRate?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## enableBFrame

```TypeScript
enableBFrame?: boolean
```

是否启用B帧。默认不启用。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-enableBFrame?: boolean--><!--Device-AVRecorderProfile-enableBFrame?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## enableTemporalScale

```TypeScript
enableTemporalScale?: boolean
```

是否支持时域分层编码。录制视频时该参数可选。默认值为**false**。如果设置为**true**，视频输出流中的部分帧可以跳过不编码。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-enableTemporalScale?: boolean--><!--Device-AVRecorderProfile-enableTemporalScale?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## fileFormat

```TypeScript
fileFormat: ContainerFormatType
```

文件的容器格式。此参数为必填参数。当前支持MP4、M4A、MP3、WAV、AMR和AAC容器格式。AUDIO_MP3编码格式不能在MP4容器格式中使用。&lt;br&gt;**原子化服务API**：从API version 12开始，该接口支持在原子化服务中使用。

**Type:** [ContainerFormatType](arkts-media-multimedia-media-containerformattype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderProfile-fileFormat: ContainerFormatType--><!--Device-AVRecorderProfile-fileFormat: ContainerFormatType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## isHdr

```TypeScript
isHdr?: boolean
```

HDR编码。录制视频时该参数可选。默认值为**false**，对编码格式无要求。当**isHdr**设置为**true**时，编码格式必须为**video/hevc**。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-isHdr?: boolean--><!--Device-AVRecorderProfile-isHdr?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## videoBitrate

```TypeScript
videoBitrate?: int
```

视频编码比特率，单位为bit/s。录制视频时该参数为必填参数。取值范围为[10000 - 100000000]。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-videoBitrate?: int--><!--Device-AVRecorderProfile-videoBitrate?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## videoCodec

```TypeScript
videoCodec?: CodecMimeType
```

视频编码格式。录制视频时该参数为必填参数。当前支持VIDEO_AVC和VIDEO_HEVC。

**Type:** [CodecMimeType](arkts-media-multimedia-media-codecmimetype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-videoCodec?: CodecMimeType--><!--Device-AVRecorderProfile-videoCodec?: CodecMimeType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## videoFrameHeight

```TypeScript
videoFrameHeight?: int
```

视频帧高度，单位为像素（px）。录制视频时该参数为必填参数。取值范围为[144 - 4096]。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-videoFrameHeight?: int--><!--Device-AVRecorderProfile-videoFrameHeight?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## videoFrameRate

```TypeScript
videoFrameRate?: int
```

视频帧率，单位为fps。录制视频时该参数为必填参数。取值范围为[1 - 60]。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-videoFrameRate?: int--><!--Device-AVRecorderProfile-videoFrameRate?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## videoFrameWidth

```TypeScript
videoFrameWidth?: int
```

视频帧宽度，单位为像素（px）。录制视频时该参数为必填参数。取值范围为[176 - 4096]。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVRecorderProfile-videoFrameWidth?: int--><!--Device-AVRecorderProfile-videoFrameWidth?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

