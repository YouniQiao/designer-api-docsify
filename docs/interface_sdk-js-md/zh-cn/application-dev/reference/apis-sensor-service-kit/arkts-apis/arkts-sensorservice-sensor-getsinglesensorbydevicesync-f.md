# getSingleSensorByDeviceSync

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## getSingleSensorByDeviceSync

```TypeScript
function getSingleSensorByDeviceSync(type: SensorId, deviceId?: number): Array<Sensor>
```

同步获取指定设备和类型的传感器信息。如果存在外设且未指定设备ID，获取到的传感器将是所有符合指定传感器类型的本地和外设传感器。如果不存在外设，则仅获取本地的传感器。

**起始版本：** 19

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SensorId](arkts-sensorservice-sensor-sensorid-e.md) | 是 |
| deviceId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;Sensor & gt; |
