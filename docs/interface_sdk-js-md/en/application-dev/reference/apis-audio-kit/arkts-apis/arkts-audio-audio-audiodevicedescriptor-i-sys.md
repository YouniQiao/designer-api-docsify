# AudioDeviceDescriptor

Describes an audio device.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-audio-interface AudioDeviceDescriptor--><!--Device-audio-interface AudioDeviceDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## dmDeviceInfo

```TypeScript
readonly dmDeviceInfo?: string
```

Extended information for distributed device, includes whether the device supports stereo, Device SN, etc.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioDeviceDescriptor-readonly dmDeviceInfo?: string--><!--Device-AudioDeviceDescriptor-readonly dmDeviceInfo?: string-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

## dmDeviceType

```TypeScript
readonly dmDeviceType?: int
```

Only [SPEAKER](arkts-audio-audio-devicetype-e.md#SPEAKER) with networkId、[REMOTE_CAST](arkts-audio-audio-devicetype-e.md#REMOTE_CAST) or [REMOTE_DAUDIO](arkts-audio-audio-devicetype-e.md#REMOTE_DAUDIO) has dmDeviceType which indicated deviceTypeId.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AudioDeviceDescriptor-readonly dmDeviceType?: int--><!--Device-AudioDeviceDescriptor-readonly dmDeviceType?: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

## highQualityRecordingSupported

```TypeScript
readonly highQualityRecordingSupported?: boolean
```

whether supports high-quality recording.

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

<!--Device-AudioDeviceDescriptor-readonly highQualityRecordingSupported?: boolean--><!--Device-AudioDeviceDescriptor-readonly highQualityRecordingSupported?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

## interruptGroupId

```TypeScript
readonly interruptGroupId: int
```

Interrupt group id

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AudioDeviceDescriptor-readonly interruptGroupId: int--><!--Device-AudioDeviceDescriptor-readonly interruptGroupId: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**System API:** This is a system API.

## networkId

```TypeScript
readonly networkId: string
```

Device network id

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AudioDeviceDescriptor-readonly networkId: string--><!--Device-AudioDeviceDescriptor-readonly networkId: string-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**System API:** This is a system API.

## volumeGroupId

```TypeScript
readonly volumeGroupId: int
```

Volume group id

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AudioDeviceDescriptor-readonly volumeGroupId: int--><!--Device-AudioDeviceDescriptor-readonly volumeGroupId: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**System API:** This is a system API.

