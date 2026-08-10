# Response

传感器数据的时间戳与精度信息基类，所有传感器Response类型均继承于此。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sensor-interface Response--><!--Device-sensor-interface Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## accuracy

```TypeScript
accuracy: SensorAccuracy
```

传感器数据上报的精度挡位值，表示当前上报数据的可信程度。

**Type:** [SensorAccuracy](arkts-sensorservice-sensor-sensoraccuracy-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Response-accuracy: SensorAccuracy--><!--Device-Response-accuracy: SensorAccuracy-End-->

**System capability:** SystemCapability.Sensors.Sensor

## timestamp

```TypeScript
timestamp: long
```

传感器数据上报的时间戳。从设备开机开始计时到上报数据的时间，单位：ns（纳秒）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Response-timestamp: long--><!--Device-Response-timestamp: long-End-->

**System capability:** SystemCapability.Sensors.Sensor

