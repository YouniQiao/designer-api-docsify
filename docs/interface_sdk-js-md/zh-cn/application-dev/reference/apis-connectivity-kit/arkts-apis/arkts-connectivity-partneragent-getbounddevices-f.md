# getBoundDevices

## 导入模块

```TypeScript
import { partnerAgent } from 'kits/@kit.ConnectivityKit';
```

## getBoundDevices

```TypeScript
function getBoundDevices(): PartnerDeviceAddress[]
```

Gets the list of addresses of the bound partner device for this application.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-partnerAgent-function getBoundDevices(): PartnerDeviceAddress[]--><!--Device-partnerAgent-function getBoundDevices(): PartnerDeviceAddress[]-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PartnerDeviceAddress](arkts-connectivity-partnerdeviceaddress-t.md)[] | Returns the list of addresses of partner device. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 34900099 | Internal error. |
| 201 | Permission denied. |

