# SensorId

表示当前支持订阅或取消订阅的传感器类型。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-sensor-enum SensorId--><!--Device-sensor-enum SensorId-End-->

**System capability:** SystemCapability.Sensors.Sensor

## COLOR

```TypeScript
COLOR = 14
```

颜色传感器。用于订阅/取消订阅颜色传感器数据，上报数据为[ColorResponse](arkts-sensorservice-sensor-colorresponse-i-sys.md)对象，包含光照强度和色温信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SensorId-COLOR = 14--><!--Device-SensorId-COLOR = 14-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

## SAR

```TypeScript
SAR = 15
```

吸收比率传感器。用于订阅/取消订阅吸收比率传感器数据，上报数据为[SarResponse](arkts-sensorservice-sensor-sarresponse-i-sys.md)对象，包含电磁波吸收率信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SensorId-SAR = 15--><!--Device-SensorId-SAR = 15-End-->

**System capability:** SystemCapability.Sensors.Sensor

**System API:** This is a system API.

