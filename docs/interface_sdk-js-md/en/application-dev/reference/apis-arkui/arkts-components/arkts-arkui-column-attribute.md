# Column properties/events

In addition to the universal attributes, the following attributes are supported.The universal events are supported.

**Inheritance/Implementation:** ColumnAttribute extends CommonMethod<ColumnAttribute>

**Since:** 7

<!--Device-unnamed-declare class ColumnAttribute--><!--Device-unnamed-declare class ColumnAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## alignItems

```TypeScript
alignItems(value: HorizontalAlign)
```

Alignment mode of the child components in the horizontal direction.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ColumnAttribute-alignItems(value: HorizontalAlign): ColumnAttribute--><!--Device-ColumnAttribute-alignItems(value: HorizontalAlign): ColumnAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | HorizontalAlign | Yes | Alignment mode of child components in the horizontal direction.<br>Default value: **HorizontalAlign.Center |

## justifyContent

```TypeScript
justifyContent(value: FlexAlign)
```

Alignment mode of the child components in the vertical direction.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ColumnAttribute-justifyContent(value: FlexAlign): ColumnAttribute--><!--Device-ColumnAttribute-justifyContent(value: FlexAlign): ColumnAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | FlexAlign | Yes | Alignment mode of child components in the vertical direction.<br>Default value: **FlexAlign.Start |

## reverse

```TypeScript
reverse(isReversed: Optional<boolean>)
```

Sets whether to reverse the vertical arrangement of child components.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ColumnAttribute-reverse(isReversed: Optional<boolean>): ColumnAttribute--><!--Device-ColumnAttribute-reverse(isReversed: Optional<boolean>): ColumnAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isReversed | Optional&lt;boolean&gt; | Yes | Whether to reverse the vertical arrangement of child components.<br> Default value: **true**. **true**: Child components are arranged in reverse order vertically. **false**: Child components are arranged in normal order vertically. |

