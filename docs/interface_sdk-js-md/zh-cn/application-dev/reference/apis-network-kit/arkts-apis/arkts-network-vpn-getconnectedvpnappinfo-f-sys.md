# getConnectedVpnAppInfo（系统接口）

## 导入模块

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## getConnectedVpnAppInfo

```TypeScript
function getConnectedVpnAppInfo(): Promise<Array<string>>
```

Get the connected VPN App Info.

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

**需要权限：** ohos.permission.MANAGE_VPN

<!--Device-vpn-function getConnectedVpnAppInfo(): Promise<Array<string>>--><!--Device-vpn-function getConnectedVpnAppInfo(): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | The promise returned by the connected VPN App Info. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 19900002 | System internal error. |
| 19900001 | Invalid parameter value. |

