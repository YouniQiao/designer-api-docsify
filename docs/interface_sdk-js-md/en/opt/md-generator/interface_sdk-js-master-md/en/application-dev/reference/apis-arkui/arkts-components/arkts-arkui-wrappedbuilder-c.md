# WrappedBuilder

Defines the WrappedBuilder class.

**Since:** 11

**Deprecated since:** -1

<!--Device-unnamed-declare class WrappedBuilder--><!--Device-unnamed-declare class WrappedBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(builder: (...args: Args) => void)
```

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WrappedBuilder-constructor(builder: (...args: Args) => void)--><!--Device-WrappedBuilder-constructor(builder: (...args: Args) => void)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [builder](#builder) | (...args: Args) = & gt; void | Yes |

## Examples

```TypeScript
@Builder
function MyBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
}
let builderVar: WrappedBuilder<[string, number]> = new WrappedBuilder<[string, number]>(MyBuilder);
```

## builder

```TypeScript
builder: (...args: Args) => void
```

**Type:** (...args: Args) =&gt; void

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WrappedBuilder-builder: (...args: Args) => void--><!--Device-WrappedBuilder-builder: (...args: Args) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
