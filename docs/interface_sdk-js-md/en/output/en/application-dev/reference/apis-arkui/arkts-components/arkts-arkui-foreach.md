# ForEach

**ForEach** enables rendering of repeated content based on array type data. For details about the development, see [ForEach: Rendering Repeated Content](docroot://ui/rendering-control/arkts-rendering-control-foreach.md).

## ForEach

```TypeScript
ForEach(
    arr: Array<any>,
    itemGenerator: (item: any, index: number) => void,
    keyGenerator?: (item: any, index: number) => string,
  )
```

**ForEach** enables rendering of repeated content based on array type data. It must be used in a container component, and the component it returns must be one allowed inside the container component. For example, a **ListItem** component is allowed only when the parent container component of **ForEach** is [List]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or [ListItemGroup]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ForEachInterface-(    arr: Array<any>,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string,  ): ForEachAttribute--><!--Device-ForEachInterface-(    arr: Array<any>,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string,  ): ForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | Array&lt;any&gt; | Yes | Data source, which is an array. \_\_\_HTML\_TAG\_USD\_0\_\_\_If this parameter is set to **undefined**, the **ForEach** API does not take effect. \_\_\_HTML\_TAG\_USD\_1\_\_\_**NOTE** \_\_\_HTML\_TAG\_USD\_2\_\_\_- You can set this parameter to an empty array. In this case, no child component is created. \_\_\_HTML\_TAG\_USD\_3\_\_\_- You can also set this parameter to a function whose return value is an array, for example, **arr.slice (1, 3)**. However, the set function cannot change any state variables including the array itself. For example, **Array.splice**, **Array.sort**, and **Array.reverse** functions are not allowed, as they may change the array.  |
| itemGenerator | (item: any, index: number) =&gt; void | Yes | Component generator. \_\_\_HTML\_TAG\_USD\_0\_\_\_- It generates a component for each data item in an array. \_\_\_HTML\_TAG\_USD\_1\_\_\_- (Optional) **item**: data item in the **arr** array. \_\_\_HTML\_TAG\_USD\_2\_\_\_- (Optional) **index**: index of the data item in the **arr** array. \_\_\_HTML\_TAG\_USD\_3\_\_\_**NOTE** \_\_\_HTML\_TAG\_USD\_4\_\_\_- The type of the created component must be the one allowed inside the parent container component of **ForEach**. For example, a **ListItem** component is allowed only when the parent container component of **ForEach** is **List**.  |
| keyGenerator | (item: any, index: number) =&gt; string | No | Key generator. \_\_\_HTML\_TAG\_USD\_0\_\_\_- It generates a unique and persistent key for each array item of the data source **arr**. You can customize the key generation rule using this function. \_\_\_HTML\_TAG\_USD\_1\_\_\_- (Optional) **item**: data item in the **arr** array. \_\_\_HTML\_TAG\_USD\_2\_\_\_- (Optional) **index**: index of the data item in the **arr** array. \_\_\_HTML\_TAG\_USD\_3\_\_\_**NOTE** \_\_\_HTML\_TAG\_USD\_4\_\_\_- If this function is not specified, the default key generator of the framework is used: **(item: T, index: number) => { return index + '\_\_' + JSON.stringify(item); }**. \_\_\_HTML\_TAG\_USD\_5\_\_\_- The key generator should not change any component state.  |

## Summary

