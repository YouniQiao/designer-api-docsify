# ModalMode

子窗菜单的模态模式。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-unnamed-declare enum ModalMode--><!--Device-unnamed-declare enum ModalMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AUTO

```TypeScript
AUTO = 0
```

自动模式，菜单组件在当前设备的默认行为。当前版本在所有设备上的效果等同于ModalMode.NONE。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ModalMode-AUTO = 0--><!--Device-ModalMode-AUTO = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 1
```

除菜单自身区域外，其他区域均可传递事件，下层控件可响应事件。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ModalMode-NONE = 1--><!--Device-ModalMode-NONE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TARGET_WINDOW

```TypeScript
TARGET_WINDOW = 2
```

菜单所在应用的窗口与菜单区域不可传递事件，其他区域可传递事件。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ModalMode-TARGET_WINDOW = 2--><!--Device-ModalMode-TARGET_WINDOW = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

