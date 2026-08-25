# setRestartWant

## 导入模块

```TypeScript
import { appRecovery } from 'kits/@kit.AbilityKit';
```

## setRestartWant

```TypeScript
function setRestartWant(want: Want): void
```

设置下次恢复主动拉起场景下的Ability。该Ability必须为当前包下的UIAbility。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
