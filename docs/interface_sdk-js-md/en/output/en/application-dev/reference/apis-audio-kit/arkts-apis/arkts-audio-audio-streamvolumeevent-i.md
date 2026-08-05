# StreamVolumeEvent

Describes the event received by the application when the audio stream volume is changed.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-audio-interface StreamVolumeEvent--><!--Device-audio-interface StreamVolumeEvent-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## previousVolume

```TypeScript
previousVolume?: int
```

Volume level before change.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-StreamVolumeEvent-previousVolume?: int--><!--Device-StreamVolumeEvent-previousVolume?: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## streamUsage

```TypeScript
streamUsage: StreamUsage
```

Audio stream for which the volume changes.

**Type:** StreamUsage

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-StreamVolumeEvent-streamUsage: StreamUsage--><!--Device-StreamVolumeEvent-streamUsage: StreamUsage-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## updateUi

```TypeScript
updateUi: boolean
```

Whether to show the volume change in UI. **true** to show, **false** otherwise.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-StreamVolumeEvent-updateUi: boolean--><!--Device-StreamVolumeEvent-updateUi: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volume

```TypeScript
volume: int
```

Volume.

**Type:** int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-StreamVolumeEvent-volume: int--><!--Device-StreamVolumeEvent-volume: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

