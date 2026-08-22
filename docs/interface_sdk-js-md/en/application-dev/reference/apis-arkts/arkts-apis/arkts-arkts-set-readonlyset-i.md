# ReadonlySet

ReadonlySet implementation.

**Inheritance/Implementation:** ReadonlySet extends Iterable<T>

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export interface ReadonlySet--><!--Device-unnamed-export interface ReadonlySet-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { HashSet } from '@kit.ArkTS';
import { HashSetCbFn } from '@kit.ArkTS';
import { LightWeightSet } from '@kit.ArkTS';
import { LightWeightSetForEachCb } from '@kit.ArkTS';
import { TreeSet } from '@kit.ArkTS';
import { TreeSetForEachCb } from '@kit.ArkTS';
import { TreeSetComparator } from '@kit.ArkTS';
```

## has

```TypeScript
has(value: T): boolean
```

Checks if a value is in the Set.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReadonlySet-has(value: T): boolean--><!--Device-ReadonlySet-has(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | the value to find in the Set. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the value is in the Set. |

