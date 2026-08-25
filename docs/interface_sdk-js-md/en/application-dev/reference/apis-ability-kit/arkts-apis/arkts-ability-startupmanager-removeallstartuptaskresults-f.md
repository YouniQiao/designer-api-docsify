# removeAllStartupTaskResults

## Modules to Import

```TypeScript
import { startupManager } from 'kits/@kit.AbilityKit';
```

## removeAllStartupTaskResults

```TypeScript
function removeAllStartupTaskResults(): void
```

Removes all startup task results. If there are preloading tasks for .so files, the corresponding .so files is set to the unloaded state. However, .so files that have already been loaded in the cache will not be removed.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AppStartup
