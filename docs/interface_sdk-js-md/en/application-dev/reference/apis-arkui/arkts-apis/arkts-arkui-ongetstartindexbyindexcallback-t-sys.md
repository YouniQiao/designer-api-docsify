# OnGetStartIndexByIndexCallback (System API)

```TypeScript
export type OnGetStartIndexByIndexCallback = (targetIndex: int) => StartLineInfo
```

根据指定的目标索引，计算Grid滚动到该位置时页面内对应的起始行，用于支持[scrollToIndex](arkts-arkui-scroll-scroller-c.md#scrolltoindex)等操作。  
**系统接口：** 此接口为系统接口。  
**模型约束：** 此接口仅可在Stage模型下使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnGetStartIndexByIndexCallback = (targetIndex: int) => StartLineInfo--><!--Device-unnamed-export type OnGetStartIndexByIndexCallback = (targetIndex: int) => StartLineInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetIndex | int | Yes | 要滚动到的目标GridItem的索引。 <br>取值限定为整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [StartLineInfo](arkts-arkui-grid-startlineinfo-i-sys.md) | - |

