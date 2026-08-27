# ForEach

**ForEach** enables rendering of repeated content based on array type data.

For details about the development, see [ForEach: Rendering Repeated Content](../../../ui/rendering-control/arkts-rendering-control-foreach.md).

## ForEach

```TypeScript
ForEach(
    arr: Array<any>,
    itemGenerator: (item: any, index: number) => void,
    keyGenerator?: (item: any, index: number) => string,
  )
```

**ForEach** enables rendering of repeated content based on array type data. It must be used in a container component, and the component it returns must be one allowed inside the container component. For example, a **ListItem** component is allowed only when the parent container component of **ForEach** is List or ListItemGroup.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | Array&lt;any&gt; | Yes | Data source, which is an array.  If this parameter is set to **undefined**, the **ForEach** API does not take effect.  **NOTE**  - You can set this parameter to an empty array. In this case, no child component is created.  - You can also set this parameter to a function whose return value is an array, for example, **arr.slice (1, 3)**. However, the set function cannot change any state variables including the array itself. For example, **Array.splice**, **Array.sort**, and **Array.reverse** functions are not allowed, as they may change the array. |
| itemGenerator | (item: any, index: number) =&gt; void | Yes | Component generator.  - It generates a component for each data item in an array.  - (Optional) **item**: data item in the **arr** array.  - (Optional) **index**: index of the data item in the **arr** array.  **NOTE**  - The type of the created component must be the one allowed inside the parent container component of **ForEach**. For example, a **ListItem** component is allowed only when the parent container component of **ForEach** is **List**. |
| keyGenerator | (item: any, index: number) =&gt; string | No | Key generator.  - It generates a unique and persistent key for each array item of the data source **arr**. You can customize the key generation rule using this function.  - (Optional) **item**: data item in the **arr** array.  - (Optional) **index**: index of the data item in the **arr** array.  **NOTE**  - If this function is not specified, the default key generator of the framework is used: **(item: T, index: number) => { return index + '__' + JSON.stringify(item); }**.  - The key generator should not change any component state. |

## Summary
