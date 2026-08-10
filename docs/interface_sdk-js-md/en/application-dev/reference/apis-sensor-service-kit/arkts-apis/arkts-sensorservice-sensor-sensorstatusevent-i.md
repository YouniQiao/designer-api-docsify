# SensorStatusEvent

设备状态变化事件数据，用于描述传感器上下线事件的信息。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-sensor-interface SensorStatusEvent--><!--Device-sensor-interface SensorStatusEvent-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## deviceId

```TypeScript
deviceId: int
```

设备ID。-1表示本地设备，其它值表示远程设备。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-SensorStatusEvent-deviceId: int--><!--Device-SensorStatusEvent-deviceId: int-End-->

**System capability:** SystemCapability.Sensors.Sensor

## deviceName

```TypeScript
deviceName: string
```

设备名称，标识传感器的来源设备。

**Type:** string

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-SensorStatusEvent-deviceName: string--><!--Device-SensorStatusEvent-deviceName: string-End-->

**System capability:** SystemCapability.Sensors.Sensor

## isSensorOnline

```TypeScript
isSensorOnline: boolean
```

传感器是否上线。true表示传感器上线，false表示传感器下线。

**Type:** boolean

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-SensorStatusEvent-isSensorOnline: boolean--><!--Device-SensorStatusEvent-isSensorOnline: boolean-End-->

**System capability:** SystemCapability.Sensors.Sensor

## sensorId

```TypeScript
sensorId: int
```

传感器类型ID，对应[SensorId](arkts-sensorservice-sensor-sensorid-e.md)枚举值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-SensorStatusEvent-sensorId: int--><!--Device-SensorStatusEvent-sensorId: int-End-->

**System capability:** SystemCapability.Sensors.Sensor

## sensorIndex

```TypeScript
sensorIndex: int
```

传感器索引，同一类型传感器可能有多个实例，通过sensorIndex区分。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-SensorStatusEvent-sensorIndex: int--><!--Device-SensorStatusEvent-sensorIndex: int-End-->

**System capability:** SystemCapability.Sensors.Sensor

## timestamp

```TypeScript
timestamp: long
```

事件发生的时间戳。从设备开机开始计时到事件发生的时间。单位：ms（毫秒）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-SensorStatusEvent-timestamp: long--><!--Device-SensorStatusEvent-timestamp: long-End-->

**System capability:** SystemCapability.Sensors.Sensor

