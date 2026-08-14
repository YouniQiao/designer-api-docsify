# AVVolumePanel

A panel to set the system audio output volume.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export declare struct AVVolumePanel--><!--Device-unnamed-export declare struct AVVolumePanel-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## Modules to Import

```TypeScript
import { AVVolumePanel } from 'AVVolumePanel';
import { AVVolumePanelParameter } from 'AVVolumePanelParameter';
```

## volumeLevel

```TypeScript
@Prop
  volumeLevel?: number
```

Sets the device volume through the volume panel. The value should be between mininum and maxinum current device volume, otherwise it will be discarded.

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVVolumePanel-@Prop  volumeLevel?: number--><!--Device-AVVolumePanel-@Prop  volumeLevel?: number-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volumeParameter

```TypeScript
@Prop
  volumeParameter?: AVVolumePanelParameter
```

Sets the custom parameters of volume panel.

**Type:** [AVVolumePanelParameter](arkts-audio-multimedia-avvolumepanel-avvolumepanelparameter-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVVolumePanel-@Prop  volumeParameter?: AVVolumePanelParameter--><!--Device-AVVolumePanel-@Prop  volumeParameter?: AVVolumePanelParameter-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

