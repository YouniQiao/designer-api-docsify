# MultithreadingDetectionOptions

Multi-thread detection functional parameter configuration

**Since:** 26.0.0

<!--Device-util-interface MultithreadingDetectionOptions--><!--Device-util-interface MultithreadingDetectionOptions-End-->

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

## abort

```TypeScript
abort?: boolean
```

If abort is **true**, the application will crash, if abort is **false**, the application will not crash. Default **true**.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultithreadingDetectionOptions-abort?: boolean--><!--Device-MultithreadingDetectionOptions-abort?: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## frequency

```TypeScript
frequency?: number
```

The sampling frequency of multi-thread detection The value must be an integer, minimum is **100**, maximum is **2147483647**. (default **100**) The value should be an integer.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultithreadingDetectionOptions-frequency?: number--><!--Device-MultithreadingDetectionOptions-frequency?: number-End-->

**System capability:** SystemCapability.Utils.Lang

## interval

```TypeScript
interval?: number
```

The interval of multi-thread detection(min) Errors will be reported again only if the time since the last detection exceeds this interval. The value must be an integer within [0,1440] (default 5min).

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultithreadingDetectionOptions-interval?: number--><!--Device-MultithreadingDetectionOptions-interval?: number-End-->

**System capability:** SystemCapability.Utils.Lang

