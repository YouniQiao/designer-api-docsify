# InputFilterParams

Sets regular expression for input filtering.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-export interface InputFilterParams--><!--Device-unnamed-export interface InputFilterParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SearchParams, AtomicServiceSearch, SearchButtonParams, OperationParams, SelectParams, InputFilterParams, MenuAlignParams } from 'kits/@kit.ArkUI';
```

## error

```TypeScript
error?: Callback<string>
```

Callback used to return the filtered-out content when regular expression matching fails. Default value:  
**undefined**.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-InputFilterParams-error?: Callback<string>--><!--Device-InputFilterParams-error?: Callback<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## inputFilterValue

```TypeScript
inputFilterValue: ResourceStr
```

Regular expression.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-InputFilterParams-inputFilterValue: ResourceStr--><!--Device-InputFilterParams-inputFilterValue: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

