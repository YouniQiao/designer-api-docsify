# Response

传感器数据的时间戳与精度信息基类，所有传感器Response类型均继承于此。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Sensors.Sensor

## 导入模块

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## accuracy

```TypeScript
accuracy: SensorAccuracy
```

传感器数据上报的精度挡位值，表示当前上报数据的可信程度。

**类型：** [SensorAccuracy](arkts-sensorservice-sensor-sensoraccuracy-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Sensors.Sensor

## timestamp

```TypeScript
timestamp: long
```

传感器数据上报的时间戳。从设备开机开始计时到上报数据的时间，单位：ns（纳秒）。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Sensors.Sensor
