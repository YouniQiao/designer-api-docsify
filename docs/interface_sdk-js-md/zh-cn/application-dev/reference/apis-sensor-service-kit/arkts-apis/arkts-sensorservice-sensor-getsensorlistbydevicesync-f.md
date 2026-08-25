# getSensorListByDeviceSync

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## getSensorListByDeviceSync

```TypeScript
function getSensorListByDeviceSync(deviceId?: number): Array<Sensor>
```

同步获取设备的所有传感器信息。getSensorListByDeviceSync返回设备上所有传感器信息，getSingleSensorByDeviceSync返回指定单个传感器信息。

**起始版本：** 19

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;Sensor & gt; |
