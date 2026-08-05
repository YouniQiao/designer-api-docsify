# PlayParameters

Describes the playback parameters of the sound pool. These parameters are used to control the playback volume, number of loops, and priority.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface PlayParameters--><!--Device-unnamed-export interface PlayParameters-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## leftVolume

```TypeScript
leftVolume?: double
```

Volume of the left channel. The value range is [0.0, 1.0], and the default value is **1.0**. When the volume exceeds the boundary value, the boundary value is automatically used.

**Type:** double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PlayParameters-leftVolume?: double--><!--Device-PlayParameters-leftVolume?: double-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## loop

```TypeScript
loop?: int
```

Number of loops. If this parameter is set to a value greater than or equal to 0, the number of times the content is actually played is the value of **loop** plus 1. If this parameter is set to a value less than 0, the content is played repeatedly. The default value is **0**, indicating that the content is played only once. If this parameter is set to a floating-point number, only the integer part is used.

**Type:** int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PlayParameters-loop?: int--><!--Device-PlayParameters-loop?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## pitch

```TypeScript
pitch?: double
```

Pitch of the sound. The value ranges from 0.25 to 4.0 with a step size of 0.001. The default value is 1.0.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayParameters-pitch?: double--><!--Device-PlayParameters-pitch?: double-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## priority

```TypeScript
priority?: int
```

Priority for playing an audio stream. The value **0** indicates the lowest priority. A larger value indicates a higher priority. The playback priority is determined by comparing the values. The value must be an integer greater than or equal to 0. The default value is **0**. If this parameter is set to a negative value, it is automatically set to 0. If this parameter is set to a floating point number, only the integer part is used.

**Type:** int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PlayParameters-priority?: int--><!--Device-PlayParameters-priority?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## rate

```TypeScript
rate?: int
```

Playback rate. For details, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. Default value: **0**

**Type:** int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PlayParameters-rate?: int--><!--Device-PlayParameters-rate?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## rightVolume

```TypeScript
rightVolume?: double
```

Volume of the right channel. (Currently, the volume cannot be set separately for the left and right channels. The volume set for the left channel is used.) The value range is [0.0, 1.0], and the default value is **1.0**. When the volume exceeds the boundary value, the boundary value is automatically used.

**Type:** double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PlayParameters-rightVolume?: double--><!--Device-PlayParameters-rightVolume?: double-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

