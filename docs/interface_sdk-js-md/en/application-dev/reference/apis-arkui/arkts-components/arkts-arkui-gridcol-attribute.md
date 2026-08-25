# GridCol properties/events

In addition to the [universal attributes](arkts-arkui-commonmethod-c.md), the following attributes are supported.The [universal events](arkts-arkui-commonmethod-c.md) are supported.

**Inheritance/Implementation:** GridColAttribute extends CommonMethod<GridColAttribute>

**Since:** 9

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## gridColOffset

```TypeScript
gridColOffset(value: number | GridColColumnOption)
```

Sets the number of offset columns relative to the original position of the component.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| [GridColColumnOption](arkts-arkui-gridcolcolumnoption-i.md) | Yes |

## order

```TypeScript
order(value: number | GridColColumnOption)
```

Sets the display order of the grid child component. Grid child components are sorted in ascending order based on their sequence numbers.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| [GridColColumnOption](arkts-arkui-gridcolcolumnoption-i.md) | Yes |

## span

```TypeScript
span(value: number | GridColColumnOption)
```

Sets the number of columns occupied by the component. If it is set to **0**, the element is not involved in layout calculation, that is, the element is not rendered.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| [GridColColumnOption](arkts-arkui-gridcolcolumnoption-i.md) | Yes |
