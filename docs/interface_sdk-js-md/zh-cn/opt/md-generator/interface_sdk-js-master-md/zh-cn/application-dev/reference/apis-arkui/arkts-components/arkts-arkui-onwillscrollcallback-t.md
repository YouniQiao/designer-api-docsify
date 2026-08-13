# OnWillScrollCallback

```TypeScript
declare type OnWillScrollCallback =
(scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | ScrollResult
```

Called before scroll to allow developer to control real offset the Scrollable can scroll.

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type OnWillScrollCallback =(scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | ScrollResult--><!--Device-unnamed-declare type OnWillScrollCallback =(scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | ScrollResult-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scrollOffset | number | 是 |
| scrollState | [ScrollState](arkts-arkui-scrollstate-e.md) | 是 |
| scrollSource | [ScrollSource](../arkts-apis/arkts-arkui-scrollsource-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| void \| [ScrollResult](arkts-arkui-scrollresult-c.md) |
