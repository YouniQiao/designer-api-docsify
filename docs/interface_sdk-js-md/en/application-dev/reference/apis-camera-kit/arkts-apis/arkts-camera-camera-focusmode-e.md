# FocusMode

枚举，焦距模式。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-camera-enum FocusMode--><!--Device-camera-enum FocusMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## FOCUS_MODE_MANUAL

```TypeScript
FOCUS_MODE_MANUAL = 0
```

手动对焦。通过手动修改相机焦距来改变对焦位置，不支持对焦点设置。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-FocusMode-FOCUS_MODE_MANUAL = 0--><!--Device-FocusMode-FOCUS_MODE_MANUAL = 0-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## FOCUS_MODE_CONTINUOUS_AUTO

```TypeScript
FOCUS_MODE_CONTINUOUS_AUTO = 1
```

连续自动对焦。不支持对焦点设置。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-FocusMode-FOCUS_MODE_CONTINUOUS_AUTO = 1--><!--Device-FocusMode-FOCUS_MODE_CONTINUOUS_AUTO = 1-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## FOCUS_MODE_AUTO

```TypeScript
FOCUS_MODE_AUTO = 2
```

自动对焦。支持对焦点设置，可以使用[Focus.setFocusPoint](arkts-camera-camera-focus-i.md#setfocuspoint)设置对焦点，根据对焦点执行一次自动对焦。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-FocusMode-FOCUS_MODE_AUTO = 2--><!--Device-FocusMode-FOCUS_MODE_AUTO = 2-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## FOCUS_MODE_LOCKED

```TypeScript
FOCUS_MODE_LOCKED = 3
```

对焦锁定。不支持对焦点设置。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-FocusMode-FOCUS_MODE_LOCKED = 3--><!--Device-FocusMode-FOCUS_MODE_LOCKED = 3-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

