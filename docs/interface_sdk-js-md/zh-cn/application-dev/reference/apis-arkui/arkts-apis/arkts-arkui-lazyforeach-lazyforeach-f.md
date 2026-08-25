# LazyForEach

## LazyForEach

```TypeScript
export declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,
    itemGenerator: ItemGeneratorFunc<T>,
    keyGenerator?: KeyGeneratorFunc<T>,
): LazyForEachAttribute
```

输入值以获取带有选项的LazyForEach。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataSource | [IDataSource](arkts-arkui-lazyforeach-idatasource-i.md)&lt;T&gt; | 是 |
| itemGenerator | [ItemGeneratorFunc](arkts-arkui-itemgeneratorfunc-t.md)&lt;T&gt; | 是 |
| keyGenerator | [KeyGeneratorFunc](arkts-arkui-keygeneratorfunc-t.md)&lt;T&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [LazyForEachAttribute](arkts-arkui-lazyforeach-lazyforeachattribute-i.md) |


## LazyForEach

```TypeScript
export declare function LazyForEach<T = Any>(dataSource: IDataSource<T>,
    itemGenerator: ItemGeneratorFunc<T>,
    keyGenerator?: KeyGeneratorFunc<T>,
    options?: LazyForEachOptions,
): LazyForEachAttribute
```

输入值以获取带有选项的LazyForEach。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataSource | [IDataSource](arkts-arkui-lazyforeach-idatasource-i.md)&lt;T&gt; | 是 |
| itemGenerator | [ItemGeneratorFunc](arkts-arkui-itemgeneratorfunc-t.md)&lt;T&gt; | 是 |
| keyGenerator | [KeyGeneratorFunc](arkts-arkui-keygeneratorfunc-t.md)&lt;T&gt; | 否 |
| options | [LazyForEachOptions](arkts-arkui-lazyforeach-lazyforeachoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [LazyForEachAttribute](arkts-arkui-lazyforeach-lazyforeachattribute-i.md) |


## LazyForEach

```TypeScript
export declare function LazyForEach<T = Any>(
    style: CustomBuilderT<LazyForEachAttribute>
): LazyForEachAttribute
```

定义LazyForEach组件。它需要在组件属性设置开始时调用setLazyForEachOptions。 并且它需要在组件属性设置结束时调用applyAttributeFinish。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[LazyForEachAttribute](arkts-arkui-lazyforeach-lazyforeachattribute-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [LazyForEachAttribute](arkts-arkui-lazyforeach-lazyforeachattribute-i.md) |
