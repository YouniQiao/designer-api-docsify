# CaretOffsetsCallback

```TypeScript
type CaretOffsetsCallback = (offset: double, index: int, leadingEdge: boolean) => boolean
```

Defines the callback used to receive the offset and index of each character in a text line object as its parameters.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：double | Yes |
| index | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |
| leadingEdge | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
