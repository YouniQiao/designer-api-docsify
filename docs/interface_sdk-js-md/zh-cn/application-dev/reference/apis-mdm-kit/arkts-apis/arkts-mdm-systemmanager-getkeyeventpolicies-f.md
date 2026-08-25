# getKeyEventPolicies

## 导入模块

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## getKeyEventPolicies

```TypeScript
function getKeyEventPolicies(admin: Want): Array<KeyEventPolicy>
```

获取按键事件处理策略。适用于需要查询当前按键事件处理策略配置的场景，帮助企业管理员验证策略是否正确下发，或在进行策略调整前获取当前配置。

**起始版本：** 23

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[KeyEventPolicy](arkts-mdm-systemmanager-keyeventpolicy-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |


## getKeyEventPolicies

```TypeScript
function getKeyEventPolicies(admin: Want | null): Array<KeyEventPolicy>
```

获取按键事件处理策略。适用于需要查询当前按键事件处理策略配置的场景，帮助企业管理员验证策略是否正确下发，或在进行策略调整前获取当前配置。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[KeyEventPolicy](arkts-mdm-systemmanager-keyeventpolicy-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
