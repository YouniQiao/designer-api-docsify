# stringify

## Modules to Import

```TypeScript
import { ArkTSUtils } from 'kits/@kit.ArkTS';
```

## stringify

```TypeScript
function stringify(value: Object | null | undefined): string
```

该方法将ArkTS对象数据转换为JSON字符串，额外支持Map和Set相关类型。

从API 18开始参数修改为Object类型，API 18之前参数只支持ISendable类型（除Int8Array、Uint8Array、Int16Array、Uint16Array、Int32Array、Uint32Array、Uint8ClampedArray、Float32Array外）。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ASON-function stringify(value: Object | null | undefined): string--><!--Device-ASON-function stringify(value: Object | null | undefined): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object \| null \| undefined | Yes | ArkTS对象数据。<br>**Since:** 18 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 转换后的JSON字符串。 |

