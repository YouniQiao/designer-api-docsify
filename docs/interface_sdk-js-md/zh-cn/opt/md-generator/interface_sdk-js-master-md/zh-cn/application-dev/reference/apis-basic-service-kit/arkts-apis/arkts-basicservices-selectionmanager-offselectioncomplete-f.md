# offSelectionComplete

## offSelectionComplete

```TypeScript
function offSelectionComplete(callback?: Callback<SelectionInfo>): void
```

取消订阅划词完成事件，与[onSelectionComplete](arkts-basicservices-selectionmanager-onselectioncomplete-f.md#onSelectionComplete)搭配使 用。

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-selectionManager-function offSelectionComplete(callback?: Callback<SelectionInfo>): void--><!--Device-selectionManager-function offSelectionComplete(callback?: Callback<SelectionInfo>): void-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i-sys.md)&gt; | 否 |
