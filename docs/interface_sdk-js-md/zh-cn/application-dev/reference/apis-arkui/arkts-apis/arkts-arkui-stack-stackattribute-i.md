# StackAttribute

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。@extends CommonMethod @interface StackAttribute

**继承/实现关系：** StackAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alignContent

```TypeScript
default alignContent(value: Alignment | undefined): this
```

设置子组件在容器内的对齐方式。该属性与align同时设置时，后设置的属性生效。 该属性与接口的构造入参同时设置时，生效属性上的设置效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Alignment](arkts-arkui-alignment-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [StackAttribute](arkts-arkui-stack-stackattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<StackAttribute> | AttributeModifier<CommonMethod>
        | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[StackAttribute](arkts-arkui-stack-stackattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [StackAttribute](arkts-arkui-stack-stackattribute-i.md) |

## setStackOptions

```TypeScript
default setStackOptions(options?: StackOptions): this
```

设置Stack选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [StackOptions](arkts-arkui-stack-stackoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [StackAttribute](arkts-arkui-stack-stackattribute-i.md) |

## syncLoad

```TypeScript
default syncLoad(enable: boolean): this
```

设置是否同步加载Stack区域内所有子组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [StackAttribute](arkts-arkui-stack-stackattribute-i.md) |
