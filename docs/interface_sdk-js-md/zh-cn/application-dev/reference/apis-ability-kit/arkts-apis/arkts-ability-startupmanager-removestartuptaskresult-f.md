# removeStartupTaskResult

## 导入模块

```TypeScript
import { startupManager } from 'kits/@kit.AbilityKit';
```

## removeStartupTaskResult

```TypeScript
function removeStartupTaskResult(startupTask: string): void
```

删除指定启动任务或so预加载任务的初始化结果。  
- 输入为启动任务名时，删除指定启动任务的初始化结果。  
- 输入为so文件时，将该so文件置为未加载，缓存中已加载的so文件不会被移除。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startupTask | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
