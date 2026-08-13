# setPortRoles（系统接口）

## setPortRoles

```TypeScript
function setPortRoles(portId: number, powerRole: PowerRoleType, dataRole: DataRoleType): Promise<void>
```

设置指定的端口支持的角色模式，包含充电角色、数据传输角色。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [setPortRoleTypes](arkts-basicservices-usbmanager-setportroletypes-f-sys.md#setPortRoleTypes（系统接口）)(portId: int, powerRole: PowerRoleType, dataRole: DataRoleType)

<!--Device-usbManager-function setPortRoles(portId: number, powerRole: PowerRoleType, dataRole: DataRoleType): Promise<void>--><!--Device-usbManager-function setPortRoles(portId: number, powerRole: PowerRoleType, dataRole: DataRoleType): Promise<void>-End-->

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
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
