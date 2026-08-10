# AudioDeviceDescriptor

描述音频设备。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioDeviceDescriptor--><!--Device-audio-interface AudioDeviceDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## address

```TypeScript
readonly address: string
```

设备静态MAC地址。

如果是蓝牙设备，需要申请权限ohos.permission.USE_BLUETOOTH。

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

设备支持的音频流能力。

**Type:** Array&lt;AudioStreamInfo&gt;

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-AudioDeviceDescriptor-readonly capabilities?: Array<AudioStreamInfo>--><!--Device-AudioDeviceDescriptor-readonly capabilities?: Array<AudioStreamInfo>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## channelCounts

```TypeScript
readonly channelCounts: Array<int>
```

支持的通道数。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly channelCounts: Array<int>--><!--Device-AudioDeviceDescriptor-readonly channelCounts: Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## channelMasks

```TypeScript
readonly channelMasks: Array<int>
```

支持的通道掩码。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly channelMasks: Array<int>--><!--Device-AudioDeviceDescriptor-readonly channelMasks: Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## deviceRole

```TypeScript
readonly deviceRole: DeviceRole
```

设备角色。

**Type:** [DeviceRole](arkts-audio-audio-devicerole-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly deviceRole: DeviceRole--><!--Device-AudioDeviceDescriptor-readonly deviceRole: DeviceRole-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## deviceType

```TypeScript
readonly deviceType: DeviceType
```

设备类型。

**Type:** [DeviceType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-devicetype-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly deviceType: DeviceType--><!--Device-AudioDeviceDescriptor-readonly deviceType: DeviceType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## displayName

```TypeScript
readonly displayName: string
```

设备显示名。

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

支持的编码类型。

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

唯一的设备id。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly id: int--><!--Device-AudioDeviceDescriptor-readonly id: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## model

```TypeScript
readonly model?: string
```

设备的具体型号类别。

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-AudioDeviceDescriptor-readonly model?: string--><!--Device-AudioDeviceDescriptor-readonly model?: string-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## name

```TypeScript
readonly name: string
```

设备名称。

如果是蓝牙设备，需要申请权限ohos.permission.USE_BLUETOOTH。

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

支持的采样率。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioDeviceDescriptor-readonly sampleRates: Array<int>--><!--Device-AudioDeviceDescriptor-readonly sampleRates: Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## spatializationSupported

```TypeScript
readonly spatializationSupported?: boolean
```

设备是否支持空间音频。true表示支持空间音频，false表示不支持空间音频。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-AudioDeviceDescriptor-readonly spatializationSupported?: boolean--><!--Device-AudioDeviceDescriptor-readonly spatializationSupported?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Spatialization

