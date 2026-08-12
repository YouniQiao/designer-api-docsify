# AudioRendererChangeInfo

Describes the audio renderer change event.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioRendererChangeInfo--><!--Device-audio-interface AudioRendererChangeInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## clientUid

```TypeScript
readonly clientUid: int
```

Uid for audio renderer client application.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioRendererChangeInfo-readonly clientUid: int--><!--Device-AudioRendererChangeInfo-readonly clientUid: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

## rendererState

```TypeScript
readonly rendererState: AudioState
```

Audio state.

**Type:** AudioState

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioRendererChangeInfo-readonly rendererState: AudioState--><!--Device-AudioRendererChangeInfo-readonly rendererState: AudioState-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**System API:** This is a system API.

