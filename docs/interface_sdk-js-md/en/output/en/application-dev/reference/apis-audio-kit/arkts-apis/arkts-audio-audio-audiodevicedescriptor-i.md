# AudioDeviceDescriptor

Describes an audio device.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioDeviceDescriptor--><!--Device-audio-interface AudioDeviceDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## address

```TypeScript
readonly address: string
```

Static MAC address of the device. For a Bluetooth device, you must request the ohos.permission.USE\_BLUETOOTH permission.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly address: string--><!--Device-AudioDeviceDescriptor-readonly address: string-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## capabilities

```TypeScript
readonly capabilities?: Array<AudioStreamInfo>
```

Audio stream capabilities supported by the device.

**Type:** Array&lt;AudioStreamInfo&gt;

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-AudioDeviceDescriptor-readonly capabilities?: Array<AudioStreamInfo>--><!--Device-AudioDeviceDescriptor-readonly capabilities?: Array<AudioStreamInfo>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## channelCounts

```TypeScript
readonly channelCounts: Array<int>
```

Number of channels supported.

**Type:** Array&lt;int&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly channelCounts: Array<int>--><!--Device-AudioDeviceDescriptor-readonly channelCounts: Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## channelMasks

```TypeScript
readonly channelMasks: Array<int>
```

Supported channel masks.

**Type:** Array&lt;int&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly channelMasks: Array<int>--><!--Device-AudioDeviceDescriptor-readonly channelMasks: Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## deviceRole

```TypeScript
readonly deviceRole: DeviceRole
```

Device role.

**Type:** DeviceRole

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly deviceRole: DeviceRole--><!--Device-AudioDeviceDescriptor-readonly deviceRole: DeviceRole-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## deviceType

```TypeScript
readonly deviceType: DeviceType
```

Device type.

**Type:** DeviceType

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly deviceType: DeviceType--><!--Device-AudioDeviceDescriptor-readonly deviceType: DeviceType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## displayName

```TypeScript
readonly displayName: string
```

Display name of the device.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly displayName: string--><!--Device-AudioDeviceDescriptor-readonly displayName: string-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## encodingTypes

```TypeScript
readonly encodingTypes?: Array<AudioEncodingType>
```

Supported encoding types.

**Type:** Array&lt;AudioEncodingType&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly encodingTypes?: Array<AudioEncodingType>--><!--Device-AudioDeviceDescriptor-readonly encodingTypes?: Array<AudioEncodingType>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## id

```TypeScript
readonly id: int
```

Audio device id.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly id: int--><!--Device-AudioDeviceDescriptor-readonly id: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## model

```TypeScript
readonly model?: string
```

Model of the device.

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-AudioDeviceDescriptor-readonly model?: string--><!--Device-AudioDeviceDescriptor-readonly model?: string-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## name

```TypeScript
readonly name: string
```

Device name. For a Bluetooth device, you must request the ohos.permission.USE\_BLUETOOTH permission.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly name: string--><!--Device-AudioDeviceDescriptor-readonly name: string-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## sampleRates

```TypeScript
readonly sampleRates: Array<int>
```

Supported sampling rates. SystemCapability.Multimedia.Audio.Device

**Type:** Array&lt;int&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly sampleRates: Array<int>--><!--Device-AudioDeviceDescriptor-readonly sampleRates: Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## spatializationSupported

```TypeScript
readonly spatializationSupported?: boolean
```

Whether the device supports spatial audio rendering. **true** if supported, **false** otherwise.

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-AudioDeviceDescriptor-readonly spatializationSupported?: boolean--><!--Device-AudioDeviceDescriptor-readonly spatializationSupported?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

