# NavContentInfo

跳转Destination信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavContentInfo--><!--Device-unnamed-export declare interface NavContentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: int
```

NavDestination在NavPathStack中的序号， 如果为根视图(NavBar)，则返回值为 -1。取值应为≥-1的整数。取值范围为全体整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavContentInfo-index: int--><!--Device-NavContentInfo-index: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode?: NavDestinationMode
```

NavDestination的模式，如果是根视图(NavBar)，则返回值为undefined。默认值： NavDestinationMode.STANDARD。

**Type:** [NavDestinationMode](../arkts-components/arkts-arkui-navdestinationmode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavContentInfo-mode?: NavDestinationMode--><!--Device-NavContentInfo-mode?: NavDestinationMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name?: string
```

NavDestination名称，如果为根视图(NavBar)，则返回值为undefined。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavContentInfo-name?: string--><!--Device-NavContentInfo-name?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navDestinationId

```TypeScript
navDestinationId?: string
```

NavDestination的唯一标识符。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavContentInfo-navDestinationId?: string--><!--Device-NavContentInfo-navDestinationId?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## param

```TypeScript
param?: Object
```

NavDestination页面加载的参数。

**Type:** Object

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavContentInfo-param?: Object--><!--Device-NavContentInfo-param?: Object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

