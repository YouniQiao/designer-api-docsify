# getSensorListSync

## 导入模块

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## getSensorListSync

```TypeScript
function getSensorListSync(): Array<Sensor>
```

获取设备上的所有传感器信息，使用同步方式返回结果。

**起始版本：** 12

**系统能力：** SystemCapability.Sensors.Sensor

**返回值：**

| 类型 |
| --- |
| Array & lt;Sensor & gt; |

**错误码：**

| 错误码ID |
| --- |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
