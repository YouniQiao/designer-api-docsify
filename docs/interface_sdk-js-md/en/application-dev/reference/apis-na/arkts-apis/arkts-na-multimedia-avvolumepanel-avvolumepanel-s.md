# AVVolumePanel

A panel to set the system audio output volume.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare struct AVVolumePanel--><!--Device-unnamed-export declare struct AVVolumePanel-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## build

```TypeScript
@Builder
  build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-AVVolumePanel-@Builder  build(): void--><!--Device-AVVolumePanel-@Builder  build(): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volumeLevel

```TypeScript
@PropRef
  volumeLevel?: int
```

Sets the device volume through the volume panel. The value should be between mininum and maxinum current device volume, otherwise it will be discarded.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-AVVolumePanel-@PropRef  volumeLevel?: int--><!--Device-AVVolumePanel-@PropRef  volumeLevel?: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volumeParameter

```TypeScript
@PropRef
  volumeParameter?: AVVolumePanelParameter
```

Sets the custom parameters of volume panel.

**Type:** [AVVolumePanelParameter](arkts-na-multimedia-avvolumepanel-avvolumepanelparameter-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-AVVolumePanel-@PropRef  volumeParameter?: AVVolumePanelParameter--><!--Device-AVVolumePanel-@PropRef  volumeParameter?: AVVolumePanelParameter-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

