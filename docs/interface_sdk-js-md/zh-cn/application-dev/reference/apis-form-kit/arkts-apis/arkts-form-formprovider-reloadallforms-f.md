# reloadAllForms

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## reloadAllForms

```TypeScript
function reloadAllForms(context: UIAbilityContext): Promise<number>
```

在应用主进程通过本接口可以通知FormExtension进程批量更新当前应用下已经加桌的所有卡片，仅支持在[UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md)中调用，使用Promise异步回 调。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
