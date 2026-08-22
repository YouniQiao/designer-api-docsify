# LazyForEachAttribute

支持拖拽排序和 [debugLine](../../../reference/apis-arkui/arkui-ts/ts-rendering-control-lazyforeach-sta.md#debugline24)属性。

**继承/实现关系：** LazyForEachAttribute extends DynamicNode

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface LazyForEachAttribute--><!--Device-unnamed-export interface LazyForEachAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

通知LazyForEach已完成属性设置。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LazyForEachAttribute-applyAttributesFinish(): void--><!--Device-LazyForEachAttribute-applyAttributesFinish(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
debugLine(sourceLine: string, moduleName?: string): this
```

设置组件源码重定向信息。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LazyForEachAttribute-debugLine(sourceLine: string, moduleName?: string): this--><!--Device-LazyForEachAttribute-debugLine(sourceLine: string, moduleName?: string): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceLine | string | 是 | 源码行号。 |
| moduleName | string | 否 | 组件所属模块名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## setLazyForEachOptions

```TypeScript
setLazyForEachOptions<T>(dataSource: IDataSource<T>,
        itemGenerator: ItemGeneratorFunc<T>,
        keyGenerator?: KeyGeneratorFunc<T>): this
```

设置LazyForEach选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LazyForEachAttribute-setLazyForEachOptions<T>(dataSource: IDataSource<T>,        itemGenerator: ItemGeneratorFunc<T>,        keyGenerator?: KeyGeneratorFunc<T>): this--><!--Device-LazyForEachAttribute-setLazyForEachOptions<T>(dataSource: IDataSource<T>,        itemGenerator: ItemGeneratorFunc<T>,        keyGenerator?: KeyGeneratorFunc<T>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataSource | [IDataSource](arkts-lazyforeach-idatasource-i.md)&lt;T&gt; | 是 | 数据源提供数据 |
| itemGenerator | [ItemGeneratorFunc](arkts-itemgeneratorfunc-t.md)&lt;T&gt; | 是 | 项目生成器函数 |
| keyGenerator | [KeyGeneratorFunc](arkts-keygeneratorfunc-t.md)&lt;T&gt; | 否 | 密钥生成器函数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | LazyForEachAttribute实例 |

## setLazyForEachOptions

```TypeScript
setLazyForEachOptions<T>(dataSource: IDataSource<T>,
        itemGenerator: ItemGeneratorFunc<T>,
        keyGenerator?: KeyGeneratorFunc<T>,
        options?: LazyForEachOptions): this
```

设置LazyForEach选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LazyForEachAttribute-setLazyForEachOptions<T>(dataSource: IDataSource<T>,        itemGenerator: ItemGeneratorFunc<T>,        keyGenerator?: KeyGeneratorFunc<T>,        options?: LazyForEachOptions): this--><!--Device-LazyForEachAttribute-setLazyForEachOptions<T>(dataSource: IDataSource<T>,        itemGenerator: ItemGeneratorFunc<T>,        keyGenerator?: KeyGeneratorFunc<T>,        options?: LazyForEachOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataSource | [IDataSource](arkts-lazyforeach-idatasource-i.md)&lt;T&gt; | 是 | 提供数据的数据源。 |
| itemGenerator | [ItemGeneratorFunc](arkts-itemgeneratorfunc-t.md)&lt;T&gt; | 是 | 项生成器函数。 |
| keyGenerator | [KeyGeneratorFunc](arkts-keygeneratorfunc-t.md)&lt;T&gt; | 否 | 键生成器函数。 |
| options | [LazyForEachOptions](arkts-lazyforeach-lazyforeachoptions-i.md) | 否 | LazyForEach可选参数选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | LazyForEachAttribute实例 |

