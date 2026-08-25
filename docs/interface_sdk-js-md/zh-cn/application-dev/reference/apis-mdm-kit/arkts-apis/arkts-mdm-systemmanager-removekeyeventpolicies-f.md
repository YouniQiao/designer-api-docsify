# removeKeyEventPolicies

## 导入模块

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## removeKeyEventPolicies

```TypeScript
function removeKeyEventPolicies(admin: Want, keyCodes: Array<KeyCode>): void
```

删除按键事件处理策略。删除成功后，系统将恢复对指定按键事件的默认处理行为。适用于需要恢复按键默认行为的场景，帮助企业管理员灵活调整设备按键响应策略，满足不同业务场景的需求。

**起始版本：** 23

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| keyCodes | Array & lt;KeyCode & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
