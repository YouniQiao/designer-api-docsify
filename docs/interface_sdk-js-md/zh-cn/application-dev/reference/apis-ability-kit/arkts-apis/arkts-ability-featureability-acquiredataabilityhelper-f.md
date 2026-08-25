# acquireDataAbilityHelper

## 导入模块

```TypeScript
import { featureAbility } from 'kits/@kit.AbilityKit';
```

## acquireDataAbilityHelper

```TypeScript
function acquireDataAbilityHelper(uri: string): DataAbilityHelper
```

获取dataAbilityHelper对象。

> **说明：**&gt;
> 组件启动规则详见：[组件启动规则（FA模型）](../../../application-models/component-startup-rules-fa.md)。&gt;
> 跨应用访问dataAbility，对端应用需配置关联启动。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityHelper](arkts-ability-dataabilityhelper-dataabilityhelper-i.md) |
