# SensorInfoParam

Defines sensor parameters, including **deviceId** and **sensorIndex**.

**Since:** 23

<!--Device-sensor-interface SensorInfoParam--><!--Device-sensor-interface SensorInfoParam-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## deviceId

```TypeScript
deviceId?: int
```

Device ID. The default value is -1, indicating the local device. You can use [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md) or [sensorStatusChange](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_sensoridcolor) to obtain the device ID.

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SensorInfoParam-deviceId?: int--><!--Device-SensorInfoParam-deviceId?: int-End-->

**System capability:** SystemCapability.Sensors.Sensor

## sensorIndex

```TypeScript
sensorIndex?: int
```

Sensor index. The default value is **0**, indicating the default sensor on the device. You can use [getSensorList](arkts-sensorservice-sensor-getsensorlist-f.md) or [sensorStatusChange](arkts-sensorservice-sensor-onsensoridcolor-f-sys.md#on_sensoridcolor) to obtain the sensor index.

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SensorInfoParam-sensorIndex?: int--><!--Device-SensorInfoParam-sensorIndex?: int-End-->

**System capability:** SystemCapability.Sensors.Sensor

