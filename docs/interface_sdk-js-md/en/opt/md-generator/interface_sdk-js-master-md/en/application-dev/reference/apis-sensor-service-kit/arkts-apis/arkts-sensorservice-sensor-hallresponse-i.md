# HallResponse

Describes the Hall effect sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response).

**Inheritance/Implementation:** HallResponse extends [Response](arkts-sensorservice-sensor-response-i.md#response)

**Since:** 23

<!--Device-sensor-interface HallResponse--><!--Device-sensor-interface HallResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
```

## status

```TypeScript
status: number
```

Hall effect sensor status. This parameter specifies whether a magnetic field exists around a device. The value **0** means that a magnetic field does not exist, and a value greater than **0** means the opposite.

**Type:** number

**Since:** 23

<!--Device-HallResponse-status: double--><!--Device-HallResponse-status: double-End-->

**System capability:** SystemCapability.Sensors.Sensor
