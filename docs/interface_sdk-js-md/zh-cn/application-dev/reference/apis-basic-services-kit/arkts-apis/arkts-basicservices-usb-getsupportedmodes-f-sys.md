# getSupportedModes（系统接口）

## 导入模块

```TypeScript
import { usb } from '@kit.BasicServicesKit';
```

## getSupportedModes

```TypeScript
function getSupportedModes(portId: number): PortModeType
```

获取指定的端口支持的模式列表的组合掩码。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 9

**替代接口：** [getSupportedModes](arkts-basicservices-usbmanager-getsupportedmodes-f-sys.md)

**系统能力：** SystemCapability.USB.USBManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [portId](arkts-basicservices-serialmanager-serialport-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| [PortModeType](arkts-basicservices-usb-portmodetype-e-sys.md) |

**示例**

```TypeScript
let ret = usb.getSupportedModes(0);
```
