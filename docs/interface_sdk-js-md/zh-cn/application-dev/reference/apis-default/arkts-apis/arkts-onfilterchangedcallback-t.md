# OnFilterChangedCallback

```TypeScript
declare type OnFilterChangedCallback = (filterResults: Array<FilterResult>) => void
```

用户点击筛选后的回调事件。回调函数的参数为选中的筛选项结果列表。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare type OnFilterChangedCallback = (filterResults: Array<FilterResult>) => void--><!--Device-unnamed-declare type OnFilterChangedCallback = (filterResults: Array<FilterResult>) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filterResults | Array&lt;[FilterResult](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-filter-filterresult-c.md)&gt; | 是 | 选中的筛选项结果列表。 |

