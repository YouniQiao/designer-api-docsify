# getDomainFilterRules

## 导入模块

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## getDomainFilterRules

```TypeScript
function getDomainFilterRules(admin: Want): Array<DomainFilterRule>
```

查询设备域名过滤规则。适用于企业网络安全审计场景，例如检查当前域名过滤策略配置、审计域名访问控制规则、验证域名过滤规则是否正确执行、排查域名访问问题，帮助企业审核和验证域名访问控制策略，确保网络访问控制符合安全要求。API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。从API version 23开始，支持[LogType](arkts-mdm-networkmanager-logtype-e.md)。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[DomainFilterRule](arkts-mdm-networkmanager-domainfilterrule-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
