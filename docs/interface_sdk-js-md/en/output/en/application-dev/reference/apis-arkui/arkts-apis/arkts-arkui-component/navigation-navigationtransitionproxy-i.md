# NavigationTransitionProxy

Navigation transition proxy.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavigationTransitionProxy--><!--Device-unnamed-export declare interface NavigationTransitionProxy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## finishTransition

```TypeScript
finishTransition(): void
```

Notification system transition animation completed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTransitionProxy-finishTransition(): void--><!--Device-NavigationTransitionProxy-finishTransition(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancelTransition

```TypeScript
cancelTransition?: VoidCallback
```

Notification system transition animation canceled.

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTransitionProxy-cancelTransition?: VoidCallback--><!--Device-NavigationTransitionProxy-cancelTransition?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## from

```TypeScript
from: NavContentInfo
```

From navigation content info.

**Type:** NavContentInfo

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTransitionProxy-from: NavContentInfo--><!--Device-NavigationTransitionProxy-from: NavContentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isInteractive

```TypeScript
isInteractive?: boolean
```

Indicates whether it is an interactive transition. Default value: false.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTransitionProxy-isInteractive?: boolean--><!--Device-NavigationTransitionProxy-isInteractive?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## to

```TypeScript
to: NavContentInfo
```

To navigation content info.

**Type:** NavContentInfo

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTransitionProxy-to: NavContentInfo--><!--Device-NavigationTransitionProxy-to: NavContentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## updateTransition

```TypeScript
updateTransition?: UpdateTransitionCallback
```

Notification system transition animation update.

**Type:** UpdateTransitionCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTransitionProxy-updateTransition?: UpdateTransitionCallback--><!--Device-NavigationTransitionProxy-updateTransition?: UpdateTransitionCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

