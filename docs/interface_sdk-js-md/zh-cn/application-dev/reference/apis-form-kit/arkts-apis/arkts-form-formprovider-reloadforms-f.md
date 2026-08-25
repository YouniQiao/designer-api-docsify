# reloadForms

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## reloadForms

```TypeScript
function reloadForms(context: UIAbilityContext, moduleName: string, abilityName: string, formName: string): Promise<number>
```

对于当前应用中moduleName、abilityName、formName相同的卡片，每次加桌会分配不同的卡片ID。卡片提供方可通过本接口批量更新这些卡片。与reloadAllForms相比，本接口可精确指定更新特定配置的卡片， 适用于仅需更新特定卡片场景；reloadAllForms更新当前应用所有已加桌卡片，适用于全局刷新场景。本接口在应用主进程中调用，通知FormExtension进程进行批量更新，仅支持在 [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md)中使用，使用Promise异步回调。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) | 是 |
| moduleName | string | 是 |
| abilityName | string | 是 |
| formName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
