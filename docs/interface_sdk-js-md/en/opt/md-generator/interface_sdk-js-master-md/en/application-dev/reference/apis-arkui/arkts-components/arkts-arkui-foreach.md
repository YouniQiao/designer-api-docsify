# ForEach

**ForEach** enables rendering of repeated content based on array type data.

For details about the development, see
[ForEach: Rendering Repeated Content](docroot://ui/rendering-control/arkts-rendering-control-foreach.md).

## ForEach

```TypeScript
ForEach(
    arr: Array<any>,
    itemGenerator: (item: any, index: number) => void,
    keyGenerator?: (item: any, index: number) => string,
  )
```

**ForEach** enables rendering of repeated content based on array type data. It must be used in a container component, and the component it returns must be one allowed inside the container component. For example, a  
**ListItem** component is allowed only when the parent container component of **ForEach** is [List]{@link ./list}or [ListItemGroup]{@link ./list_item_group}.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ForEachInterface-(    arr: Array<any>,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string,  ): ForEachAttribute--><!--Device-ForEachInterface-(    arr: Array<any>,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string,  ): ForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arr | Array & lt;any & gt; | Yes |
| itemGenerator | (item: any, index: number) = & gt; void | Yes |
| keyGenerator | (item: any, index: number) = & gt; string | No |

## Summary
