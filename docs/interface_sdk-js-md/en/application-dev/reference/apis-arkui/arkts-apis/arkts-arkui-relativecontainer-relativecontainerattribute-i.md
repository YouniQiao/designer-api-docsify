# RelativeContainerAttribute

The RelativeContainerAttribute.@extends CommonMethod @interface RelativeContainerAttribute

**Inheritance/Implementation:** RelativeContainerAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RelativeContainerAttribute> | AttributeModifier<CommonMethod>
        | undefined): this
```

Set the attribute modifier

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md) |

## barrier

```TypeScript
default barrier(barrierStyle: Array<BarrierStyle> | Array<LocalizedBarrierStyle> | undefined): this
```

Specifies barriers of relativeContainer

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| barrierStyle | Array&lt;[BarrierStyle](arkts-arkui-relativecontainer-barrierstyle-i.md)&gt; \| Array&lt;[LocalizedBarrierStyle](arkts-arkui-relativecontainer-localizedbarrierstyle-i.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md) |

## guideLine

```TypeScript
default guideLine(value: Array<GuideLineStyle> | undefined): this
```

Specifies guideLines of relativeContainer

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Array&lt;[GuideLineStyle](arkts-arkui-relativecontainer-guidelinestyle-i.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md) |

## setRelativeContainerOptions

```TypeScript
default setRelativeContainerOptions(): this
```

Set RelativeContainer options.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RelativeContainerAttribute](arkts-arkui-relativecontainer-relativecontainerattribute-i.md) |
