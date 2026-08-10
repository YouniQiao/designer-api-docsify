# getSysVpnConfigList（系统接口）

## 导入模块

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## getSysVpnConfigList

```TypeScript
function getSysVpnConfigList(): Promise<Array<SysVpnConfig>>
```

Get all system VPN network configuration.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**需要权限：** ohos.permission.MANAGE_VPN

<!--Device-vpn-function getSysVpnConfigList(): Promise<Array<SysVpnConfig>>--><!--Device-vpn-function getSysVpnConfigList(): Promise<Array<SysVpnConfig>>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;SysVpnConfig&gt;&gt; | The promise returned by the all VPN network configuration. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2200003 | System internal error. |
| 2200002 | Operation failed. Cannot connect to service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

