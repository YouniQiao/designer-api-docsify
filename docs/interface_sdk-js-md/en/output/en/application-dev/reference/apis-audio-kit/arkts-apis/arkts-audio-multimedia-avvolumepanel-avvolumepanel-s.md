# AVVolumePanel

A panel to set the system audio output volume.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Component

<!--Device-unnamed-export declare struct AVVolumePanel--><!--Device-unnamed-export declare struct AVVolumePanel-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## build

```TypeScript
build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

<!--Device-AVVolumePanel-build(): void--><!--Device-AVVolumePanel-build(): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volumeLevel

```TypeScript
volumeLevel?: int
```

Sets the device volume through the volume panel. The value should be between mininum and maxinum current device volume, otherwise it will be discarded.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVVolumePanel-volumeLevel?: int--><!--Device-AVVolumePanel-volumeLevel?: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volumeParameter

```TypeScript
volumeParameter?: AVVolumePanelParameter
```

Sets the custom parameters of volume panel.

**Type:** AVVolumePanelParameter

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVVolumePanel-volumeParameter?: AVVolumePanelParameter--><!--Device-AVVolumePanel-volumeParameter?: AVVolumePanelParameter-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

