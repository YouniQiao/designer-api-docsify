# RouterMode

Router Mode

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-router-export enum RouterMode--><!--Device-router-export enum RouterMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Standard

```TypeScript
Standard
```

Default route mode. The page will be added to the top of the page stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RouterMode-Standard--><!--Device-RouterMode-Standard-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Single

```TypeScript
Single
```

Single route mode. If the target page already has the same url page in the page stack, the same url page closest to the top of the stack will be moved to the top of the stack. If the target page url does not exist in the page stack, route will use default route mode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RouterMode-Single--><!--Device-RouterMode-Single-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

