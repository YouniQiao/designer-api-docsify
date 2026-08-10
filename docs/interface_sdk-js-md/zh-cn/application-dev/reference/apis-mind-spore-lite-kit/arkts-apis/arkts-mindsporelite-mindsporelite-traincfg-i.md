# TrainCfg

Provides the train configuration

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-mindSporeLite-interface TrainCfg--><!--Device-mindSporeLite-interface TrainCfg-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## 导入模块

```TypeScript
import { mindSporeLite } from 'kits/@kit.MindSporeLiteKit';
```

## lossName

```TypeScript
lossName?: string[]
```

Array of loss name

**类型：** string[]

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrainCfg-lossName?: string[]--><!--Device-TrainCfg-lossName?: string[]-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## optimizationLevel

```TypeScript
optimizationLevel?: OptimizationLevel
```

Train optimization level

**类型：** [OptimizationLevel](arkts-mindsporelite-mindsporelite-optimizationlevel-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TrainCfg-optimizationLevel?: OptimizationLevel--><!--Device-TrainCfg-optimizationLevel?: OptimizationLevel-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

