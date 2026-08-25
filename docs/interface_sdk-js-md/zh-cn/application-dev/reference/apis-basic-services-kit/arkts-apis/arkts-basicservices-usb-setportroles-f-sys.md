# setPortRoles（系统接口）

## 导入模块

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## setPortRoles

```TypeScript
function setPortRoles(portId: number, powerRole: PowerRoleType, dataRole: DataRoleType): Promise<boolean>
```

设置指定的端口支持的角色模式，包含充电角色、数据传输角色。

**起始版本：** 9

**废弃版本：** 9

**替代接口：** [setPortRoles](arkts-basicservices-usbmanager-setportroles-f-sys.md)

**系统能力：** SystemCapability.USB.USBManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [portId](arkts-basicservices-serialmanager-serialport-i.md) | number | 是 |
| powerRole | [PowerRoleType](arkts-basicservices-usbmanager-powerroletype-e-sys.md) | 是 |
| dataRole | [DataRoleType](arkts-basicservices-usbmanager-dataroletype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
