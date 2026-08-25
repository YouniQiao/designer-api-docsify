# getPortList

## 导入模块

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## getPortList

```TypeScript
function getPortList(): Readonly<SerialPort>[]
```

查询串口设备清单，包括设备名称和对应的端口号。通常在应用启动时、设备连接后或需要检测可用串口设备时调用。

**起始版本：** 19

**系统能力：** SystemCapability.USB.USBManager.Serial

**返回值：**

| 类型 |
| --- |
| Readonly & lt;SerialPort & gt;[] |
