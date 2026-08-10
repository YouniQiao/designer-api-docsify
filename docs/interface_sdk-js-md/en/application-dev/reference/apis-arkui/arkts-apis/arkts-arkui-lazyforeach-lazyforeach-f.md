# LazyForEach

## LazyForEach

```TypeScript
export declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,
    itemGenerator: ItemGeneratorFunc<T>,
    keyGenerator?: KeyGeneratorFunc<T>,
): LazyForEachAttribute
```

输入值以获取带有选项的LazyForEach。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,): LazyForEachAttribute--><!--Device-unnamed-export declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,): LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | [IDataSource](arkts-arkui-lazyforeach-idatasource-i.md)&lt;T&gt; | Yes | 要在UI中使用的数组集合。 |
| itemGenerator | [ItemGeneratorFunc](arkts-arkui-itemgeneratorfunc-t.md)&lt;T&gt; | Yes | item生成器函数。 |
| keyGenerator | [KeyGeneratorFunc](arkts-arkui-keygeneratorfunc-t.md)&lt;T&gt; | No | 密钥生成器函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyForEachAttribute](../arkts-components/arkts-arkui-lazyforeach-attribute.md) | LazyForEach组件。 |


## LazyForEach

```TypeScript
export declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,
    itemGenerator: ItemGeneratorFunc<T>,
    keyGenerator?: KeyGeneratorFunc<T>,
    options?: LazyForEachOptions,
): LazyForEachAttribute
```

输入值以获取带有选项的LazyForEach。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,    options?: LazyForEachOptions,): LazyForEachAttribute--><!--Device-unnamed-export declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,    itemGenerator: ItemGeneratorFunc<T>,    keyGenerator?: KeyGeneratorFunc<T>,    options?: LazyForEachOptions,): LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | [IDataSource](arkts-arkui-lazyforeach-idatasource-i.md)&lt;T&gt; | Yes | 要在UI中使用的数组集合。 |
| itemGenerator | [ItemGeneratorFunc](arkts-arkui-itemgeneratorfunc-t.md)&lt;T&gt; | Yes | item生成器函数。 |
| keyGenerator | [KeyGeneratorFunc](arkts-arkui-keygeneratorfunc-t.md)&lt;T&gt; | No | 密钥生成器函数。 |
| options | [LazyForEachOptions](arkts-arkui-lazyforeach-lazyforeachoptions-i.md) | No | LazyForEach可选参数选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyForEachAttribute](../arkts-components/arkts-arkui-lazyforeach-attribute.md) | LazyForEach组件 |


## LazyForEach

```TypeScript
export declare function LazyForEach<T = Any>(
    style: CustomBuilderT<LazyForEachAttribute>
): LazyForEachAttribute
```

定义LazyForEach组件。它需要在组件属性设置开始时调用setLazyForEachOptions。并且它需要在组件属性设置结束时调用applyAttributeFinish。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function LazyForEach<T = Any>(    style: CustomBuilderT<LazyForEachAttribute>): LazyForEachAttribute--><!--Device-unnamed-export declare function LazyForEach<T = Any>(    style: CustomBuilderT<LazyForEachAttribute>): LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;LazyForEachAttribute&gt; | Yes | 回调来设置LazyForEach的属性 |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyForEachAttribute](../arkts-components/arkts-arkui-lazyforeach-attribute.md) | LazyForEach的属性。 |

