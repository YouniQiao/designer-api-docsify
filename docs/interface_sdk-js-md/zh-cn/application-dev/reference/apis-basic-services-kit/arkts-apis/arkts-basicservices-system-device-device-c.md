# Device

getInfo interface

**起始版本：** 3

**废弃版本：** 6

**系统能力：** SystemCapability.Startup.SystemInfo.Lite

## 导入模块

```TypeScript
import { Device, DeviceResponse, GetDeviceOptions } from 'kits/@kit.BasicServicesKit';
```

## getInfo

```TypeScript
static getInfo(options?: GetDeviceOptions): void
```

获取当前设备的信息。该接口异步读取系统设备信息，通过回调函数返回设备品牌、型号、屏幕参数等数据。

> **说明：**

> 
> 在首页的onShow生命周期之前不建议调用Device.getInfo接口。
**系统能力：** SystemCapability.Startup.SystemInfo.Lite  
**返回值：**  
| 类型 | 说明 | | -------- | -------- | | void |

**起始版本：** 3

**废弃版本：** 6

**系统能力：** SystemCapability.Startup.SystemInfo.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [GetDeviceOptions](arkts-basicservices-system-device-getdeviceoptions-i.md) | 否 |
