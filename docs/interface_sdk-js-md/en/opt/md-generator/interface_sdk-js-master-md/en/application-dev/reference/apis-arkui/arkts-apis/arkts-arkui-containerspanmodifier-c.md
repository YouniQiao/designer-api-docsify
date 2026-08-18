# ContainerSpanModifier

Defines ContainerSpan modifier, the base class for quick use modifier ability

**Inheritance/Implementation:** ContainerSpanModifier extends ContainerSpanAttribute and implements AttributeModifier<ContainerSpanAttribute>

**Since:** 12

<!--Device-unnamed-export declare class ContainerSpanModifier--><!--Device-unnamed-export declare class ContainerSpanModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyNormalAttribute

```TypeScript
applyNormalAttribute?(containerSpanAttribute: ContainerSpanAttribute): void
```

Defines the normal update attribute function.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ContainerSpanModifier-applyNormalAttribute?(containerSpanAttribute: ContainerSpanAttribute): void--><!--Device-ContainerSpanModifier-applyNormalAttribute?(containerSpanAttribute: ContainerSpanAttribute): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| containerSpanAttribute | ContainerSpanAttribute | Yes |
