# DecodeWithStreamOptions

定义解码是否跟随数据块。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-util-interface DecodeWithStreamOptions--><!--Device-util-interface DecodeWithStreamOptions-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## stream

```TypeScript
stream?: boolean
```

是否允许后续的 **decodeWithStream()** 处理数据块。如果按块处理数据，请将此参数设置为 **true**。如果这是要处理的最后一个数据块或数据未分块，请将此参数设置为 **false**。默认值为 **false**。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DecodeWithStreamOptions-stream?: boolean--><!--Device-DecodeWithStreamOptions-stream?: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

