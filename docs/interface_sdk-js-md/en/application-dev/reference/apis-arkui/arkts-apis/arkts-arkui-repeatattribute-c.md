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

> **NOTE：**
> 
> - The **each** property is mandatory. If it is omitted, runtime errors will occur.
> 
> - The **itemGenerator** parameter is of the **RepeatItem** type, which combines **item** and **index**. Do not
> destructure **RepeatItem**.
> 
> - This API cannot be called within attributeModifier.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemGenerator | (repeatItem: RepeatItem & lt;T & gt;) = & gt; void | Yes | Component generator. |

**Return value:**

| Type | Description |
| --- | --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md)&lt;T&gt; |  |

**Examples**

```TypeScript
// Create a Text component for each item in the arr array of the Array<string> type.
Repeat<string>(this.arr)
  .each((obj: RepeatItem<string>) => { Text(obj.item) })
```

## key

```TypeScript
key(keyGenerator: (item: T, index: number) => string): RepeatAttribute<T>
```

Key generator.

> **NOTE：**
> 
> This API cannot be called within attributeModifier.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyGenerator | (item: T, index: number) = & gt; string | Yes | Key generator.   **item**: data item in the **arr** array. It is optional.    **index**: index of a data item in the **arr** array. It is optional. |

**Return value:**

| Type | Description |
| --- | --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md)&lt;T&gt; |  |

**Examples**

```TypeScript
// Create a Text component for each item in the arr array of the Array<string> type.
// Use the string value as its key.
Repeat<string>(this.arr)
  .each((obj: RepeatItem<string>) => { Text(obj.item) })
  .key((obj: string) => obj)
```

## template

```TypeScript
template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions): RepeatAttribute<T>
```

Renders the corresponding template child component based on the template type.

> **NOTE：**
> 
> This API cannot be called within attributeModifier.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Current template type. |
| itemBuilder | [RepeatItemBuilder](arkts-arkui-repeatitembuilder-t.md)&lt;T&gt; | Yes | Component generator. |
| templateOptions | [TemplateOptions](arkts-arkui-templateoptions-i.md) | No | Current template configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md)&lt;T&gt; |  |

**Examples**

```TypeScript
// arr is an array of the Array<string> type.
// Use Repeat in a List container component with virtual scrolling enabled.
// Define a reusable template temp for generating Text components.
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => {})
    .virtualScroll()
    .template('temp', (obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
}
```

## templateId

```TypeScript
templateId(typedFunc: TemplateTypedFunc<T>): RepeatAttribute<T>
```

Assigns a template type for this data item.

> **NOTE：**
> 
> This API cannot be called within attributeModifier.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typedFunc | [TemplateTypedFunc](arkts-arkui-templatetypedfunc-t.md)&lt;T&gt; | Yes | Function that generates a template type for each data item. |

**Return value:**

| Type | Description |
| --- | --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md)&lt;T&gt; |  |

**Examples**

```TypeScript
// arr is an array of the Array<string> type.
// Use Repeat in a List container component with virtual scrolling enabled.
// Define a reusable template temp for generating Text components.
// Use the temp template for all data items.
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => {})
    .virtualScroll()
    .template('temp', (obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
    .templateId((item: string, index: number) => { return 'temp' })
}
```

## virtualScroll

```TypeScript
virtualScroll(virtualScrollOptions?: VirtualScrollOptions): RepeatAttribute<T>
```

Enables virtual scrolling for **Repeat**.

> **NOTE：**
> 
> This API cannot be called within attributeModifier.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| virtualScrollOptions | [VirtualScrollOptions](arkts-arkui-virtualscrolloptions-i.md) | No | Virtual scrolling configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md)&lt;T&gt; |  |

**Examples**

```TypeScript
// Create a Text component for each item in the arr array of the Array<string> type.
// Use Repeat in a List container component with virtual scrolling enabled.
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
    .virtualScroll()
}
```
