# LazyForEach

For details about the development, see
[LazyForEach: Lazy Data Loading](docroot://ui/rendering-control/arkts-rendering-control-lazyforeach.md).

In scenarios involving a large number of child components, LazyForEach, when combined with techniques such as cached
list items, dynamic preloading, and component reuse, can significantly improve scrolling frame rates while reducing
memory usage. For best practices, see
[Optimizing Frame Loss for Long List Loading](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-best-practices-long-list).

## LazyForEach

```TypeScript
LazyForEach(
    dataSource: IDataSource,
    itemGenerator: (item: any, index: number) => void,
    keyGenerator?: (item: any, index: number) => string
  )
```

LazyForEach** iterates over provided data sources and creates corresponding components during each iteration.When **LazyForEach** is used in a scrolling container, the framework creates components as required within the visible area of the scrolling container. When a component is out of the visible area, the framework destroys and reclaims the component to reduce memory usage.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LazyForEachInterface-(    dataSource: IDataSource,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string  ): LazyForEachAttribute--><!--Device-LazyForEachInterface-(    dataSource: IDataSource,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string  ): LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | **LazyForEach** data source. You need to implement related APIs.  |
| itemGenerator | (item: any, index: number) =&gt; void | Yes | Child component generation function, which generates a child component for each data item in the array. \_\_\_HTML\_TAG\_USD\_0\_\_\_**NOTE** \_\_\_HTML\_TAG\_USD\_1\_\_\_- (Optional) **item**: data item. \_\_\_HTML\_TAG\_USD\_2\_\_\_(Optional) **index**: index of the data item. \_\_\_HTML\_TAG\_USD\_3\_\_\_- The function body of **itemGenerator** must be included in braces {...}. \_\_\_HTML\_TAG\_USD\_4\_\_\_- **itemGenerator** can and must generate only one child component for each iteration. \_\_\_HTML\_TAG\_USD\_5\_\_\_- The **if** statement is allowed in **itemGenerator**, but you must ensure that each branch of the **if** statement creates a child component of the same type.  |
| keyGenerator | (item: any, index: number) =&gt; string | No | ID generation function, which generates a unique and fixed ID for each data item in the data source. Components are updated only when their generated key changes. The **keyGenerator** parameter is optional, but you are advised to provide it so that the development framework can better identify array changes and update components correctly. \_\_\_HTML\_TAG\_USD\_0\_\_\_The default value is an empty callback. \_\_\_HTML\_TAG\_USD\_1\_\_\_**NOTE** \_\_\_HTML\_TAG\_USD\_2\_\_\_- (Optional) **item**: data item. \_\_\_HTML\_TAG\_USD\_3\_\_\_(Optional) **index**: index of the data item. \_\_\_HTML\_TAG\_USD\_4\_\_\_- When **keyGenerator** is omitted, the default function **(item: Object, index: number) => { return viewId + '-' + index.toString(); }** is used, where key generation is affected by the index value only (**viewId** is compiler-generated and consistent within the same **LazyForEach** component). \_\_\_HTML\_TAG\_USD\_5\_\_\_- To ensure correct and efficient child component updates, avoiding rendering anomalies or performance degradation, keys must meet the following requirements: \_\_\_HTML\_TAG\_USD\_6\_\_\_1. Uniqueness: Each data item must have a distinct key. \_\_\_HTML\_TAG\_USD\_7\_\_\_2. Consistency: Keys must remain unchanged for unmodified data items.  |

## LazyForEach

```TypeScript
LazyForEach(
    dataSource: IDataSource,
    itemGenerator: (item: any, index: number) => void,
    keyGenerator?: (item: any, index: number) => string,
    options?: LazyForEachOptions
  )
```

Enter the value to obtain the LazyForEach.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyForEachInterface-(    dataSource: IDataSource,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string,    options?: LazyForEachOptions  ): LazyForEachAttribute--><!--Device-LazyForEachInterface-(    dataSource: IDataSource,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string,    options?: LazyForEachOptions  ): LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |
| itemGenerator | (item: any, index: number) =&gt; void | Yes |  |
| keyGenerator | (item: any, index: number) =&gt; string | No |  |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

## Summary

