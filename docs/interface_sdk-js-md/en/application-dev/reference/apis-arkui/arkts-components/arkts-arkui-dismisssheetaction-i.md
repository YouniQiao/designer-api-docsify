# DismissSheetAction

半模态关闭前的回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface DismissSheetAction--><!--Device-unnamed-declare interface DismissSheetAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dismiss

```TypeScript
dismiss: Callback<void>
```

半模态页面关闭回调函数。开发者需要退出页面时调用。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DismissSheetAction-dismiss: Callback<void>--><!--Device-DismissSheetAction-dismiss: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reason

```TypeScript
reason: DismissReason
```

返回本次半模态页面退出的操作类型。

**说明：**

DismissReason.SLIDE只生效半模态侧边弹窗形态，表示右滑退出。若镜像场景则表示左滑退出。

DismissReason.SLIDE_DOWN生效半模态底部弹窗形态和居中弹窗形态，表示下滑退出。

半模态气泡弹窗形态无滑动退出能力。

**Type:** [DismissReason](arkts-arkui-dismissreason-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DismissSheetAction-reason: DismissReason--><!--Device-DismissSheetAction-reason: DismissReason-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

