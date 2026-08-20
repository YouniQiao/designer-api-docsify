# FilterResult

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface FilterResult--><!--Device-unnamed-export declare interface FilterResult-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## index

```TypeScript
index: int
```

该维度筛选项选中项目的索引值。

取值范围：大于等于-1的整数。

默认值：-1，没有选中项。若设置数值小于-1，按没有选中项处理。

**类型：** int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FilterResult-index: int--><!--Device-FilterResult-index: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name: ResourceStr
```

筛选项维度名称。

默认值：空字符串。

**说明：**如果文本大于列宽时，文本被截断。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FilterResult-name: ResourceStr--><!--Device-FilterResult-name: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: ResourceStr
```

该维度筛选项选中项目的值。

默认值：空字符串。

**说明：**如果文本大于列宽时，文本被截断。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FilterResult-value: ResourceStr--><!--Device-FilterResult-value: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

