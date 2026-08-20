# HeapMemoryThreshold

Describes the heap memory threshold at which the registered callback is triggered after a GC.

@interface HeapMemoryThreshold

**Since:** 24

<!--Device-util-interface HeapMemoryThreshold--><!--Device-util-interface HeapMemoryThreshold-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { ArrayList } from '@kit.ArkTS';
import { ArrayListComparatorFn } from '@kit.ArkTS';
import { ArrayListForEachCb } from '@kit.ArkTS';
import { ArrayListReplaceCb } from '@kit.ArkTS';
import { util } from '@kit.ArkTS';
import { Deque } from '@kit.ArkTS';
import { DequeForEachCb } from '@kit.ArkTS';
import { HashMap } from '@kit.ArkTS';
import { HashMapCbFn } from '@kit.ArkTS';
import { HashSet } from '@kit.ArkTS';
import { HashSetCbFn } from '@kit.ArkTS';
import { LightWeightMap } from '@kit.ArkTS';
import { LightWeightMapCbFn } from '@kit.ArkTS';
import { LightWeightSet } from '@kit.ArkTS';
import { LightWeightSetForEachCb } from '@kit.ArkTS';
import { LinkedList } from '@kit.ArkTS';
import { LinkedListForEachCb } from '@kit.ArkTS';
import { List } from '@kit.ArkTS';
import { ListComparatorFn } from '@kit.ArkTS';
import { ListForEachCb } from '@kit.ArkTS';
import { ListReplaceCb } from '@kit.ArkTS';
import { PlainArray } from '@kit.ArkTS';
import { PlainArrayForEachCb } from '@kit.ArkTS';
import { Queue } from '@kit.ArkTS';
import { QueueForEachCb } from '@kit.ArkTS';
import { Stack } from '@kit.ArkTS';
import { StackForEachCb } from '@kit.ArkTS';
import { TreeMap } from '@kit.ArkTS';
import { TreeMapForEachCb } from '@kit.ArkTS';
import { TreeMapComparator } from '@kit.ArkTS';
import { TreeSet } from '@kit.ArkTS';
import { TreeSetForEachCb } from '@kit.ArkTS';
import { TreeSetComparator } from '@kit.ArkTS';
import { stream } from '@kit.ArkTS';
import { Vector } from '@kit.ArkTS';
import { JSON } from '@kit.ArkTS';
```

## localHeapThreshold

```TypeScript
localHeapThreshold?: number
```

This number is on a scale of 70 to 95, representing the percentage threshold of the local heap memory at which the callback is triggered after a GC. Values outside this range are automatically clamped to the valid range. If not set, the callback will not be triggered by local heap memory pressure.

**Type:** number

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeapMemoryThreshold-localHeapThreshold?: number--><!--Device-HeapMemoryThreshold-localHeapThreshold?: number-End-->

**System capability:** SystemCapability.Utils.Lang

## processHeapThreshold

```TypeScript
processHeapThreshold?: number
```

This number is on a scale of 70 to 95, representing the percentage threshold of the process's total heap memory at which the callback is triggered after a GC. Values outside this range are automatically clamped to the valid range. If not set, the callback will not be triggered by process heap memory pressure.

**Type:** number

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeapMemoryThreshold-processHeapThreshold?: number--><!--Device-HeapMemoryThreshold-processHeapThreshold?: number-End-->

**System capability:** SystemCapability.Utils.Lang

## sharedHeapThreshold

```TypeScript
sharedHeapThreshold?: number
```

This number is on a scale of 70 to 95, representing the percentage threshold of the shared heap memory at which the callback is triggered after a GC. Values outside this range are automatically clamped to the valid range. If not set, the callback will not be triggered by shared heap memory pressure.

**Type:** number

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeapMemoryThreshold-sharedHeapThreshold?: number--><!--Device-HeapMemoryThreshold-sharedHeapThreshold?: number-End-->

**System capability:** SystemCapability.Utils.Lang

