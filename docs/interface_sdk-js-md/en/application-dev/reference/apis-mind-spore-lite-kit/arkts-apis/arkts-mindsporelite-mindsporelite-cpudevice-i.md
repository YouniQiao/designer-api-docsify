# CpuDevice

Provides the CPU device info

**Since:** 10

**System capability:** SystemCapability.AI.MindSporeLite

## Modules to Import

```TypeScript
import mindSporeLite from '@kit.MindSporeLiteKit';
```

## precisionMode

```TypeScript
precisionMode?: string
```

The precision mode

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

## threadAffinityCoreList

```TypeScript
threadAffinityCoreList?: number[]
```

The thread affinity core list

**Type:** number[]

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

## threadAffinityMode

```TypeScript
threadAffinityMode?: ThreadAffinityMode
```

The thread affinity mode

**Type:** [ThreadAffinityMode](arkts-mindsporelite-mindsporelite-threadaffinitymode-e.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

## threadNum

```TypeScript
threadNum?: number
```

The thread num

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Examples**

```TypeScript
let context: mindSporeLite.Context = {};
context.cpu = {};
context.target = ['cpu'];
context.cpu.threadNum = 2;
context.cpu.threadAffinityMode = 0;
context.cpu.precisionMode = 'preferred_fp16';
context.cpu.threadAffinityCoreList = [0, 1, 2];
```
