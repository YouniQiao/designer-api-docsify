# queryEntityInfo（系统接口）

## 导入模块

```TypeScript
import { insightIntentDriver } from 'kits/@kit.AbilityKit';
```

## queryEntityInfo

```TypeScript
function queryEntityInfo(param: QueryParam): Promise<Array<Record<string, Object>>>
```

查询意图实体信息。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.EXECUTE_INSIGHT_INTENT

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| param | [QueryParam](arkts-ability-insightintentdriver-queryparam-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;Record & lt;string, Object & gt; & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
