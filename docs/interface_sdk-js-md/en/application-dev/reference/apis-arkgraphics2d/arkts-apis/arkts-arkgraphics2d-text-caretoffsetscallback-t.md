# CaretOffsetsCallback

```TypeScript
type CaretOffsetsCallback = (offset: number, index: number, leadingEdge: boolean) => boolean
```

Defines the callback used to receive the offset and index of each character in a text line object as its parameters.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |
| index | number | Yes |
| leadingEdge | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
