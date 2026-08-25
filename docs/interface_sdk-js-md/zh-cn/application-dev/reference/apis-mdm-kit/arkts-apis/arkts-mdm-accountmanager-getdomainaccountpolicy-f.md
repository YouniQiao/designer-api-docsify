# getDomainAccountPolicy

## 导入模块

```TypeScript
import { accountManager } from 'kits/@kit.MDMKit';
```

## getDomainAccountPolicy

```TypeScript
function getDomainAccountPolicy(admin: Want, domainAccountInfo: osAccount.DomainAccountInfo): DomainAccountPolicy
```

获取域账号策略。适用于企业管理场景，如查询当前域账号策略配置、策略合规性审计等。

**起始版本：** 19

**需要权限：** ohos.permission.ENTERPRISE_SET_ACCOUNT_POLICY

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| [domainAccountInfo](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | osAccount.DomainAccountInfo | 是 |

**返回值：**

| 类型 |
| --- |
| [DomainAccountPolicy](arkts-mdm-accountmanager-domainaccountpolicy-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
