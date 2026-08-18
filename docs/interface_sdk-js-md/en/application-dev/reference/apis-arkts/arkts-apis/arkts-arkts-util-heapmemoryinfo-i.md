# HeapMemoryInfo

Describes heap memory information of either an ArkTS-VM, or the shared heap memory of current process.

**Since:** 24

<!--Device-util-interface HeapMemoryInfo--><!--Device-util-interface HeapMemoryInfo-End-->

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

## heapObjectSize

```TypeScript
heapObjectSize: number
```

The value is a number representing the total size of all heap objects in KB, from either an ArkTS-VM local heap or the shared heap.

**Type:** number

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeapMemoryInfo-heapObjectSize: number--><!--Device-HeapMemoryInfo-heapObjectSize: number-End-->

**System capability:** SystemCapability.Utils.Lang

## heapType

```TypeScript
heapType: string
```

The value is a string representing whether this memory information is from an ArkTS-VM local heap, or the shared heap.

**Type:** string

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeapMemoryInfo-heapType: string--><!--Device-HeapMemoryInfo-heapType: string-End-->

**System capability:** SystemCapability.Utils.Lang

## threadId

```TypeScript
threadId?: number
```

If this memory information describes an ArkTS-VM local heap, the value is a number representing the running thread; If this memory information describes the shared heap, the value is undefined.

**Type:** number

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeapMemoryInfo-threadId?: number--><!--Device-HeapMemoryInfo-threadId?: number-End-->

**System capability:** SystemCapability.Utils.Lang

## threadName

```TypeScript
threadName?: string
```

If this memory information describes an ArkTS-VM local heap, the value is a string representing the name of the running thread; If this memory information describes the shared heap, the value is undefined.

**Type:** string

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeapMemoryInfo-threadName?: string--><!--Device-HeapMemoryInfo-threadName?: string-End-->

**System capability:** SystemCapability.Utils.Lang

