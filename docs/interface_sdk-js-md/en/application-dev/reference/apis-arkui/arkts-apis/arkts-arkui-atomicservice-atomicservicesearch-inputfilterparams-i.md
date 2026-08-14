# InputFilterParams

Sets regular expression for input filtering.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-export interface InputFilterParams--><!--Device-unnamed-export interface InputFilterParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceSearch } from 'AtomicServiceSearch';
import { InputFilterParams } from 'InputFilterParams';
import { SearchButtonParams } from 'SearchButtonParams';
import { MenuAlignParams } from 'MenuAlignParams';
import { SearchParams } from 'SearchParams';
import { SelectParams } from 'SelectParams';
import { OperationParams } from 'OperationParams';
```

## error

```TypeScript
error?: Callback<string>
```

Callback used to return the filtered-out content when regular expression matching fails. Default value: **undefined**.

**Type:** Callback&lt;string&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-InputFilterParams-error?: Callback<string>--><!--Device-InputFilterParams-error?: Callback<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## inputFilterValue

```TypeScript
inputFilterValue: ResourceStr
```

Regular expression.

**Type:** ResourceStr

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-InputFilterParams-inputFilterValue: ResourceStr--><!--Device-InputFilterParams-inputFilterValue: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

