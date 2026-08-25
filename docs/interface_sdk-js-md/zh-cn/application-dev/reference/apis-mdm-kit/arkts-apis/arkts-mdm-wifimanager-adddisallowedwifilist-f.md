# addDisallowedWifiList

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.MDMKit';
```

## addDisallowedWifiList

```TypeScript
function addDisallowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void
```

添加Wi-Fi禁用名单。添加禁用名单后当前设备不允许连接该名单下的Wi-Fi。适用于企业安全管控场景，例如禁止设备连接不安全的公共Wi-Fi(如咖啡馆、机场Wi-Fi)、防止员工连接竞争对手或恶意网络，保障企业数据安全。以下情况下，调用本接口会报策略冲突：
1. 已经通过[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)接口禁用了设备Wi-Fi能力。通过[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)解除Wi-Fi禁用后，可解除冲突。
2. 已经通过[addAllowedWifiList](arkts-mdm-wifimanager-addallowedwifilist-f.md)接口添加了Wi-Fi允许名单。通过[removeAllowedWifiList](arkts-mdm-wifimanager-removeallowedwifilist-f.md)移除Wi-Fi允许名单后，可解除冲突。

**起始版本：** 19

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| list | Array&lt;[WifiAccessInfo](arkts-mdm-wifimanager-wifiaccessinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-策略冲突) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
