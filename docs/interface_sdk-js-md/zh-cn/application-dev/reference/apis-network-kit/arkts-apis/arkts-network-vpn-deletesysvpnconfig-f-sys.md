# deleteSysVpnConfig（系统接口）

## 导入模块

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## deleteSysVpnConfig

```TypeScript
function deleteSysVpnConfig(vpnId: string): Promise<void>
```

Delete the configuration of system VPN network by the specified vpnId.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**需要权限：** ohos.permission.MANAGE_VPN

<!--Device-vpn-function deleteSysVpnConfig(vpnId: string): Promise<void>--><!--Device-vpn-function deleteSysVpnConfig(vpnId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vpnId | string | 是 | Indicates the uuid of the VPN network configuration. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Operation failed. Cannot connect to service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

