# @ohos.app.ability.appMemoryOptimizer

appMemoryOptimizer提供应用内存优化的能力，包括释放指定文件的文件页缓存、释放指定模块的文件页缓存等。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace appMemoryOptimizer--><!--Device-unnamed-declare namespace appMemoryOptimizer-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { appMemoryOptimizer } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [evictFilePages](arkts-ability-appmemoryoptimizer-evictfilepages-f.md#evictfilepages) | 向系统发出释放指定文件的文件页缓存请求，系统会根据当前内存状况决定是否真正执行释放，不保证一定释放成功。 |
| [evictModuleFilePages](arkts-ability-appmemoryoptimizer-evictmodulefilepages-f.md#evictmodulefilepages) | 向系统发出释放指定模块的文件页缓存请求，系统会根据当前内存状况决定是否真正执行释放，不保证一定释放成功。系统会读取对应模块中的memory_optimizer.json配置文件，获取evictFilePages数组，然后对数组中的文件执行文件页缓存释放操作。  配置文件路径：{模块目录}/src/main/resources/rawfile/memory_optimizer.json配置文件中evictFilePages数组里的文件名必须以 .so、.hap 或 .hsp 结尾。 |

