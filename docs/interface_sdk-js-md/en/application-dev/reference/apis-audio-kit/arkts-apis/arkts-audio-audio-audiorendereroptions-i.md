# AudioRendererOptions

```TypeScript
interface AudioRendererOptions
```

Describes audio renderer configurations.

**Since:** 8

<!--Device-audio-interface AudioRendererOptions--><!--Device-audio-interface AudioRendererOptions-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## keepActiveOnSilence

```TypeScript
keepActiveOnSilence?: boolean
```

Indicates whether to keep the audio path active during silent playback. By default, when silent data is played, including zero-volume audio or input of silent data, the system stops the audio path and hardware upon detection to save power. The audio path is restored immediately when non-silent audio data resumes. However, this restoration incurs a short delay. To keep the audio path active during silent playback to ensure a fixed data output timing, you can disable this behavior using this API. This setting is valid only when the audio playback stream is running. The default value is **false**.

**Type:** boolean

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioRendererOptions-keepActiveOnSilence?: boolean--><!--Device-AudioRendererOptions-keepActiveOnSilence?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## offloadAllowed

```TypeScript
offloadAllowed?: boolean
```

Indicates whether the low-power mode is allowed. When the audio playback scenario is music or book listening, the system uses the low-power mode to play the audio by default, which reduces power consumption when the audio is played in the background. However, in low power consumption mode, a large amount of data is buffered in the audio system. Therefore, this mode is not applicable to scenarios where audio data is generated in real time. In this case, developers can set this mode not to be used. Default value: true.

**Type:** boolean

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioRendererOptions-offloadAllowed?: boolean--><!--Device-AudioRendererOptions-offloadAllowed?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## privacyType

```TypeScript
privacyType?: AudioPrivacyType
```

Whether the audio stream can be recorded by other applications. The default value is **0**.

**Type:** [AudioPrivacyType](arkts-audio-audio-audioprivacytype-e.md)

**Since:** 10

<!--Device-AudioRendererOptions-privacyType?: AudioPrivacyType--><!--Device-AudioRendererOptions-privacyType?: AudioPrivacyType-End-->

**System capability:** SystemCapability.Multimedia.Audio.PlaybackCapture

## rendererInfo

```TypeScript
rendererInfo: AudioRendererInfo
```

Describes audio renderer information.

**Type:** [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md)

**Since:** 8

<!--Device-AudioRendererOptions-rendererInfo: AudioRendererInfo--><!--Device-AudioRendererOptions-rendererInfo: AudioRendererInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## streamInfo

```TypeScript
streamInfo: AudioStreamInfo
```

Describes audio stream information.

**Type:** [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)

**Since:** 8

<!--Device-AudioRendererOptions-streamInfo: AudioStreamInfo--><!--Device-AudioRendererOptions-streamInfo: AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer
