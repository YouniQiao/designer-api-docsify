# SaveButtonOnClickResult

保存控件点击后的授权结果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare enum SaveButtonOnClickResult--><!--Device-unnamed-declare enum SaveButtonOnClickResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SUCCESS

```TypeScript
SUCCESS = 0
```

保存控件点击后权限授权成功。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SaveButtonOnClickResult-SUCCESS = 0--><!--Device-SaveButtonOnClickResult-SUCCESS = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TEMPORARY_AUTHORIZATION_FAILED

```TypeScript
TEMPORARY_AUTHORIZATION_FAILED = 1
```

保存控件点击后权限授权失败。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SaveButtonOnClickResult-TEMPORARY_AUTHORIZATION_FAILED = 1--><!--Device-SaveButtonOnClickResult-TEMPORARY_AUTHORIZATION_FAILED = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CANCELED_BY_USER

```TypeScript
CANCELED_BY_USER = 2
```

保存控件点击后，弹窗中用户取消授权。仅在调用[userCancelEvent](SaveButtonAttribute#userCancelEvent)并设置参数为true时，回调结果中才会返回该值。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-SaveButtonOnClickResult-CANCELED_BY_USER = 2--><!--Device-SaveButtonOnClickResult-CANCELED_BY_USER = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

