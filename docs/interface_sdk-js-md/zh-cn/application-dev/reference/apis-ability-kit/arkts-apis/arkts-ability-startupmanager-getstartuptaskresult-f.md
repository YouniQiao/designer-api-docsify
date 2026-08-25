# getStartupTaskResult

## 导入模块

```TypeScript
import { startupManager } from 'kits/@kit.AbilityKit';
```

## getStartupTaskResult

```TypeScript
function getStartupTaskResult(startupTask: string): Object
```

获取指定启动任务或so预加载任务的执行结果。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startupTask | string | 是 |

**返回值：**

| 类型 |
| --- |
| Object |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
