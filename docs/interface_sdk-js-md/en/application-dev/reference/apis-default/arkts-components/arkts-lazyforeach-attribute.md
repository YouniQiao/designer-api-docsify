# LazyForEachAttribute

Declare LazyForEachAttribute.

**Inheritance/Implementation:** LazyForEachAttribute extends DynamicNode

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export interface LazyForEachAttribute--><!--Device-unnamed-export interface LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

Notify LazyForEach has finished setting up its attributes.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyForEachAttribute-applyAttributesFinish(): void--><!--Device-LazyForEachAttribute-applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
debugLine(sourceLine: string, moduleName?: string): this
```

Set the component's source code redirection information.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyForEachAttribute-debugLine(sourceLine: string, moduleName?: string): this--><!--Device-LazyForEachAttribute-debugLine(sourceLine: string, moduleName?: string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceLine | string | Yes | the source code line. |
| moduleName | string | No | module to which the component belongs. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setLazyForEachOptions

```TypeScript
setLazyForEachOptions<T>(dataSource: IDataSource<T>,
        itemGenerator: ItemGeneratorFunc<T>,
        keyGenerator?: KeyGeneratorFunc<T>): this
```

Sets LazyForEach options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyForEachAttribute-setLazyForEachOptions<T>(dataSource: IDataSource<T>,        itemGenerator: ItemGeneratorFunc<T>,        keyGenerator?: KeyGeneratorFunc<T>): this--><!--Device-LazyForEachAttribute-setLazyForEachOptions<T>(dataSource: IDataSource<T>,        itemGenerator: ItemGeneratorFunc<T>,        keyGenerator?: KeyGeneratorFunc<T>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | [IDataSource](arkts-lazyforeach-idatasource-i.md)&lt;T&gt; | Yes | Data source to provide data. |
| itemGenerator | [ItemGeneratorFunc](arkts-itemgeneratorfunc-t.md)&lt;T&gt; | Yes | Item generator function. |
| keyGenerator | [KeyGeneratorFunc](arkts-keygeneratorfunc-t.md)&lt;T&gt; | No | Key generator function. |

**Return value:**

| Type | Description |
| --- | --- |
| this | LazyForEachAttribute instance |

## setLazyForEachOptions

```TypeScript
setLazyForEachOptions<T>(dataSource: IDataSource<T>,
        itemGenerator: ItemGeneratorFunc<T>,
        keyGenerator?: KeyGeneratorFunc<T>,
        options?: LazyForEachOptions): this
```

Sets LazyForEach options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyForEachAttribute-setLazyForEachOptions<T>(dataSource: IDataSource<T>,        itemGenerator: ItemGeneratorFunc<T>,        keyGenerator?: KeyGeneratorFunc<T>,        options?: LazyForEachOptions): this--><!--Device-LazyForEachAttribute-setLazyForEachOptions<T>(dataSource: IDataSource<T>,        itemGenerator: ItemGeneratorFunc<T>,        keyGenerator?: KeyGeneratorFunc<T>,        options?: LazyForEachOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | [IDataSource](arkts-lazyforeach-idatasource-i.md)&lt;T&gt; | Yes | Data source to provide data. |
| itemGenerator | [ItemGeneratorFunc](arkts-itemgeneratorfunc-t.md)&lt;T&gt; | Yes | Item generator function. |
| keyGenerator | [KeyGeneratorFunc](arkts-keygeneratorfunc-t.md)&lt;T&gt; | No | Key generator function. |
| options | [LazyForEachOptions](arkts-lazyforeach-lazyforeachoptions-i.md) | No | options for LazyForEach behavior |

**Return value:**

| Type | Description |
| --- | --- |
| this | LazyForEachAttribute instance |

