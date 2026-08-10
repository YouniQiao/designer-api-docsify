# ArcDotIndicator

提供弧形圆点指示器属性及功能。

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

设置弧形指示器的方向。未通过该接口设置时，形指示器的方向默认为6点钟方向。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcDotIndicator-arcDirection(direction: ArcDirection | undefined): ArcDotIndicator--><!--Device-ArcDotIndicator-arcDirection(direction: ArcDirection | undefined): ArcDotIndicator-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | [ArcDirection](arkts-arkui-arkui-arcswiper-arcdirection-e.md) \| undefined | Yes | 设置弧形指示器的方向。&lt;br/&gt;取值为undefined时，弧形指示器的方向为6点钟方向。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) | 提供弧形圆点指示器属性及功能。 |

## backgroundColor

```TypeScript
backgroundColor(color: ResourceColor | undefined): ArcDotIndicator
```

设置弧形指示器被长按时，弧形指示器的颜色。未通过该接口设置时，弧形指示器被长按时，弧形指示器的颜色默认为'#FF404040'。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcDotIndicator-backgroundColor(color: ResourceColor | undefined): ArcDotIndicator--><!--Device-ArcDotIndicator-backgroundColor(color: ResourceColor | undefined): ArcDotIndicator-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 设置弧形指示器被长按时，弧形指示器的颜色。&lt;br/&gt;取值为undefined时，弧形指示器被长按时，弧形指示器的颜色为'#FF404040' 。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) | 提供弧形圆点指示器属性及功能。 |

## constructor

```TypeScript
constructor()
```

ArcDotIndicator的构造函数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcDotIndicator-constructor()--><!--Device-ArcDotIndicator-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## itemColor

```TypeScript
itemColor(color: ResourceColor | undefined): ArcDotIndicator
```

设置弧形指示器中，未选中导航点的颜色。未通过该接口设置时，未选中导航点的颜色默认为'#A9FFFFFF'。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcDotIndicator-itemColor(color: ResourceColor | undefined): ArcDotIndicator--><!--Device-ArcDotIndicator-itemColor(color: ResourceColor | undefined): ArcDotIndicator-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 设置弧形指示器中，未选中导航点的颜色。&lt;br/&gt;取值为undefined时，未选中导航点的颜色为'#A9FFFFFF'。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) | 提供弧形圆点指示器属性及功能。 |

## maskColor

```TypeScript
maskColor(color: LinearGradient | undefined): ArcDotIndicator
```

设置弧形指示器的遮罩渐变色。未通过该接口设置时，弧形指示器的遮罩渐变色起始颜色默认为'#00000000'，结束颜色默认为'#FF000000'。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcDotIndicator-maskColor(color: LinearGradient | undefined): ArcDotIndicator--><!--Device-ArcDotIndicator-maskColor(color: LinearGradient | undefined): ArcDotIndicator-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [LinearGradient](../arkts-components/arkts-arkui-lineargradient-i.md) \| undefined | Yes | 设置弧形指示器的遮罩渐变色。&lt;br/&gt;取值为undefined时，弧形指示器的遮罩渐变色起始颜色为'#00000000'，结束颜色为'# FF000000'。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) | 提供弧形圆点指示器属性及功能。 |

## selectedItemColor

```TypeScript
selectedItemColor(color: ResourceColor | undefined): ArcDotIndicator
```

设置弧形指示器中，选中导航点的颜色。未通过该接口设置时，选中导航点的颜色默认为'#FF5EA1FF'。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcDotIndicator-selectedItemColor(color: ResourceColor | undefined): ArcDotIndicator--><!--Device-ArcDotIndicator-selectedItemColor(color: ResourceColor | undefined): ArcDotIndicator-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 设置弧形指示器中，选中导航点的颜色。&lt;br/&gt;取值为undefined时，选中导航点的颜色为'#FF5EA1FF'。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) | 提供弧形圆点指示器属性及功能。 |

