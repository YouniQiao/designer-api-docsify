# setAlwaysOnVpnEnabled（系统接口）

## 导入模块

```TypeScript
import { vpnExtension } from 'kits/@kit.NetworkKit';
```

## setAlwaysOnVpnEnabled

```TypeScript
function setAlwaysOnVpnEnabled(enable: boolean, bundleName: string): Promise<void>
```

Set the Enable/Disable Always on VPN mode for a device.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**需要权限：** ohos.permission.MANAGE_VPN

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-vpnExtension-function setAlwaysOnVpnEnabled(enable: boolean, bundleName: string): Promise<void>--><!--Device-vpnExtension-function setAlwaysOnVpnEnabled(enable: boolean, bundleName: string): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | Always on enable or disable |
| bundleName | string | 是 | bundleName is used to set always on. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

