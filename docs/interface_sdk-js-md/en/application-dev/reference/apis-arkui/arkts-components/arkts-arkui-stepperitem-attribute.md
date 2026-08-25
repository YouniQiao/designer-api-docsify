# StepperItem properties/events

Defines StepperItem Component instance.

**Inheritance/Implementation:** StepperItemAttribute extends CommonMethod<StepperItemAttribute>

**Since:** 8

**Deprecated since:** 22

**Substitutes:** [SwiperAttribute](arkts-arkui-swiper-attribute.md#swiperattribute)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## nextLabel

```TypeScript
nextLabel(value: string)
```

Sets the text label of the button on the right. The default value is **Start** for the last page and **Next** for the other pages.

> **NOTE：**

**Since:** 8

**Deprecated since:** 22

**Substitutes:** showNext

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

## prevLabel

```TypeScript
prevLabel(value: string)
```

Sets the text label of the button on the left, which is not displayed on the first page. When the **Stepper** contains more than one page, the default value for all pages except the first page is **Back**.

> **NOTE：**

**Since:** 8

**Deprecated since:** 22

**Substitutes:** showPrevious

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

## status

```TypeScript
status(value?: ItemState)
```

Sets the display status of **nextLabel** in the stepper.

> **NOTE：**

**Since:** 8

**Deprecated since:** 22

**Substitutes:** [indicatorInteractive](arkts-arkui-swiper-attribute.md#indicatorinteractive)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ItemState](arkts-arkui-itemstate-e.md) | No |
