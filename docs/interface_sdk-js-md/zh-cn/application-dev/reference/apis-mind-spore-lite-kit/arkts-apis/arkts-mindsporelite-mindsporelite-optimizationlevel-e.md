# OptimizationLevel

Enum for optimization level

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-mindSporeLite-export enum OptimizationLevel--><!--Device-mindSporeLite-export enum OptimizationLevel-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## O0

```TypeScript
O0 = 0
```

Do not change

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OptimizationLevel-O0 = 0--><!--Device-OptimizationLevel-O0 = 0-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## O2

```TypeScript
O2 = 2
```

Cast network to float16, keep batch norm and loss in float32

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OptimizationLevel-O2 = 2--><!--Device-OptimizationLevel-O2 = 2-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## O3

```TypeScript
O3 = 3
```

Cast network to float16, including batch norm

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OptimizationLevel-O3 = 3--><!--Device-OptimizationLevel-O3 = 3-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## AUTO

```TypeScript
AUTO = 4
```

Choose optimization based on device

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OptimizationLevel-AUTO = 4--><!--Device-OptimizationLevel-AUTO = 4-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

