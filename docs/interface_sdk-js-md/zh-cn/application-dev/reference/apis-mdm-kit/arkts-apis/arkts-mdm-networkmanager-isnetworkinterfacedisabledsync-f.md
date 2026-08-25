# isNetworkInterfaceDisabledSync

## 导入模块

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## isNetworkInterfaceDisabledSync

```TypeScript
function isNetworkInterfaceDisabledSync(admin: Want, networkInterface: string): boolean
```

查询指定网络接口是否被禁用。适用于企业网络管理场景，例如检查网络接口状态、审计网络接口使用情况、验证网络策略执行效果，帮助企业确认网络接口管理策略是否生效，便于策略调整和问题排查。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| networkInterface | string | 是 |

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
| [401](../../errorcode-universal.md#401-参数检查失败) |


## isNetworkInterfaceDisabledSync

```TypeScript
function isNetworkInterfaceDisabledSync(admin: Want | null, networkInterface: string): boolean
```

查询指定网络接口是否被禁用。适用于企业网络管理场景，例如检查网络接口状态、审计网络接口使用情况、验证网络策略执行效果，帮助企业确认网络接口管理策略是否生效，便于策略调整和问题排查。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | 是 |
| networkInterface | string | 是 |

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
