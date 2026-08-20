# repeat(Defines Repeat component.)

## Modules to Import

```TypeScript
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [RepeatAttribute(Defines Repeat component.)](arkts-arkui-repeatattribute-c.md) | In addition to the drag-and-drop sorting attribute, the following attributes are supported. |

### Interfaces

| Name | Description |
| --- | --- |
| [RepeatItem(Defines Repeat component.)](arkts-arkui-repeatitem-i.md) | Construct a new type for each item. |
| [TemplateOptions(Defines Repeat component.)](arkts-arkui-templateoptions-i.md) | When **cachedCount** is set to the maximum number of nodes in the display area of the container component for the current template, **Repeat** achieves maximum reuse efficiency. If there are no nodes of the current template in the container component's display area, the cache list is not released, which increases application memory usage. You are advised to set **cachedCount** to the number of nodes within the container component's display area and adjust the value according to the actual situation. Yet, setting **cachedCount** to less than 2 is not recommended, as this may lead to the frequent node creation during rapid scrolling and result in performance degradation. |
| [VirtualScrollOptions(Defines Repeat component.)](arkts-arkui-virtualscrolloptions-i.md) | Configures the expected total number of data items to be loaded in lazy loading mode, the reuse capability, and the precise data lazy loading capability. |

### Enums

| Name | Description |
| --- | --- |
| [RepeatMemOptStrategy(Defines Repeat component.)](arkts-arkui-repeatmemoptstrategy-e.md) | Defines a type for memory optimization strategy. |

### Types

| Name | Description |
| --- | --- |
| [RepeatArray(Defines Repeat component.)](arkts-arkui-repeatarray-t.md) | Defines a union type for **Repeat** data source parameters. |
| [RepeatInterface(Defines Repeat component.)](arkts-arkui-repeatinterface-t.md) | Indicates the type of Repeat. |
| [RepeatItemBuilder(Defines Repeat component.)](arkts-arkui-repeatitembuilder-t.md) | Defines builder function to render one template type. |
| [TemplateTypedFunc(Defines Repeat component.)](arkts-arkui-templatetypedfunc-t.md) | Function that returns typed string to render one template. |

### Constants

| Name | Description |
| --- | --- |
| [Repeat(Defines Repeat component.)](arkts-arkui-repeat-con.md#repeat) | Defines Repeat Component, and Add More Array Type. |

