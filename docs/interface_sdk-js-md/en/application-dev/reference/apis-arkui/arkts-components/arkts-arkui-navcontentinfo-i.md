# NavContentInfo

跳转Destination信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface NavContentInfo--><!--Device-unnamed-declare interface NavContentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: number
```

NavDestination在NavPathStack中的序号， 如果为根视图(NavBar)，则返回值为 -1。

取值范围：[-1, +∞)。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavContentInfo-index: number--><!--Device-NavContentInfo-index: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode?: NavDestinationMode
```

NavDestination的模式，如果是根视图(NavBar)，则返回值为undefined。

**Type:** [NavDestinationMode](arkts-arkui-navdestinationmode-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavContentInfo-mode?: NavDestinationMode--><!--Device-NavContentInfo-mode?: NavDestinationMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name?: string
```

NavDestination名称，如果为根视图(NavBar)，则返回值为undefined。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavContentInfo-name?: string--><!--Device-NavContentInfo-name?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navDestinationId

```TypeScript
navDestinationId?: string
```

NavDestination的唯一标识符。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavContentInfo-navDestinationId?: string--><!--Device-NavContentInfo-navDestinationId?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## param

```TypeScript
param?: Object
```

NavDestination页面加载的参数。

**Type:** Object

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavContentInfo-param?: Object--><!--Device-NavContentInfo-param?: Object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

