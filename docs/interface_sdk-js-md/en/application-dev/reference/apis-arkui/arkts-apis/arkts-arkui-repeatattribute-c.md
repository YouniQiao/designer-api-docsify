# RepeatAttribute

In addition to the drag-and-drop sorting attribute, the following attributes are supported.

**Inheritance/Implementation:** RepeatAttribute extends DynamicNode<RepeatAttribute<T>>

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## each

```TypeScript
each(itemGenerator: (repeatItem: RepeatItem<T>) => void): RepeatAttribute<T>
```

Component generator. When the return value of [.templateId()](#templateid) does not match any [.template()](#template) type (that is, the current item does not match any defined template style), the data item is processed using **.each()**.

> **NOTE：**&gt;
> - The **each** property is mandatory. If it is omitted, runtime errors will occur.&gt;
> - The **itemGenerator** parameter is of the **RepeatItem** type, which combines **item** and **index**. Do not
> destructure **RepeatItem**.&gt;
> - This API cannot be called within attributeModifier.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| itemGenerator | (repeatItem: RepeatItem & lt;T & gt;) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md)&lt;T&gt; |

## key

```TypeScript
key(keyGenerator: (item: T, index: number) => string): RepeatAttribute<T>
```

Key generator.

> **NOTE：**&gt;
> This API cannot be called within attributeModifier.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyGenerator | (item: T, index: number) = & gt; string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md)&lt;T&gt; |

## template

```TypeScript
template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions): RepeatAttribute<T>
```

Renders the corresponding template child component based on the template type.

> **NOTE：**&gt;
> This API cannot be called within attributeModifier.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| itemBuilder | [RepeatItemBuilder](arkts-arkui-repeatitembuilder-t.md)&lt;T&gt; | Yes |
| templateOptions | [TemplateOptions](arkts-arkui-templateoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md)&lt;T&gt; |

## templateId

```TypeScript
templateId(typedFunc: TemplateTypedFunc<T>): RepeatAttribute<T>
```

Assigns a template type for this data item.

> **NOTE：**&gt;
> This API cannot be called within attributeModifier.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| typedFunc | [TemplateTypedFunc](arkts-arkui-templatetypedfunc-t.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md)&lt;T&gt; |

## virtualScroll

```TypeScript
virtualScroll(virtualScrollOptions?: VirtualScrollOptions): RepeatAttribute<T>
```

Enables virtual scrolling for **Repeat**.

> **NOTE：**&gt;
> This API cannot be called within attributeModifier.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| virtualScrollOptions | [VirtualScrollOptions](arkts-arkui-virtualscrolloptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md)&lt;T&gt; |
