# VibratorCurvePoint

相对事件振动强度的增益。用于[ContinuousParam](arkts-sensorservice-vibrator-continuousparam-i.md)和[VibratorEvent](arkts-sensorservice-vibrator-vibratorevent-i.md)的points字段，精细控制振动强度和频率的变化趋势。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-vibrator-interface VibratorCurvePoint--><!--Device-vibrator-interface VibratorCurvePoint-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## frequency

```TypeScript
frequency?: int
```

可选参数，相对事件振动频率变化。取值范围：[-100,100]内所有整数。默认值：0。使用场景：适用于精细调节振动频率的交互反馈场景，正值频率升高，负值频率降低。不填写时默认不改变频率。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorCurvePoint-frequency?: int--><!--Device-VibratorCurvePoint-frequency?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## intensity

```TypeScript
intensity?: double
```

可选参数，相对事件振动强度增益。取值范围：[0,1]。默认值：1。使用场景：适用于精细调节振动强度的交互反馈场景，值越大振动越强。不填写时默认使用最大增益。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorCurvePoint-intensity?: double--><!--Device-VibratorCurvePoint-intensity?: double-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## time

```TypeScript
time: int
```

起始时间偏移。单位：ms。用于指定振动调节曲线中该调节点的时间位置。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorCurvePoint-time: int--><!--Device-VibratorCurvePoint-time: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

