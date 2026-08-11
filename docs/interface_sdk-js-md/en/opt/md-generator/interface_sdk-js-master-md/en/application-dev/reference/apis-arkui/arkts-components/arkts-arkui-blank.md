# Blank

The **Blank** component is a spacer in the layout, automatically filling the remaining space along the main axis of
its parent container. It works only when the parent component is [Row]{@link Row}, [Column]{@link Column}, or
[Flex]{@link Flex}.
> **Child Components**
>
> No child component can be set.

## Blank

```TypeScript
Blank(min?: number | string)
```

Creates a **Blank** component.

Since API version 10: 

- When the **Blank** component is used within a [Row]{@link Row}, [Column]{@link Column}, or [Flex]{@link Flex}   
container, it will automatically stretch or shrink along the main axis if it does not have a main axis size specified. If the **Blank** component has a main axis size specified or if the container is set to adapt to the size of its child nodes, the component will not automatically stretch or shrink.  
- Relationship between **size** and **min** of the **Blank** component on the main axis: max(min, size).   
- If the **Blank** component has a cross axis size specified, it will not fill up the parent container on the cross  
axis. If it does not have a cross axis size specified, it will fill up the parent container on the cross axis, following the **ItemAlign.Stretch** mode, the default setting of **alignSelf**.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BlankInterface-(min?: number | string): BlankAttribute--><!--Device-BlankInterface-(min?: number | string): BlankAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| min | number \| string | No |

## Summary
