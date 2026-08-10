# ComposeListItemV2

列表组件，可自定义列表左侧、中间元素以及右侧显示内容。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @ComponentV2

<!--Device-unnamed-export declare struct ComposeListItemV2--><!--Device-unnamed-export declare struct ComposeListItemV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OperateCheckV2Options, ComposeListItemV2, IconTypeV2, OperateIconV2, OperateCheckV2, OperateItemV2, OperateItemV2Options, OperateIconV2Options, OperateButtonV2, OperateButtonV2Options, ContentItemV2, ContentItemV2Options } from 'kits/@kit.ArkUI';
```

## build

```TypeScript
build(): void
```

构建组件的方法。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeListItemV2-build(): void--><!--Device-ComposeListItemV2-build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentItemV2

```TypeScript
contentItemV2?: ContentItemV2
```

定义左侧以及中间元素。

**Type:** [ContentItemV2](arkts-arkui-arkui-advanced-composelistitemv2-contentitemv2-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeListItemV2-contentItemV2?: ContentItemV2--><!--Device-ComposeListItemV2-contentItemV2?: ContentItemV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operateItemV2

```TypeScript
operateItemV2?: OperateItemV2
```

定义右侧元素。

**Type:** [OperateItemV2](arkts-arkui-arkui-advanced-composelistitemv2-operateitemv2-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComposeListItemV2-operateItemV2?: OperateItemV2--><!--Device-ComposeListItemV2-operateItemV2?: OperateItemV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

