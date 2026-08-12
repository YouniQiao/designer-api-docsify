# CpuDevice

Provides the CPU device info

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-mindSporeLite-interface CpuDevice--><!--Device-mindSporeLite-interface CpuDevice-End-->

**System capability:** SystemCapability.AI.MindSporeLite

## Modules to Import

```TypeScript
import { mindSporeLite } from '@kit.MindSporeLiteKit';
```

## precisionMode

```TypeScript
precisionMode?: string
```

The precision mode

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CpuDevice-precisionMode?: string--><!--Device-CpuDevice-precisionMode?: string-End-->

**System capability:** SystemCapability.AI.MindSporeLite

## threadAffinityCoreList

```TypeScript
threadAffinityCoreList?: int[]
```

The thread affinity core list

**Type:** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CpuDevice-threadAffinityCoreList?: int[]--><!--Device-CpuDevice-threadAffinityCoreList?: int[]-End-->

**System capability:** SystemCapability.AI.MindSporeLite

## threadAffinityMode

```TypeScript
threadAffinityMode?: ThreadAffinityMode
```

The thread affinity mode

**Type:** [ThreadAffinityMode](arkts-mindsporelite-mindsporelite-threadaffinitymode-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CpuDevice-threadAffinityMode?: ThreadAffinityMode--><!--Device-CpuDevice-threadAffinityMode?: ThreadAffinityMode-End-->

**System capability:** SystemCapability.AI.MindSporeLite

## threadNum

```TypeScript
threadNum?: int
```

The thread num

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CpuDevice-threadNum?: int--><!--Device-CpuDevice-threadNum?: int-End-->

**System capability:** SystemCapability.AI.MindSporeLite

