# getAttribute

## getAttribute

```TypeScript
function getAttribute(portId: int): Readonly<SerialAttribute>
```

获取指定串口的配置参数。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

<!--Device-serialManager-function getAttribute(portId: int): Readonly<SerialAttribute>--><!--Device-serialManager-function getAttribute(portId: int): Readonly<SerialAttribute>-End-->

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 目标设备的端口号，来自[getPortList](arkts-basicservices-serialmanager-getportlist-f.md#getPortList)获取的串口参数SerialPort。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Readonly&lt;[SerialAttribute](arkts-basicservices-serialmanager-serialattribute-i.md)&gt; | 返回串口的配置参数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [31400005](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-usb.md#31400005-设备未打开) | The serial port device is not opened. Call the open API first. |
| [31400003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-usb.md#31400003-端口号不存在) | PortId does not exist. |
| [31400001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-usb.md#31400001-串口服务异常) | Serial port management exception. |

