# AVVolumePanel(Defines a panel to set the system audio output volume.)

A panel to set the system audio output volume.

**Since:** 12

<!--Device-unnamed-export declare struct AVVolumePanel--><!--Device-unnamed-export declare struct AVVolumePanel-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## Modules to Import

```TypeScript
import { AVVolumePanel, AVVolumePanelParameter } from '@kit.AudioKit';
```

## volumeLevel

```TypeScript
@Prop
  volumeLevel?: number
```

Sets the device volume through the volume panel. The value should be between mininum and maxinum current device volume, otherwise it will be discarded.

**Type:** number

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVVolumePanel-@Prop  volumeLevel?: number--><!--Device-AVVolumePanel-@Prop  volumeLevel?: number-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volumeParameter

```TypeScript
@Prop
  volumeParameter?: AVVolumePanelParameter
```

Sets the custom parameters of volume panel.

**Type:** [AVVolumePanelParameter](../../apis-na/arkts-apis/arkts-na-multimedia-avvolumepanel-avvolumepanelparameter-c.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVVolumePanel-@Prop  volumeParameter?: AVVolumePanelParameter--><!--Device-AVVolumePanel-@Prop  volumeParameter?: AVVolumePanelParameter-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

