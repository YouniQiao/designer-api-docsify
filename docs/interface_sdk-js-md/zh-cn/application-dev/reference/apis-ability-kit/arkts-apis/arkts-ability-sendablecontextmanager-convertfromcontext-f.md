# convertFromContext

## 导入模块

```TypeScript
import { sendableContextManager } from 'kits/@kit.AbilityKit';
```

## convertFromContext

```TypeScript
function convertFromContext(context: common.Context): SendableContext
```

将Context转换为SendableContext对象。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | common.Context | 是 |

**返回值：**

| 类型 |
| --- |
| [SendableContext](arkts-ability-sendablecontextmanager-sendablecontext-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
