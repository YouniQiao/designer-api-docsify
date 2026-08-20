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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,): LazyForEachAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,): LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | [IDataSource](arkts-lazyforeach-idatasource-i.md)&lt;T&gt; | Yes | the array collection to be used in UI. |
| itemGenerator | [ItemGeneratorFunc](arkts-itemgeneratorfunc-t.md)&lt;T&gt; | Yes | item generator function. |
| keyGenerator | [KeyGeneratorFunc](arkts-keygeneratorfunc-t.md)&lt;T&gt; | No | key generator function |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyForEachAttribute](arkts-lazyforeach-attribute.md) | LazyForEach attribute |


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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,    options?: LazyForEachOptions,): LazyForEachAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,    options?: LazyForEachOptions,): LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | [IDataSource](arkts-lazyforeach-idatasource-i.md)&lt;T&gt; | Yes | the array collection to be used in UI. |
| itemGenerator | [ItemGeneratorFunc](arkts-itemgeneratorfunc-t.md)&lt;T&gt; | Yes | item generator function. |
| keyGenerator | [KeyGeneratorFunc](arkts-keygeneratorfunc-t.md)&lt;T&gt; | No | key generator function. |
| options | [LazyForEachOptions](arkts-lazyforeach-lazyforeachoptions-i.md) | No | options for LazyForEach behavior. |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyForEachAttribute](arkts-lazyforeach-attribute.md) | LazyForEach attribute |


## LazyForEach

```TypeScript
@Builder
export declare function LazyForEach<T = Any>(
    style: CustomBuilderT<LazyForEachAttribute>
): LazyForEachAttribute
```

Defines LazyForEach Component. It requires calling setLazyForEachOptions at start of component attribute set-up, and it requires calling applyAttributesFinish at end of component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function LazyForEach<T = Any>(    style: CustomBuilderT<LazyForEachAttribute>): LazyForEachAttribute--><!--Device-unnamed-@Builderexport declare function LazyForEach<T = Any>(    style: CustomBuilderT<LazyForEachAttribute>): LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[LazyForEachAttribute](arkts-lazyforeach-attribute.md)&gt; | Yes | callback to set up LazyForEach's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyForEachAttribute](arkts-lazyforeach-attribute.md) | The attribute of LazyForEach. |

