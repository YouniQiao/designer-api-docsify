# AudioDeviceDescriptor

Describes an audio device.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioDeviceDescriptor--><!--Device-audio-interface AudioDeviceDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## dmDeviceInfo

```TypeScript
readonly dmDeviceInfo?: string
```

Extended information for distributed device, includes whether the device supports stereo, Device SN, etc.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioDeviceDescriptor-readonly dmDeviceInfo?: string--><!--Device-AudioDeviceDescriptor-readonly dmDeviceInfo?: string-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

## dmDeviceType

```TypeScript
readonly dmDeviceType?: int
```

Only \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ with networkId、\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ or \_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ has dmDeviceType which indicated deviceTypeId.

**Type:** int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-AudioDeviceDescriptor-readonly dmDeviceType?: int--><!--Device-AudioDeviceDescriptor-readonly dmDeviceType?: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

## highQualityRecordingSupported

```TypeScript
readonly highQualityRecordingSupported?: boolean
```

whether supports high-quality recording.

**Type:** boolean

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 24.

<!--Device-AudioDeviceDescriptor-readonly highQualityRecordingSupported?: boolean--><!--Device-AudioDeviceDescriptor-readonly highQualityRecordingSupported?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

## interruptGroupId

```TypeScript
readonly interruptGroupId: int
```

Interrupt group id

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioDeviceDescriptor-readonly interruptGroupId: int--><!--Device-AudioDeviceDescriptor-readonly interruptGroupId: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**System API:** This is a system API.

## networkId

```TypeScript
readonly networkId: string
```

Device network id

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioDeviceDescriptor-readonly networkId: string--><!--Device-AudioDeviceDescriptor-readonly networkId: string-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**System API:** This is a system API.

## volumeGroupId

```TypeScript
readonly volumeGroupId: int
```

Volume group id

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioDeviceDescriptor-readonly volumeGroupId: int--><!--Device-AudioDeviceDescriptor-readonly volumeGroupId: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**System API:** This is a system API.

