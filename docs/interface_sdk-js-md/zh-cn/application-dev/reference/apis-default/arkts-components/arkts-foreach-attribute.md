# ForEachAttribute

支持[debugLine](../../../reference/apis-arkui/arkui-ts/ts-rendering-control-foreach-sta.md#debugline24)属性。

**继承/实现关系：** ForEachAttribute extends DynamicNode

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export interface ForEachAttribute--><!--Device-unnamed-export interface ForEachAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

Notify ForEach已经完成了其属性的设置。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ForEachAttribute-applyAttributesFinish(): void--><!--Device-ForEachAttribute-applyAttributesFinish(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
debugLine(sourceLine: string, moduleName?: string): this
```

设置组件源码重定向信息。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ForEachAttribute-debugLine(sourceLine: string, moduleName?: string): this--><!--Device-ForEachAttribute-debugLine(sourceLine: string, moduleName?: string): this-End-->

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

## setForEachOptions

```TypeScript
setForEachOptions<T>(arr: () => Array<T>,
        itemGenerator: ItemGeneratorFunc<T>,
        keyGenerator?: KeyGeneratorFunc<T>): this
```

设置ForEach选项。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ForEachAttribute-setForEachOptions<T>(arr: () => Array<T>,        itemGenerator: ItemGeneratorFunc<T>,        keyGenerator?: KeyGeneratorFunc<T>): this--><!--Device-ForEachAttribute-setForEachOptions<T>(arr: () => Array<T>,        itemGenerator: ItemGeneratorFunc<T>,        keyGenerator?: KeyGeneratorFunc<T>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | () =&gt; Array&lt;T&gt; | 是 | 返回用于UI的数组的函数。 |
| itemGenerator | [ItemGeneratorFunc](arkts-itemgeneratorfunc-t.md)&lt;T&gt; | 是 | 项生成器函数。 |
| keyGenerator | [KeyGeneratorFunc](arkts-keygeneratorfunc-t.md)&lt;T&gt; | 否 | 键生成器函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | ForEachAttribute实例。 |

