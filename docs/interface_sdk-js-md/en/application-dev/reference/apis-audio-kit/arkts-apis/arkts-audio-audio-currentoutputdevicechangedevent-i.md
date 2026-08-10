# CurrentOutputDeviceChangedEvent

应用接收到输出设备的变更事件。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-audio-interface CurrentOutputDeviceChangedEvent--><!--Device-audio-interface CurrentOutputDeviceChangedEvent-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## changeReason

```TypeScript
changeReason: AudioStreamDeviceChangeReason
```

设备变更原因。

**Type:** [AudioStreamDeviceChangeReason](arkts-audio-audio-audiostreamdevicechangereason-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CurrentOutputDeviceChangedEvent-changeReason: AudioStreamDeviceChangeReason--><!--Device-CurrentOutputDeviceChangedEvent-changeReason: AudioStreamDeviceChangeReason-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## devices

```TypeScript
devices: AudioDeviceDescriptors
```

设备信息。

**Type:** [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CurrentOutputDeviceChangedEvent-devices: AudioDeviceDescriptors--><!--Device-CurrentOutputDeviceChangedEvent-devices: AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## preDevices

```TypeScript
preDevices?: AudioDeviceDescriptors
```

应用输出设备变更前的设备信息。

**Type:** [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CurrentOutputDeviceChangedEvent-preDevices?: AudioDeviceDescriptors--><!--Device-CurrentOutputDeviceChangedEvent-preDevices?: AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## recommendedAction

```TypeScript
recommendedAction: OutputDeviceChangeRecommendedAction
```

设备变更后推荐的操作。

**Type:** [OutputDeviceChangeRecommendedAction](arkts-audio-audio-outputdevicechangerecommendedaction-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-CurrentOutputDeviceChangedEvent-recommendedAction: OutputDeviceChangeRecommendedAction--><!--Device-CurrentOutputDeviceChangedEvent-recommendedAction: OutputDeviceChangeRecommendedAction-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

