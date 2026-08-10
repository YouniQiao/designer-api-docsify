# Options

设置传感器上报频率及传感器选择参数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sensor-interface Options--><!--Device-sensor-interface Options-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## interval

```TypeScript
interval?: long | SensorFrequency
```

用于设置传感器数据上报的时间间隔。默认值：200000000ns（即200ms）。单位：ns（纳秒）。取值范围需参考各传感器的minSamplePeriod和maxSamplePeriod，可通过  
[getSingleSensor](arkts-sensorservice-sensor-getsinglesensor-f.md#getsinglesensor)查询。建议根据实际业务需求设置合理的上报频率，取值越小上报越频繁。当设置频率大于最大值时以最大值上报数据，小于最小值时以最小值上报数据。

**Type:** ArkTS-Dyn: number \| SensorFrequency  <br>ArkTS-Sta：long \| SensorFrequency

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Options-interval?: long | SensorFrequency--><!--Device-Options-interval?: long | SensorFrequency-End-->

**System capability:** SystemCapability.Sensors.Sensor

## sensorInfoParam

```TypeScript
sensorInfoParam?: SensorInfoParam
```

传感器传入设置参数，可指定deviceId、sensorIndex，用于多传感器场景下选择目标传感器。

从API version 19开始，该接口支持在原子化服务中使用。

**Type:** [SensorInfoParam](arkts-sensorservice-sensor-sensorinfoparam-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Options-sensorInfoParam?: SensorInfoParam--><!--Device-Options-sensorInfoParam?: SensorInfoParam-End-->

**System capability:** SystemCapability.Sensors.Sensor

