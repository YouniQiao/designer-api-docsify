# Action

触屏输入事件类型。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare enum Action--><!--Device-unnamed-export declare enum Action-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## CANCEL

```TypeScript
CANCEL = 0
```

触屏取消。触屏down事件异常打断，未正常闭环，例如：手指按下后未抬起，屏幕发生旋转、折叠或有新hover等场景时触发cancel事件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Action-CANCEL = 0--><!--Device-Action-CANCEL = 0-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## DOWN

```TypeScript
DOWN = 1
```

触屏按下。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Action-DOWN = 1--><!--Device-Action-DOWN = 1-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## MOVE

```TypeScript
MOVE = 2
```

触屏移动。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Action-MOVE = 2--><!--Device-Action-MOVE = 2-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## UP

```TypeScript
UP = 3
```

触屏抬起。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Action-UP = 3--><!--Device-Action-UP = 3-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## PULL_DOWN

```TypeScript
PULL_DOWN = 4
```

触屏开始拖拽。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Action-PULL_DOWN = 4--><!--Device-Action-PULL_DOWN = 4-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## PULL_MOVE

```TypeScript
PULL_MOVE = 5
```

触屏拖拽移动。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Action-PULL_MOVE = 5--><!--Device-Action-PULL_MOVE = 5-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## PULL_UP

```TypeScript
PULL_UP = 6
```

触屏结束拖拽。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Action-PULL_UP = 6--><!--Device-Action-PULL_UP = 6-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

