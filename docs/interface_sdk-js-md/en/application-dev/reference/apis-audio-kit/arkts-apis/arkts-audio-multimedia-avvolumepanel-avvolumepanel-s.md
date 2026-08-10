# AVVolumePanel

音量面板，可用于在当前应用内展示音量调节面板。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Component

<!--Device-unnamed-export declare struct AVVolumePanel--><!--Device-unnamed-export declare struct AVVolumePanel-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## Modules to Import

```TypeScript
import { AVVolumePanelParameter, AVVolumePanel } from 'kits/@kit.AudioKit';
```

## build

```TypeScript
build(): void
```

用于构造组件的建造接口。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

<!--Device-AVVolumePanel-build(): void--><!--Device-AVVolumePanel-build(): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volumeLevel

```TypeScript
volumeLevel?: int
```

通过音量面板设置的音量值。

该值应介于当前设备音量的最小值和最大值之间。

如果该值大于当前设备音量的最大值，则视为设置最大音量值。

如果该值小于当前设备音量的最小值，则视为设置最小音量值。

获取设备的最大值、最小值和当前值，可参考[AudioVolumeGroupManager](arkts-audio-audio-audiovolumegroupmanager-i.md)。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVVolumePanel-volumeLevel?: int--><!--Device-AVVolumePanel-volumeLevel?: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volumeParameter

```TypeScript
volumeParameter?: AVVolumePanelParameter
```

设置音量面板的自定义参数。 

如果不设置该参数，则为系统音量条。

**Type:** [AVVolumePanelParameter](arkts-audio-multimedia-avvolumepanel-avvolumepanelparameter-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVVolumePanel-volumeParameter?: AVVolumePanelParameter--><!--Device-AVVolumePanel-volumeParameter?: AVVolumePanelParameter-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

