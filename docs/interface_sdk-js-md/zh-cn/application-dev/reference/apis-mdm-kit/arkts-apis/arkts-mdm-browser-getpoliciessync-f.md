# getPoliciesSync

## 导入模块

```TypeScript
import { browser } from 'kits/@kit.MDMKit';
```

## getPoliciesSync

```TypeScript
function getPoliciesSync(admin: Want, appId: string): string
```

通过appid获取指定浏览器设置的策略，适用于查询当前浏览器策略配置的场景，例如在企业设备管理应用中展示策略详情、验证策略是否生效等。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| appId | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getPoliciesSync

```TypeScript
function getPoliciesSync(admin: Want | null, appId: string): string
```

通过appid获取指定浏览器设置的策略，适用于查询当前浏览器策略配置的场景，例如在企业设备管理应用中展示策略详情、验证策略是否生效等。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | 是 |
| appId | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
