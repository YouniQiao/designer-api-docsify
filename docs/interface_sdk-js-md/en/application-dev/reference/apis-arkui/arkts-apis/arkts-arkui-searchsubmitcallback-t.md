# SearchSubmitCallback

```TypeScript
export type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void
```

点击搜索图标、搜索按钮或者按下软键盘搜索按钮时的回调事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void--><!--Device-unnamed-export type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchContent | string | Yes | 当前搜索框中输入的文本内容。 |
| event | [SubmitEvent](../arkts-components/arkts-arkui-submitevent-i.md) | No | 提交事件。 |

