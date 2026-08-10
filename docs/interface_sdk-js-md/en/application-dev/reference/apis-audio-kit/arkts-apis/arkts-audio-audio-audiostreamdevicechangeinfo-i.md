# AudioStreamDeviceChangeInfo

流设备变更时，应用接收到的事件。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioStreamDeviceChangeInfo--><!--Device-audio-interface AudioStreamDeviceChangeInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## changeReason

```TypeScript
changeReason: AudioStreamDeviceChangeReason
```

流设备变更原因。

**Type:** [AudioStreamDeviceChangeReason](arkts-audio-audio-audiostreamdevicechangereason-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioStreamDeviceChangeInfo-changeReason: AudioStreamDeviceChangeReason--><!--Device-AudioStreamDeviceChangeInfo-changeReason: AudioStreamDeviceChangeReason-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## devices

```TypeScript
devices: AudioDeviceDescriptors
```

设备信息。

**Type:** [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioStreamDeviceChangeInfo-devices: AudioDeviceDescriptors--><!--Device-AudioStreamDeviceChangeInfo-devices: AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## preDevices

```TypeScript
preDevices?: AudioDeviceDescriptors
```

应用流设备变更前的设备信息。

**Type:** [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioStreamDeviceChangeInfo-preDevices?: AudioDeviceDescriptors--><!--Device-AudioStreamDeviceChangeInfo-preDevices?: AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

