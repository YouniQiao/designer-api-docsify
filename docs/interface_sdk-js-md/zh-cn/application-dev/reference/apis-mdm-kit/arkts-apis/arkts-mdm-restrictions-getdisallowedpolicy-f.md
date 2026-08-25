# getDisallowedPolicy

## 导入模块

```TypeScript
import { restrictions } from 'kits/@kit.MDMKit';
```

## getDisallowedPolicy

```TypeScript
function getDisallowedPolicy(admin: Want | null, feature: string): boolean
```

查询某特性是否被禁用。

**起始版本：** 12

**废弃版本：** 26.0.0

**替代接口：** [getDisallowedPolicy](#getdisallowedpolicy)(admin: Want | null, feature: FeatureForDevice)

**需要权限：** 
- API版本20+：ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS or ohos.permission.ENTERPRISE_MANAGE_NETWORK
- API版本15 - 19：ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS
- API版本12 - 14：ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | 是 |
| [feature](../../apis-multimodal-awareness-kit/arkts-apis/arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |


## getDisallowedPolicy

```TypeScript
function getDisallowedPolicy(admin: Want | null, feature: FeatureForDevice): boolean
```

查询指定设备特性是否被禁用。

**起始版本：** 24

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | 是 |
| [feature](../../apis-multimodal-awareness-kit/arkts-apis/arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md) | [FeatureForDevice](arkts-mdm-restrictions-featurefordevice-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
