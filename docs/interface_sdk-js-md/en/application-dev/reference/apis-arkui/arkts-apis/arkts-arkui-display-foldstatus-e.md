# FoldStatus

当前可折叠设备的折叠状态枚举。如果是双折轴设备，则在充电口朝下的状态下，从右到左分别是折轴一和折轴二。

> **说明：**

> 只有一个折轴的产品包含FOLD_STATUS_EXPANDED、FOLD_STATUS_FOLDED、FOLD_STATUS_HALF_FOLDED三种折叠状态。

> 具有两个折轴的产品包含上表除FOLD_STATUS_UNKNOWN以外的九种折叠状态。

> FOLD_STATUS_UNKNOWN是一种不可用的折叠状态。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-display-enum FoldStatus--><!--Device-display-enum FoldStatus-End-->

**System capability:** SystemCapability.Window.SessionManager

## FOLD_STATUS_UNKNOWN

```TypeScript
FOLD_STATUS_UNKNOWN = 0
```

表示设备当前折叠状态无法确定或设备本身不可折叠。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldStatus-FOLD_STATUS_UNKNOWN = 0--><!--Device-FoldStatus-FOLD_STATUS_UNKNOWN = 0-End-->

**System capability:** SystemCapability.Window.SessionManager

## FOLD_STATUS_EXPANDED

```TypeScript
FOLD_STATUS_EXPANDED = 1
```

表示设备当前折叠状态为完全展开。如果是双折轴设备，则表示折轴一折叠状态为完全展开，折轴二折叠状态为折叠。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldStatus-FOLD_STATUS_EXPANDED = 1--><!--Device-FoldStatus-FOLD_STATUS_EXPANDED = 1-End-->

**System capability:** SystemCapability.Window.SessionManager

## FOLD_STATUS_FOLDED

```TypeScript
FOLD_STATUS_FOLDED = 2
```

表示设备当前折叠状态为折叠。如果是双折轴设备，则表示折轴一和折轴二的折叠状态均为折叠。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldStatus-FOLD_STATUS_FOLDED = 2--><!--Device-FoldStatus-FOLD_STATUS_FOLDED = 2-End-->

**System capability:** SystemCapability.Window.SessionManager

## FOLD_STATUS_HALF_FOLDED

```TypeScript
FOLD_STATUS_HALF_FOLDED = 3
```

表示设备当前折叠状态为半折叠。半折叠指完全展开和折叠之间的状态。如果是双折轴设备，则表示折轴一折叠状态为半折叠，折轴二折叠状态为折叠。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldStatus-FOLD_STATUS_HALF_FOLDED = 3--><!--Device-FoldStatus-FOLD_STATUS_HALF_FOLDED = 3-End-->

**System capability:** SystemCapability.Window.SessionManager

## FOLD_STATUS_EXPANDED_WITH_SECOND_EXPANDED

```TypeScript
FOLD_STATUS_EXPANDED_WITH_SECOND_EXPANDED = 11
```

表示双折轴设备折轴一和折轴二的折叠状态均为完全展开。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FoldStatus-FOLD_STATUS_EXPANDED_WITH_SECOND_EXPANDED = 11--><!--Device-FoldStatus-FOLD_STATUS_EXPANDED_WITH_SECOND_EXPANDED = 11-End-->

**System capability:** SystemCapability.Window.SessionManager

## FOLD_STATUS_EXPANDED_WITH_SECOND_HALF_FOLDED

```TypeScript
FOLD_STATUS_EXPANDED_WITH_SECOND_HALF_FOLDED = 21
```

表示双折轴设备折轴一折叠状态为完全展开，折轴二折叠状态为半折叠。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FoldStatus-FOLD_STATUS_EXPANDED_WITH_SECOND_HALF_FOLDED = 21--><!--Device-FoldStatus-FOLD_STATUS_EXPANDED_WITH_SECOND_HALF_FOLDED = 21-End-->

**System capability:** SystemCapability.Window.SessionManager

## FOLD_STATUS_FOLDED_WITH_SECOND_HALF_FOLDED

```TypeScript
FOLD_STATUS_FOLDED_WITH_SECOND_HALF_FOLDED = 22
```

表示双折轴设备折轴一折叠状态为折叠，折轴二折叠状态为半折叠。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FoldStatus-FOLD_STATUS_FOLDED_WITH_SECOND_HALF_FOLDED = 22--><!--Device-FoldStatus-FOLD_STATUS_FOLDED_WITH_SECOND_HALF_FOLDED = 22-End-->

**System capability:** SystemCapability.Window.SessionManager

## FOLD_STATUS_HALF_FOLDED_WITH_SECOND_HALF_FOLDED

```TypeScript
FOLD_STATUS_HALF_FOLDED_WITH_SECOND_HALF_FOLDED = 23
```

表示双折轴设备折轴一和折轴二的折叠状态均为半折叠。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FoldStatus-FOLD_STATUS_HALF_FOLDED_WITH_SECOND_HALF_FOLDED = 23--><!--Device-FoldStatus-FOLD_STATUS_HALF_FOLDED_WITH_SECOND_HALF_FOLDED = 23-End-->

**System capability:** SystemCapability.Window.SessionManager

## FOLD_STATUS_FOLDED_WITH_SECOND_EXPANDED

```TypeScript
FOLD_STATUS_FOLDED_WITH_SECOND_EXPANDED = 12
```

表示双折轴设备折轴一折叠状态为折叠，折轴二折叠状态为完全展开。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FoldStatus-FOLD_STATUS_FOLDED_WITH_SECOND_EXPANDED = 12--><!--Device-FoldStatus-FOLD_STATUS_FOLDED_WITH_SECOND_EXPANDED = 12-End-->

**System capability:** SystemCapability.Window.SessionManager

## FOLD_STATUS_HALF_FOLDED_WITH_SECOND_EXPANDED

```TypeScript
FOLD_STATUS_HALF_FOLDED_WITH_SECOND_EXPANDED = 13
```

表示双折轴设备折轴一折叠状态为半折叠，折轴二折叠状态为完全展开。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FoldStatus-FOLD_STATUS_HALF_FOLDED_WITH_SECOND_EXPANDED = 13--><!--Device-FoldStatus-FOLD_STATUS_HALF_FOLDED_WITH_SECOND_EXPANDED = 13-End-->

**System capability:** SystemCapability.Window.SessionManager

