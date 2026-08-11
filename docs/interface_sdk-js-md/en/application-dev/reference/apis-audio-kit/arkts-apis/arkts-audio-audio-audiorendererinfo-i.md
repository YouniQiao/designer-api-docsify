# AudioRendererInfo

Describes audio renderer information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioRendererInfo--><!--Device-audio-interface AudioRendererInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## content

```TypeScript
content?: ContentType
```

Audio content type.

**Type:** [ContentType](../../apis-arkui/arkts-components/arkts-arkui-contenttype-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 10

**Substitutes:** ohos.multimedia.audio.AudioRendererInfo#usage

<!--Device-AudioRendererInfo-content?: ContentType--><!--Device-AudioRendererInfo-content?: ContentType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## rendererFlags

```TypeScript
rendererFlags: int
```

Flags that control the renderer behavior.

Set this parameter to **0**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioRendererInfo-rendererFlags: int--><!--Device-AudioRendererInfo-rendererFlags: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## usage

```TypeScript
usage: StreamUsage
```

Audio stream usage.

**Type:** [StreamUsage](arkts-audio-audio-streamusage-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioRendererInfo-usage: StreamUsage--><!--Device-AudioRendererInfo-usage: StreamUsage-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## volumeMode

```TypeScript
volumeMode?: AudioVolumeMode
```

Audio volume mode config. If volumeMode is set to {@link AudioVolumeMode.APP_INDIVIDUAL}, this audio renderer will be affected by app volume percentage set by {@link setAppVolumePercentage}

**Type:** [AudioVolumeMode](arkts-audio-audio-audiovolumemode-e.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-AudioRendererInfo-volumeMode?: AudioVolumeMode--><!--Device-AudioRendererInfo-volumeMode?: AudioVolumeMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

