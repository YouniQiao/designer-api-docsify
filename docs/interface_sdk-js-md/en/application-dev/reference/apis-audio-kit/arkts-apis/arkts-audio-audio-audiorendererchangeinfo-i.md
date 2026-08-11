# AudioRendererChangeInfo

Describes the audio renderer change event.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioRendererChangeInfo--><!--Device-audio-interface AudioRendererChangeInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## deviceDescriptors

```TypeScript
readonly deviceDescriptors: AudioDeviceDescriptors
```

Audio device description.

**Type:** [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioRendererChangeInfo-readonly deviceDescriptors: AudioDeviceDescriptors--><!--Device-AudioRendererChangeInfo-readonly deviceDescriptors: AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## rendererInfo

```TypeScript
readonly rendererInfo: AudioRendererInfo
```

Audio renderer information.

**Type:** [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioRendererChangeInfo-readonly rendererInfo: AudioRendererInfo--><!--Device-AudioRendererChangeInfo-readonly rendererInfo: AudioRendererInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## streamId

```TypeScript
readonly streamId: int
```

Unique ID of an audio stream.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioRendererChangeInfo-readonly streamId: int--><!--Device-AudioRendererChangeInfo-readonly streamId: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

