# ArcDotIndicator

Describes the properties and behavior of the arc dot navigation indicator.

**Since:** 18

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcSwiper, ArcSwiperAttribute, ArcDotIndicator, ArcDirection, ArcSwiperController } from 'kits/@kit.ArkUI';
```

## arcDirection

```TypeScript
arcDirection(direction: Optional<ArcDirection>): ArcDotIndicator
```

Sets the direction of the arc navigation indicator.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| direction | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[ArcDirection](arkts-arkui-arkui-arcswiper-arcdirection-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) |

## backgroundColor

```TypeScript
backgroundColor(color: Optional<ResourceColor>): ArcDotIndicator
```

Sets the color of the arc navigation indicator when it is number-pressed.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) |

## constructor

```TypeScript
constructor()
```

A constructor used to create an **ArcDotIndicator** instance.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## itemColor

```TypeScript
itemColor(color: Optional<ResourceColor>): ArcDotIndicator
```

Sets the color of the unselected navigation points in the arc navigation indicator.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) |

## maskColor

```TypeScript
maskColor(color: Optional<LinearGradient>): ArcDotIndicator
```

Sets the mask gradient color of the arc navigation indicator.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;LinearGradient&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) |

## selectedItemColor

```TypeScript
selectedItemColor(color: Optional<ResourceColor>): ArcDotIndicator
```

Sets the color of the selected navigation point in the arc navigation indicator.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) |
