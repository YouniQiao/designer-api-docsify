# LazyForEach

## LazyForEach

```TypeScript
@ComponentBuilder
export declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,
    itemGenerator: ItemGeneratorFunc<T>,
    keyGenerator?: KeyGeneratorFunc<T>,
): LazyForEachAttribute
```

Enter the value to obtain the LazyForEach.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,): LazyForEachAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,): LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | [IDataSource](arkts-na-lazyforeach-idatasource-i.md)&lt;T&gt; | Yes | the array collection to be used in UI. |
| itemGenerator | [ItemGeneratorFunc](arkts-na-itemgeneratorfunc-t.md)&lt;T&gt; | Yes | item generator function. |
| keyGenerator | [KeyGeneratorFunc](arkts-na-keygeneratorfunc-t.md)&lt;T&gt; | No | key generator function |

**Return value:**

| Type | Description |
| --- | --- |
| LazyForEachAttribute | LazyForEach attribute |


## LazyForEach

```TypeScript
@ComponentBuilder
export declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,
    itemGenerator: ItemGeneratorFunc<T>,
    keyGenerator?: KeyGeneratorFunc<T>,
    options?: LazyForEachOptions,
): LazyForEachAttribute
```

Enter the value to obtain the LazyForEach.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,    options?: LazyForEachOptions,): LazyForEachAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,    options?: LazyForEachOptions,): LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | [IDataSource](arkts-na-lazyforeach-idatasource-i.md)&lt;T&gt; | Yes | the array collection to be used in UI. |
| itemGenerator | [ItemGeneratorFunc](arkts-na-itemgeneratorfunc-t.md)&lt;T&gt; | Yes | item generator function. |
| keyGenerator | [KeyGeneratorFunc](arkts-na-keygeneratorfunc-t.md)&lt;T&gt; | No | key generator function. |
| options | [LazyForEachOptions](arkts-na-lazyforeach-lazyforeachoptions-i.md) | No | options for LazyForEach behavior. |

**Return value:**

| Type | Description |
| --- | --- |
| LazyForEachAttribute | LazyForEach attribute |


## LazyForEach

```TypeScript
@Builder
export declare function LazyForEach<T = Any>(
    style: CustomBuilderT<LazyForEachAttribute>
): LazyForEachAttribute
```

Defines LazyForEach Component. It requires calling setLazyForEachOptions at start of component attribute set-up, and it requires calling applyAttributesFinish at end of component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function LazyForEach<T = Any>(    style: CustomBuilderT<LazyForEachAttribute>): LazyForEachAttribute--><!--Device-unnamed-@Builderexport declare function LazyForEach<T = Any>(    style: CustomBuilderT<LazyForEachAttribute>): LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;LazyForEachAttribute&gt; | Yes | callback to set up LazyForEach's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| LazyForEachAttribute | The attribute of LazyForEach. |

