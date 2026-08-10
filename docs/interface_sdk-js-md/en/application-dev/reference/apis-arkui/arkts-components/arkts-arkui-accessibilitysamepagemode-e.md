# AccessibilitySamePageMode

当前跨进程嵌入式显示的组件和宿主应用的同page模式。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare enum AccessibilitySamePageMode--><!--Device-unnamed-declare enum AccessibilitySamePageMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SEMI_SILENT

```TypeScript
SEMI_SILENT = 0
```

跨进程嵌入式显示的组件拉起来的进程的page事件中如果是首次加载页面或者该事件页面的根节点发送的page事件会被忽略。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-AccessibilitySamePageMode-SEMI_SILENT = 0--><!--Device-AccessibilitySamePageMode-SEMI_SILENT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FULL_SILENT

```TypeScript
FULL_SILENT = 1
```

跨进程嵌入式显示的组件将忽略所有的page事件。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-AccessibilitySamePageMode-FULL_SILENT = 1--><!--Device-AccessibilitySamePageMode-FULL_SILENT = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

