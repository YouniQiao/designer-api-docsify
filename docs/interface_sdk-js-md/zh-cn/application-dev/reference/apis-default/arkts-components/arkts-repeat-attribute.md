# RepeatAttribute

除支持拖拽排序属性外，还支持以下属性。

**继承/实现关系：** RepeatAttribute extends DynamicNode

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export interface RepeatAttribute--><!--Device-unnamed-export interface RepeatAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

通知Repeat已完成属性设置。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RepeatAttribute-applyAttributesFinish(): void--><!--Device-RepeatAttribute-applyAttributesFinish(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
debugLine(sourceLine: string, moduleName?: string): this
```

设置组件源码重定向信息。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RepeatAttribute-debugLine(sourceLine: string, moduleName?: string): this--><!--Device-RepeatAttribute-debugLine(sourceLine: string, moduleName?: string): this-End-->

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

## each

```TypeScript
each(itemGenerator: RepeatItemBuilder<T>): this
```

组件生成函数。当所有`.template()`的type和`.templateId()`返回值不匹配时，将使用`.each()`处理数据项。

> **说明：**
> 
> `each`属性必须有，否则运行时会报错。
> 
> `itemGenerator`的参数为`RepeatItem`，该参数将`item`和`index`结合到了一起，请勿将`RepeatItem`参数拆开使用。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RepeatAttribute-each(itemGenerator: RepeatItemBuilder<T>): this--><!--Device-RepeatAttribute-each(itemGenerator: RepeatItemBuilder<T>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemGenerator | [RepeatItemBuilder](arkts-repeatitembuilder-t.md)&lt;T&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | RepeatAttribute instance |

## key

```TypeScript
key(keyGenerator: KeyGeneratorFunc<T>): this
```

键值生成函数。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RepeatAttribute-key(keyGenerator: KeyGeneratorFunc<T>): this--><!--Device-RepeatAttribute-key(keyGenerator: KeyGeneratorFunc<T>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyGenerator | [KeyGeneratorFunc](arkts-keygeneratorfunc-t.md)&lt;T&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | RepeatAttribute instance |

## setRepeatOptions

```TypeScript
setRepeatOptions<T>(arr: RepeatArray<T>): this
```

设置Repeat选项。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RepeatAttribute-setRepeatOptions<T>(arr: RepeatArray<T>): this--><!--Device-RepeatAttribute-setRepeatOptions<T>(arr: RepeatArray<T>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | [RepeatArray](arkts-repeatarray-t.md)&lt;T&gt; | 是 | 数据源数组 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | RepeatAttribute实例 |

## template

```TypeScript
template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions): this
```

由template type渲染对应的template子组件。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RepeatAttribute-template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions): this--><!--Device-RepeatAttribute-template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 当前模板类型。 |
| itemBuilder | [RepeatItemBuilder](arkts-repeatitembuilder-t.md)&lt;T&gt; | 是 | 组件生成函数。 |
| templateOptions | [TemplateOptions](arkts-repeat-templateoptions-i.md) | 否 | 当前模板配置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | RepeatAttribute instance |

## templateId

```TypeScript
templateId(typedFunc: TemplateTypedFunc<T>): this
```

为当前数据项分配template type。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RepeatAttribute-templateId(typedFunc: TemplateTypedFunc<T>): this--><!--Device-RepeatAttribute-templateId(typedFunc: TemplateTypedFunc<T>): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedFunc | [TemplateTypedFunc](arkts-templatetypedfunc-t.md)&lt;T&gt; | 是 | 生成当前数据项对应的template type。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | RepeatAttribute instance |

## virtualScroll

```TypeScript
virtualScroll(virtualScrollOptions?: VirtualScrollOptions): this
```

`Repeat`开启虚拟滚动。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RepeatAttribute-virtualScroll(virtualScrollOptions?: VirtualScrollOptions): this--><!--Device-RepeatAttribute-virtualScroll(virtualScrollOptions?: VirtualScrollOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| virtualScrollOptions | [VirtualScrollOptions](arkts-repeat-virtualscrolloptions-i.md) | 否 | 虚拟滚动配置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | RepeatAttribute instance |

