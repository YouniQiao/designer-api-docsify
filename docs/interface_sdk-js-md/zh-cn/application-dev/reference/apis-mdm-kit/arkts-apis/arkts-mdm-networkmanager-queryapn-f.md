# queryApn

## 导入模块

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## queryApn

```TypeScript
function queryApn(admin: Want, apnInfo: Record<string, string>): Array<string>
```

查询符合特定APN信息的APN ID。适用于企业移动网络配置审计场景，例如查找特定配置的APN、验证APN配置是否存在、为APN管理操作提供APN ID参数，帮助企业查找和管理APN配置，为APN的更新和删除操作提供必要的参数信 息。

**起始版本：** 20

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APN

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| apnInfo | Record & lt;string, string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |


## queryApn

```TypeScript
function queryApn(admin: Want, apnId: string): Record<string, string>
```

查询特定APN的APN参数信息。适用于企业移动网络配置审计场景，例如检查特定APN的配置参数、验证APN配置是否正确、审计移动网络接入点配置，帮助企业审核和验证APN配置，确保移动网络配置符合要求。

**起始版本：** 20

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APN

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| apnId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Record & lt;string, string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
