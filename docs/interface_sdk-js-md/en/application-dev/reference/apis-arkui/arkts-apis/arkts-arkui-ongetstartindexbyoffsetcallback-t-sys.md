# OnGetStartIndexByOffsetCallback (System API)

```TypeScript
export type OnGetStartIndexByOffsetCallback = (totalOffset: double) => StartLineInfo
```

根据Grid的总偏移量，计算当前页面起始行的位置，用于快速滑动或反向滑动场景。  
**系统接口：** 此接口为系统接口。  
**模型约束：** 此接口仅可在Stage模型下使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnGetStartIndexByOffsetCallback = (totalOffset: double) => StartLineInfo--><!--Device-unnamed-export type OnGetStartIndexByOffsetCallback = (totalOffset: double) => StartLineInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| totalOffset | double | Yes | 总滚动偏移量，即Grid当中第一个GridItem的顶部与Grid顶部之间的偏移量。 单位：vp。 |

**Return value:**

| Type | Description |
| --- | --- |
| [StartLineInfo](arkts-arkui-grid-startlineinfo-i-sys.md) | - |

