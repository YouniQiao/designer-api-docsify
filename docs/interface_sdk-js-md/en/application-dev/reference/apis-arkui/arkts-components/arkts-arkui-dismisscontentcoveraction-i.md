# DismissContentCoverAction

Component content cover dismiss

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface DismissContentCoverAction--><!--Device-unnamed-declare interface DismissContentCoverAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dismiss

```TypeScript
dismiss: Callback<void>
```

全屏模态页面关闭回调函数。开发者需要退出页面时调用。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DismissContentCoverAction-dismiss: Callback<void>--><!--Device-DismissContentCoverAction-dismiss: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reason

```TypeScript
reason: DismissReason
```

返回本次拦截全屏模态页面退出的事件原因。

**Type:** [DismissReason](arkts-arkui-dismissreason-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DismissContentCoverAction-reason: DismissReason--><!--Device-DismissContentCoverAction-reason: DismissReason-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

