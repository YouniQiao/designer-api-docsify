# OnWillScrollCallback

```TypeScript
export type OnWillScrollCallback = (scrollOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | ScrollResult)
```

Called before scroll to allow developer to control real offset the Scrollable can scroll.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scrollOffset | double | 是 |
| scrollState | [ScrollState](../arkts-components/arkts-arkui-scrollstate-e.md) | 是 |
| scrollSource | [ScrollSource](arkts-arkui-scrollsource-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| (undefined \| ScrollResult) |
