# GridColAttribute

The GridColAttribute.@extends CommonMethod @interface GridColAttribute

**继承/实现关系：** GridColAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<GridColAttribute> | AttributeModifier<CommonMethod>
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
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[GridColAttribute](arkts-arkui-gridcol-gridcolattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GridColAttribute](arkts-arkui-gridcol-gridcolattribute-i.md) |

## gridColOffset

```TypeScript
default gridColOffset(value: int | GridColColumnOption | undefined): this
```

设置相对于前一个栅格子组件偏移的列数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| [GridColColumnOption](arkts-arkui-gridcol-gridcolcolumnoption-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GridColAttribute](arkts-arkui-gridcol-gridcolattribute-i.md) |

## order

```TypeScript
default order(value: int | GridColColumnOption | undefined): this
```

设置栅格子组件的序号，根据序号从小到大对栅格子组件进行排序。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| [GridColColumnOption](arkts-arkui-gridcol-gridcolcolumnoption-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GridColAttribute](arkts-arkui-gridcol-gridcolattribute-i.md) |

## setGridColOptions

```TypeScript
default setGridColOptions(options?: GridColOptions): this
```

Set GridCol options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [GridColOptions](arkts-arkui-gridcol-gridcoloptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [GridColAttribute](arkts-arkui-gridcol-gridcolattribute-i.md) |

## span

```TypeScript
default span(value: int | GridColColumnOption | undefined): this
```

设置占用列数。 span为0，意味着该元素不参与布局计算，即不会被渲染。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| [GridColColumnOption](arkts-arkui-gridcol-gridcolcolumnoption-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GridColAttribute](arkts-arkui-gridcol-gridcolattribute-i.md) |
