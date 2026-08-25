# removeAllStartupTaskResults

## 导入模块

```TypeScript
import { startupManager } from 'kits/@kit.AbilityKit';
```

## removeAllStartupTaskResults

```TypeScript
function removeAllStartupTaskResults(): void
```

删除所有启动任务结果。 如果存在so预加载任务，则将对应so文件置为未加载状态。对于缓存中已加载的so文件，不会被移除。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppStartup
