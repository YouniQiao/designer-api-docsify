# VibratorEvent

振动事件。用于[VibratorPattern](arkts-sensorservice-vibrator-vibratorpattern-i.md)的events数组中定义具体的振动事件。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-vibrator-interface VibratorEvent--><!--Device-vibrator-interface VibratorEvent-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## duration

```TypeScript
duration?: int
```

可选参数，表示振动持续时间。单位：ms。取值范围：(0,5000]区间所有整数。默认值：短振默认48，长振默认1000。使用场景：适用于长振和短振交互反馈场景。不填写时使用对应类型的默认持续时间。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-duration?: int--><!--Device-VibratorEvent-duration?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## eventType

```TypeScript
eventType: VibratorEventType
```

振动事件类型。CONTINUOUS（0）表示长振，TRANSIENT（1）表示短振。

**Type:** [VibratorEventType](arkts-sensorservice-vibrator-vibratoreventtype-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-eventType: VibratorEventType--><!--Device-VibratorEvent-eventType: VibratorEventType-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## frequency

```TypeScript
frequency?: int
```

可选参数，表示振动频率。取值范围：[0,100]区间内所有整数。默认值：50。不填写时默认使用中等频率。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-frequency?: int--><!--Device-VibratorEvent-frequency?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## index

```TypeScript
index?: int
```

可选参数，表示马达通道编号。取值范围：[0,2]区间内所有整数。默认值：0。使用场景：不同通道对应不同的马达器件，适用于多马达设备的精细控制场景。不填写时默认使用通道0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-index?: int--><!--Device-VibratorEvent-index?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## intensity

```TypeScript
intensity?: int
```

可选参数，表示振动强度。取值范围：[0,100]区间所有整数。默认值：100。不填写时默认使用最大强度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-intensity?: int--><!--Device-VibratorEvent-intensity?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## points

```TypeScript
points?: Array<VibratorCurvePoint>
```

可选参数，表示振动调节曲线数组。使用场景：适用于需要精细控制振动强度和频率变化趋势的交互反馈场景。数组中元素个数最少设置4个，最大设置16个。

**Type:** Array&lt;VibratorCurvePoint&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-points?: Array<VibratorCurvePoint>--><!--Device-VibratorEvent-points?: Array<VibratorCurvePoint>-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## time

```TypeScript
time: int
```

振动起始时间。单位：ms。取值范围：[0,1800000]区间内所有整数。用于指定振动事件在序列中的起始时间点。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-VibratorEvent-time: int--><!--Device-VibratorEvent-time: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

