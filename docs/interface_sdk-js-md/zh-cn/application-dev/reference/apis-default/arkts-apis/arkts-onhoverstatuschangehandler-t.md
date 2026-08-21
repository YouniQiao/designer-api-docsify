# OnHoverStatusChangeHandler

```TypeScript
export type OnHoverStatusChangeHandler = (status: HoverModeStatus) => void
```

onHoverStatusChange事件处理。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export type OnHoverStatusChangeHandler = (status: HoverModeStatus) => void--><!--Device-unnamed-export type OnHoverStatusChangeHandler = (status: HoverModeStatus) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| status | [HoverModeStatus](arkts-arkui-advanced-foldsplitcontainer-hovermodestatus-i.md) | 是 | 折叠屏进入或退出悬停模式时触发的回调函数。 |

