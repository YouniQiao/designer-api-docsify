# addAllowedHotspotClientList

## 导入模块

```TypeScript
import { wifiManager } from '@kit.MDMKit';
```

## addAllowedHotspotClientList

```TypeScript
function addAllowedHotspotClientList(macAddresses: Array<string>): void
```

添加网络共享MAC地址。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-wifiManager-function addAllowedHotspotClientList(macAddresses: Array<string>): void--><!--Device-wifiManager-function addAllowedHotspotClientList(macAddresses: Array<string>): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| macAddresses | Array&lt;string&gt; | 是 | 添加允许连接热点的设备可用名单。<br>最大长度为1000。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) | The administrator application does not have permission to manage the device. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) | Parameter verification failed. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-服务超时) | Service timeout. |
| [9200019](../errorcode-enterpriseDeviceManager.md#9200019-策略列表超限) | The policy list has exceeded the limit. |
