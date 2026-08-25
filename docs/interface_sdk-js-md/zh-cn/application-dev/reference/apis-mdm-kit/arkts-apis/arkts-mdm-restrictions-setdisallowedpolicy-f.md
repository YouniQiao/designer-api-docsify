# setDisallowedPolicy

## 导入模块

```TypeScript
import { restrictions } from 'kits/@kit.MDMKit';
```

## setDisallowedPolicy

```TypeScript
function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void
```

设置禁用/启用某特性。

> **说明：**&gt;
> 本接口为设备级禁用策略，影响设备所有用户。如需针对特定用户设置禁用策略，请使用
> [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md)接口。

**起始版本：** 12

**废弃版本：** 26.0.0

**替代接口：** [setDisallowedPolicy](#setdisallowedpolicy)(admin: Want, feature: FeatureForDevice, disallow: boolean)

**需要权限：** 
- API版本20+：ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS or ohos.permission.ENTERPRISE_MANAGE_NETWORK
- API版本15 - 19：ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS
- API版本12 - 14：ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| [feature](../../apis-multimodal-awareness-kit/arkts-apis/arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md) | string | 是 |
| disallow | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200013](../errorcode-enterpriseDeviceManager.md#9200013-管控未实时生效) |


## setDisallowedPolicy

```TypeScript
function setDisallowedPolicy(admin: Want, feature: FeatureForDevice, disallow: boolean): void
```

设置禁用/启用指定设备特性，禁用后相关设备特性无法被使用。

**起始版本：** 24

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| [feature](../../apis-multimodal-awareness-kit/arkts-apis/arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md) | [FeatureForDevice](arkts-mdm-restrictions-featurefordevice-e.md) | 是 |
| disallow | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-策略冲突) |
| [9200013](../errorcode-enterpriseDeviceManager.md#9200013-管控未实时生效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
