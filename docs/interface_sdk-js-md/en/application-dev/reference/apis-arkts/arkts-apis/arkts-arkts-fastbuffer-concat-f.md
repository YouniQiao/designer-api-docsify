# concat

## Modules to Import

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## concat

```TypeScript
function concat(list: FastBuffer[] | Uint8Array[], totalLength?: number): FastBuffer
```

Returns a new `FastBuffer` which is the result of concatenating all the `FastBuffer`instances in the `list` together.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| list | [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md)[] \| Uint8Array[] | Yes |
| [totalLength](../../apis-arkui/arkts-components/arkts-arkui-computedbarattribute-i.md) | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |
