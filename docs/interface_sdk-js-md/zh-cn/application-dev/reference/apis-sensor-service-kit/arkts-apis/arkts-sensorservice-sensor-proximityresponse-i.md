# ProximityResponse

接近光传感器数据，继承于[Response](arkts-sensorservice-sensor-response-i.md)。

**继承/实现关系：** ProximityResponse extends [Response](arkts-sensorservice-sensor-response-i.md)

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-sensor-interface ProximityResponse extends Response--><!--Device-sensor-interface ProximityResponse extends Response-End-->

**系统能力：** SystemCapability.Sensors.Sensor

## distance

```TypeScript
distance: double
```

可见物体与设备显示器的接近程度。取值范围：0表示接近（物体靠近设备），大于0表示远离（物体远离设备）。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-ProximityResponse-distance: double--><!--Device-ProximityResponse-distance: double-End-->

**系统能力：** SystemCapability.Sensors.Sensor

