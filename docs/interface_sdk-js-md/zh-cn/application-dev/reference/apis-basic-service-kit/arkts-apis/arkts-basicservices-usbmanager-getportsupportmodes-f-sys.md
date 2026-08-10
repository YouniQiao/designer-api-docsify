# getPortSupportModes（系统接口）

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## getPortSupportModes

```TypeScript
function getPortSupportModes(portId: int): PortModeType
```

获取指定的端口支持的模式列表的组合掩码。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function getPortSupportModes(portId: int): PortModeType--><!--Device-usbManager-function getPortSupportModes(portId: int): PortModeType-End-->

**系统能力：** SystemCapability.USB.USBManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 端口号。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PortModeType](arkts-basicservices-usb-portmodetype-e-sys.md) | 支持的模式列表的组合掩码。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  &lt;br&gt;1.Mandatory parameters are left unspecified.  &lt;br&gt;2.Incorrect parameter types. |
| 801 | Capability not supported.<br>**适用版本：** 18+ |
| 201 | Permission verification failed. The application does not have the permission required to call the API.<br>**适用版本：** 18+ |
| 202 | Permission denied. Normal application do not have permission to use system api. |

