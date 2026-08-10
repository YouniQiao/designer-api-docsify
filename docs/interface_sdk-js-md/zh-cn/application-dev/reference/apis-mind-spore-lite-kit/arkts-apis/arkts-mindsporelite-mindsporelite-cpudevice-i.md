# CpuDevice

Provides the CPU device info

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-mindSporeLite-interface CpuDevice--><!--Device-mindSporeLite-interface CpuDevice-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## 导入模块

```TypeScript
import { mindSporeLite } from 'kits/@kit.MindSporeLiteKit';
```

## precisionMode

```TypeScript
precisionMode?: string
```

The precision mode

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CpuDevice-precisionMode?: string--><!--Device-CpuDevice-precisionMode?: string-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## threadAffinityCoreList

```TypeScript
threadAffinityCoreList?: int[]
```

The thread affinity core list

**类型：** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CpuDevice-threadAffinityCoreList?: int[]--><!--Device-CpuDevice-threadAffinityCoreList?: int[]-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## threadAffinityMode

```TypeScript
threadAffinityMode?: ThreadAffinityMode
```

The thread affinity mode

**类型：** [ThreadAffinityMode](arkts-mindsporelite-mindsporelite-threadaffinitymode-e.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CpuDevice-threadAffinityMode?: ThreadAffinityMode--><!--Device-CpuDevice-threadAffinityMode?: ThreadAffinityMode-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## threadNum

```TypeScript
threadNum?: int
```

The thread num

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CpuDevice-threadNum?: int--><!--Device-CpuDevice-threadNum?: int-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

