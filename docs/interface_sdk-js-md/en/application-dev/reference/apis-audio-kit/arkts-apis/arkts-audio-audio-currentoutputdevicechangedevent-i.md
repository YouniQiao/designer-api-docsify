# CurrentOutputDeviceChangedEvent

Describes the event indicating that the output device changes.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-audio-interface CurrentOutputDeviceChangedEvent--><!--Device-audio-interface CurrentOutputDeviceChangedEvent-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## changeReason

```TypeScript
changeReason: AudioStreamDeviceChangeReason
```

Audio device change reason.

**Type:** AudioStreamDeviceChangeReason

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CurrentOutputDeviceChangedEvent-changeReason: AudioStreamDeviceChangeReason--><!--Device-CurrentOutputDeviceChangedEvent-changeReason: AudioStreamDeviceChangeReason-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## devices

```TypeScript
devices: AudioDeviceDescriptors
```

Audio device descriptors after change.

**Type:** AudioDeviceDescriptors

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CurrentOutputDeviceChangedEvent-devices: AudioDeviceDescriptors--><!--Device-CurrentOutputDeviceChangedEvent-devices: AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## preDevices

```TypeScript
preDevices?: AudioDeviceDescriptors
```

Audio device descriptors before change.

**Type:** AudioDeviceDescriptors

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CurrentOutputDeviceChangedEvent-preDevices?: AudioDeviceDescriptors--><!--Device-CurrentOutputDeviceChangedEvent-preDevices?: AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## recommendedAction

```TypeScript
recommendedAction: OutputDeviceChangeRecommendedAction
```

Recommend action when device change.

**Type:** OutputDeviceChangeRecommendedAction

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CurrentOutputDeviceChangedEvent-recommendedAction: OutputDeviceChangeRecommendedAction--><!--Device-CurrentOutputDeviceChangedEvent-recommendedAction: OutputDeviceChangeRecommendedAction-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

