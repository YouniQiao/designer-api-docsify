# OnGetStartIndexByOffsetCallback (System API)

```TypeScript
declare type OnGetStartIndexByOffsetCallback = (totalOffset: double) => StartLineInfo
```

根据Grid的总偏移量，计算当前页面起始行的位置，用于快速滑动或反向滑动场景。此回调需与onGetStartIndexByIndex同时设置才能生效。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type OnGetStartIndexByOffsetCallback = (totalOffset: double) => StartLineInfo--><!--Device-unnamed-declare type OnGetStartIndexByOffsetCallback = (totalOffset: double) => StartLineInfo-End-->

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| totalOffset | double | Yes | 总滚动偏移量，即Grid当中第一个GridItem的顶部与Grid顶部之间的偏移量。<br/>单位：vp |

**Return value:**

| Type | Description |
| --- | --- |
| [StartLineInfo](../arkts-apis/arkts-arkui-grid-startlineinfo-i-sys.md) | 用于记录Grid页面内起始行的位置信息。 |

