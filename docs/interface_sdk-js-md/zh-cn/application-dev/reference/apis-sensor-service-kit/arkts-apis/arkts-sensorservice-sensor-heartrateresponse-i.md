# HeartRateResponse

心率传感器数据，继承于[Response](arkts-sensorservice-sensor-response-i.md)。

**继承/实现关系：** HeartRateResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sensor-interface HeartRateResponse extends Response--><!--Device-sensor-interface HeartRateResponse extends Response-End-->

**系统能力：** SystemCapability.Sensors.Sensor

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## heartRate

```TypeScript
heartRate: double
```

用户的心率数值。单位：bpm（beats per minute，每分钟心跳次数）。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-HeartRateResponse-heartRate: double--><!--Device-HeartRateResponse-heartRate: double-End-->

**系统能力：** SystemCapability.Sensors.Sensor

