# OnGetStartIndexByIndexCallback (System API)

```TypeScript
declare type OnGetStartIndexByIndexCallback = (targetIndex: int) => StartLineInfo
```

根据指定的目标索引，计算Grid滚动到该位置时页面内对应的起始行，用于支持[scrollToIndex](../arkts-apis/arkts-arkui-scroll-scroller-c.md/arkts-arkui-scroll-scroller-c.md#scrolltoindex)等操作。此回调需与onGetStartIndexByOffset同时设置才能生效。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type OnGetStartIndexByIndexCallback = (targetIndex: int) => StartLineInfo--><!--Device-unnamed-declare type OnGetStartIndexByIndexCallback = (targetIndex: int) => StartLineInfo-End-->

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetIndex | int | Yes | 要滚动到的目标GridItem的索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| [StartLineInfo](../arkts-apis/arkts-arkui-grid-startlineinfo-i-sys.md) | 用于记录Grid页面内起始行的位置信息。 |

