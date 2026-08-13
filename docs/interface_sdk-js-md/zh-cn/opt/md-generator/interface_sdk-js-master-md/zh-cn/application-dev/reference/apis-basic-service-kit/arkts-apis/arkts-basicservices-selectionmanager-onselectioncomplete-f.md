# onSelectionComplete

## onSelectionComplete

```TypeScript
function onSelectionComplete(callback: Callback<SelectionInfo>): void
```

订阅划词完成事件，与[offSelectionComplete](arkts-basicservices-selectionmanager-offselectioncomplete-f.md#offSelectionComplete)搭配 使用取消订阅。

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-selectionManager-function onSelectionComplete(callback: Callback<SelectionInfo>): void--><!--Device-selectionManager-function onSelectionComplete(callback: Callback<SelectionInfo>): void-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [33600003](../../apis-basic-services-kit/errorcode-selection.md#33600003-调用接口的应用与系统设置中选择的应用不匹配) |
