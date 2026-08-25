# @ohos.app.ability.appMemoryOptimizer

appMemoryOptimizer提供应用内存优化的能力，包括释放指定文件的文件页缓存、释放指定模块的文件页缓存等。 例如，应用进入后台或设备内存紧张时，调用evictFilePages释放已加载文件的文件页缓存，可降低应用自身的内存占用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { appMemoryOptimizer } from '@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [evictFilePages](arkts-ability-appmemoryoptimizer-evictfilepages-f.md) |
| [evictModuleFilePages](arkts-ability-appmemoryoptimizer-evictmodulefilepages-f.md) |
