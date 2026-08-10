# BarometerResponse

气压计传感器数据，继承于[Response](arkts-sensorservice-sensor-response-i.md)。

**继承/实现关系：** BarometerResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sensor-interface BarometerResponse extends Response--><!--Device-sensor-interface BarometerResponse extends Response-End-->

**系统能力：** SystemCapability.Sensors.Sensor

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## pressure

```TypeScript
pressure: double
```

大气压力值。单位：hPa（百帕）。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-BarometerResponse-pressure: double--><!--Device-BarometerResponse-pressure: double-End-->

**系统能力：** SystemCapability.Sensors.Sensor

