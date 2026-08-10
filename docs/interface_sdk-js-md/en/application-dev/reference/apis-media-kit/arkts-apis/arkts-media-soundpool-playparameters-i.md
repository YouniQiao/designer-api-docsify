# PlayParameters

表示音频池播放参数设置。

通过设置播放相关参数，来控制播放的音量，循环次数，播放优先级等参数。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface PlayParameters--><!--Device-unnamed-export interface PlayParameters-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## leftVolume

```TypeScript
leftVolume?: double
```

设置左声道音量。设置范围为[0.0, 1.0]，默认值为1.0。

当音量超过边界值时自动设置为边界值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PlayParameters-leftVolume?: double--><!--Device-PlayParameters-leftVolume?: double-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## loop

```TypeScript
loop?: int
```

设置循环次数。

当loop≥0时，实际播放次数为loop+1。

当loop＜0时，表示一直循环。

默认值：0，表示仅播放一次。

当loop为浮点数时只截取整数部分。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PlayParameters-loop?: int--><!--Device-PlayParameters-loop?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## pitch

```TypeScript
pitch?: double
```

Pitch of the sound. The value ranges from 0.25 to 4.0 with a step size of 0.001. The Deault pitch is 1.0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PlayParameters-pitch?: double--><!--Device-PlayParameters-pitch?: double-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## priority

```TypeScript
priority?: int
```

音频流播放的优先级。0为最低优先级，数值越大优先级越高。

通过相互比较数值大小确定播放优先级，设置范围为大于等于0的整数。默认值为0。 

当优先级为负数时自动设置为0，为浮点数时只截取整数部分。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PlayParameters-priority?: int--><!--Device-PlayParameters-priority?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## rate

```TypeScript
rate?: int
```

设置音频播放的倍速，具体倍速范围参照[AudioRendererRate](../../../reference/apis-audio-kit/arkts-apis-audio-e.md)。默认值：0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PlayParameters-rate?: int--><!--Device-PlayParameters-rate?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## rightVolume

```TypeScript
rightVolume?: double
```

设置右声道音量（当前不支持左右分别设置，将以左声道音量为准）。设置范围为[0.0, 1.0]，默认值为1.0。

当音量超过边界值时自动设置为边界值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PlayParameters-rightVolume?: double--><!--Device-PlayParameters-rightVolume?: double-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

