# connectAbility

## 导入模块

```TypeScript
import { particleAbility } from 'kits/@kit.AbilityKit';
```

## connectAbility

```TypeScript
function connectAbility(request: Want, options: ConnectOptions): number
```

将当前ability与指定的ServiceAbility进行连接。

> **说明：**&gt;
> 组件启动规则详见：[组件启动规则（FA模型）](../../../application-models/component-startup-rules-fa.md)。
> 
> 跨应用连接serviceAbility，对端应用需配置关联启动。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |
