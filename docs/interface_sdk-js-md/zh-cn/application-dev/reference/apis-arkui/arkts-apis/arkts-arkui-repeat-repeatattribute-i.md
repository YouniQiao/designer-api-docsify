# RepeatAttribute

除支持拖拽排序属性外，还支持以下属性。

**继承/实现关系：** RepeatAttribute extends DynamicNode

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

通知Repeat已完成属性设置。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
debugLine(sourceLine: string, moduleName?: string): this
```

设置组件源码重定向信息。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceLine | string | 是 |
| moduleName | string | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## each

```TypeScript
each(itemGenerator: RepeatItemBuilder<T>): this
```

组件生成函数。当所有`.template()`的type和`.templateId()`返回值不匹配时，将使用`.each()`处理数据项。

> **说明：**&gt;
> `each`属性必须有，否则运行时会报错。
> 
> `itemGenerator`的参数为`RepeatItem`，该参数将`item`和`index`结合到了一起，请勿将`RepeatItem`参数拆开使用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| itemGenerator | [RepeatItemBuilder](arkts-arkui-repeatitembuilder-t.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## key

```TypeScript
key(keyGenerator: KeyGeneratorFunc<T>): this
```

键值生成函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyGenerator | [KeyGeneratorFunc](arkts-arkui-keygeneratorfunc-t.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## setRepeatOptions

```TypeScript
setRepeatOptions<T>(arr: RepeatArray<T>): this
```

设置Repeat选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | [RepeatArray](arkts-arkui-repeatarray-t.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## template

```TypeScript
template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions): this
```

由template type渲染对应的template子组件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| itemBuilder | [RepeatItemBuilder](arkts-arkui-repeatitembuilder-t.md)&lt;T&gt; | 是 |
| templateOptions | [TemplateOptions](arkts-arkui-repeat-templateoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## templateId

```TypeScript
templateId(typedFunc: TemplateTypedFunc<T>): this
```

为当前数据项分配template type。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| typedFunc | [TemplateTypedFunc](arkts-arkui-templatetypedfunc-t.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## virtualScroll

```TypeScript
virtualScroll(virtualScrollOptions?: VirtualScrollOptions): this
```

`Repeat`开启虚拟滚动。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| virtualScrollOptions | [VirtualScrollOptions](arkts-arkui-repeat-virtualscrolloptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |
