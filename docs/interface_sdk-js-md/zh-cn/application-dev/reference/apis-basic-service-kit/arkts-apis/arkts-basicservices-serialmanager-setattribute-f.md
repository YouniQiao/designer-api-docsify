# setAttribute

## setAttribute

```TypeScript
function setAttribute(portId: int, attribute: SerialAttribute): void
```

设置串口的配置参数。如果未调用该方法，使用默认配置参数（波特率：9600bps；数据位：8；校验位：0；停止位：1）。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

<!--Device-serialManager-function setAttribute(portId: int, attribute: SerialAttribute): void--><!--Device-serialManager-function setAttribute(portId: int, attribute: SerialAttribute): void-End-->

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 目标设备的端口号，来自[getPortList](arkts-basicservices-serialmanager-getportlist-f.md#getportlist)获取的串口参数SerialPort。 |
| attribute | [SerialAttribute](arkts-basicservices-serialmanager-serialattribute-i.md) | 是 | 串口参数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [31400005](../../apis-basic-services-kit/errorcode-usb.md#31400005-设备未打开) | The serial port device is not opened. Call the open API first. |
| [31400003](../../apis-basic-services-kit/errorcode-usb.md#31400003-端口号不存在) | PortId does not exist. |
| [31400001](../../apis-basic-services-kit/errorcode-usb.md#31400001-串口服务异常) | Serial port management exception. |

