# concat

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## concat

```TypeScript
function concat(list: Buffer[] | Uint8Array[], totalLength?: number): Buffer
```

Concatenates an array of **Buffer** objects of the specified length into a new object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| list | Buffer[] \| Uint8Array[] | Yes |
| [totalLength](../../apis-arkui/arkts-components/arkts-arkui-computedbarattribute-i.md) | number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Buffer |

**Error codes:**

| Error Code ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-value-out-of-range) |
