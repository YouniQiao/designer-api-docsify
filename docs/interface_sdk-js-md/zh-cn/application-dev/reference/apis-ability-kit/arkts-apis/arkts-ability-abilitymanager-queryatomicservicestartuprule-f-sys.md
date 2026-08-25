# queryAtomicServiceStartupRule（系统接口）

## 导入模块

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## queryAtomicServiceStartupRule

```TypeScript
function queryAtomicServiceStartupRule(context: Context, appId: string): Promise<AtomicServiceStartupRule>
```

查询嵌入式拉起[EmbeddableUIAbility](arkts-ability-app-ability-embeddableuiability-embeddableuiability-c.md)的规则。使用Promise异步回调。 该接口仅在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | 是 |
| appId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AtomicServiceStartupRule](arkts-ability-abilitymanager-atomicservicestartuprule-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
