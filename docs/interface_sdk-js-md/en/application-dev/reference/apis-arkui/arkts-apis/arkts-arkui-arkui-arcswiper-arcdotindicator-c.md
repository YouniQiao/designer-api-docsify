# ArcDotIndicator

Define ArcDotIndicator, the indicator type is arc dot.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class ArcDotIndicator--><!--Device-unnamed-export declare class ArcDotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcSwiperAttribute, ArcSwiper, ArcDirection, ArcSwiperController, ArcDotIndicator } from 'kits/@kit.ArkUI';
```

## arcDirection

```TypeScript
arcDirection(direction: ArcDirection | undefined): ArcDotIndicator
```

Set the direction of arc indicator.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcDotIndicator-arcDirection(direction: ArcDirection | undefined): ArcDotIndicator--><!--Device-ArcDotIndicator-arcDirection(direction: ArcDirection | undefined): ArcDotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | [ArcDirection](arkts-arkui-arkui-arcswiper-arcdirection-e.md) \| undefined | Yes | the direction of arc indicator, default value is { ArcDirection.SIX_CLOCK_DIRECTION }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) |  |

## backgroundColor

```TypeScript
backgroundColor(color: ResourceColor | undefined): ArcDotIndicator
```

Set the background color.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcDotIndicator-backgroundColor(color: ResourceColor | undefined): ArcDotIndicator--><!--Device-ArcDotIndicator-backgroundColor(color: ResourceColor | undefined): ArcDotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | the background color, default value is { #FF404040 }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) |  |

## constructor

```TypeScript
constructor()
```

A constructor used to create a ArcDotIndicator object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcDotIndicator-constructor()--><!--Device-ArcDotIndicator-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## itemColor

```TypeScript
itemColor(color: ResourceColor | undefined): ArcDotIndicator
```

Set the navigation point color.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcDotIndicator-itemColor(color: ResourceColor | undefined): ArcDotIndicator--><!--Device-ArcDotIndicator-itemColor(color: ResourceColor | undefined): ArcDotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | the indicator item color, default value is { #A9FFFFFF }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) |  |

## maskColor

```TypeScript
maskColor(color: LinearGradient | undefined): ArcDotIndicator
```

Set the gradient color for the mask.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcDotIndicator-maskColor(color: LinearGradient | undefined): ArcDotIndicator--><!--Device-ArcDotIndicator-maskColor(color: LinearGradient | undefined): ArcDotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [LinearGradient](../arkts-components/arkts-arkui-lineargradient-i.md) \| undefined | Yes | the gradient color, default start color is { #00000000 }, default end color is { #FF000000 }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) |  |

## selectedItemColor

```TypeScript
selectedItemColor(color: ResourceColor | undefined): ArcDotIndicator
```

Set the selected navigation point color.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcDotIndicator-selectedItemColor(color: ResourceColor | undefined): ArcDotIndicator--><!--Device-ArcDotIndicator-selectedItemColor(color: ResourceColor | undefined): ArcDotIndicator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | the indicator item when selected, default value is { #FF5EA1FF }, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) |  |

