# getPortSupportModes（系统接口）

## 导入模块

```TypeScript
```

## getPortSupportModes

```TypeScript
function getPortSupportModes(portId: number): PortModeType
```

获取指定的端口支持的模式列表的组合掩码。适用于系统应用需要查询USB-C端口能力判断是否支持特定模式（如UFP、DFP或DRP模式）的场景。开发者模式关闭时，如果没有设备接入，接口返回undefined，注意需要对接口返回值做判空 处理。详细枚举值参见[PortModeType](arkts-basicservices-usbmanager-portmodetype-e-sys.md#portmodetype系统接口)。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function getPortSupportModes(portId: int): PortModeType--><!--Device-usbManager-function getPortSupportModes(portId: int): PortModeType-End-->

**系统能力：** SystemCapability.USB.USBManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [portId](arkts-basicservices-serialmanager-serialport-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| [PortModeType](arkts-basicservices-usbmanager-portmodetype-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
