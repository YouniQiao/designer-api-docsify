# OnScrollCallback

```TypeScript
export type OnScrollCallback = (scrollOffset: double, scrollState: ScrollState) => void
```

On scroll callback using in scrollable onDidScroll.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scrollOffset | double | 是 |
| scrollState | [ScrollState](../arkts-components/arkts-arkui-scrollstate-e.md) | 是 |
