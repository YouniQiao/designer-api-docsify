# removeFirewallRule

## 导入模块

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## removeFirewallRule

```TypeScript
function removeFirewallRule(admin: Want, firewallRule?: FirewallRule): void
```

移除设备防火墙过滤规则。适用于企业网络安全策略调整场景，例如取消某些网络访问限制、调整防火墙策略、清理过时或无效的规则，帮助企业灵活调整网络安全策略，确保网络访问控制策略与实际需求保持一致。API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。从API version 23开始，支持[LogType](arkts-mdm-networkmanager-logtype-e.md)。移除规则后如果不存在[Action](arkts-mdm-networkmanager-action-e.md)为ALLOW规则后，会将[addFirewallRule](arkts-mdm-networkmanager-addfirewallrule-f.md)添 加的默认DENY规则清空。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| firewallRule | [FirewallRule](arkts-mdm-networkmanager-firewallrule-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
