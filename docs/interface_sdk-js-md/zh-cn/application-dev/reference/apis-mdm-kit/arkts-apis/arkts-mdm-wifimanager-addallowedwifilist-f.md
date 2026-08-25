# addAllowedWifiList

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.MDMKit';
```

## addAllowedWifiList

```TypeScript
function addAllowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void
```

添加Wi-Fi允许名单。添加允许名单后当前设备仅允许连接该名单下的Wi-Fi。适用于企业安全管理场景，例如限制员工设备只能连接公司授权的Wi-Fi网络，防止连接不安全的外部Wi-Fi，保障企业网络安全和数据安全。以下情况下，调用本接口会报策略冲突：
1. 已经通过[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)接口禁用了设备Wi-Fi能力。通过[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)解除Wi-Fi禁用后，可解除冲突。
2. 已经通过[addDisallowedWifiList](arkts-mdm-wifimanager-adddisallowedwifilist-f.md)接口添加了Wi-Fi禁用名单。通过[removeDisallowedWifiList](arkts-mdm-wifimanager-removedisallowedwifilist-f.md)移除Wi-Fi禁用名单后，可解除冲突。

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
