# AudioRendererOptions

音频渲染器选项信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioRendererOptions--><!--Device-audio-interface AudioRendererOptions-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## privacyType

```TypeScript
privacyType?: AudioPrivacyType
```

表示音频流是否可以被其他应用录制，默认值为0。

**Type:** [AudioPrivacyType](arkts-audio-audio-audioprivacytype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AudioRendererOptions-privacyType?: AudioPrivacyType--><!--Device-AudioRendererOptions-privacyType?: AudioPrivacyType-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## rendererInfo

```TypeScript
rendererInfo: AudioRendererInfo
```

音频渲染器信息。

**Type:** [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AudioRendererOptions-rendererInfo: AudioRendererInfo--><!--Device-AudioRendererOptions-rendererInfo: AudioRendererInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## streamInfo

```TypeScript
streamInfo: AudioStreamInfo
```

音频流信息。

**Type:** [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AudioRendererOptions-streamInfo: AudioStreamInfo--><!--Device-AudioRendererOptions-streamInfo: AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

