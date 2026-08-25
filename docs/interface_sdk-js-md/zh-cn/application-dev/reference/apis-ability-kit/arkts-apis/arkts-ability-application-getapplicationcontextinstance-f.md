# getApplicationContextInstance

## 导入模块

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## getApplicationContextInstance

```TypeScript
export function getApplicationContextInstance(): ApplicationContext
```

获取应用上下文实例。开发者使用该接口时，无需依赖Context基类。 重复调用该接口，将获取同一个ApplicationContext实例。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| [ApplicationContext](arkts-ability-applicationcontext-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
