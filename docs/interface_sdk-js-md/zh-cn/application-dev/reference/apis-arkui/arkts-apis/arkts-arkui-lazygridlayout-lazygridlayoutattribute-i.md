# LazyGridLayoutAttribute

LazyGridLayout组件属性。

**继承/实现关系：** LazyGridLayoutAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## columnsGap

```TypeScript
default columnsGap(value: LengthMetrics | undefined): this
```

设置列与列的间距。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## footer

```TypeScript
default footer(builder: CustomBuilder | undefined): this
```

设置懒加载网格布局的尾部。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## header

```TypeScript
default header(builder: CustomBuilder | undefined): this
```

设置懒加载网格布局的头部。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onVisibleIndexesChange

```TypeScript
default onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): this
```

当可视区域内子组件的索引值发生变化时触发回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnVisibleIndexesChangeCallback](../arkts-components/arkts-arkui-onvisibleindexeschangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## rowsGap

```TypeScript
default rowsGap(value: LengthMetrics | undefined): this
```

设置行与行的间距。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## sticky

```TypeScript
default sticky(sticky: StickyStyle | undefined): this
```

设置头部和尾部的吸顶吸底样式。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [sticky](#sticky) | [StickyStyle](../arkts-components/arkts-arkui-stickystyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |
