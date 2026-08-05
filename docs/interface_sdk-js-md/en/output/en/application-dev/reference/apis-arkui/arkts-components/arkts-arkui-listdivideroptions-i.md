# ListDividerOptions

Defines the divider style of the list or list item group. > **NOTE** > > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface ListDividerOptions--><!--Device-unnamed-declare interface ListDividerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

Color of the divider. Anonymous Object Rectification. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Default value\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: 0x08000000 \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_

**Type:** ResourceColor

**Default:** 0x08000000 [since 18]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListDividerOptions-color?: ResourceColor--><!--Device-ListDividerOptions-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## endMargin

```TypeScript
endMargin?: Length
```

Distance between the divider and the end edge of the list. Anonymous Object Rectification. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Default value\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: **0**\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_Unit: vp \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_ \_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_If this parameter is set to a negative number or a percentage, the default value will be used. \_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_If \_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_endMargin\_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_ and \_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_startMargin\_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_ add up to a value that exceeds the column width, they will be set to \_\_\_HTML\_TAG\_DESC\_USD\_13\_\_\_0\_\_\_HTML\_TAG\_DESC\_USD\_14\_\_\_. \_\_\_HTML\_TAG\_DESC\_USD\_15\_\_\_

**Type:** Length

**Default:** 0vp [since 18]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListDividerOptions-endMargin?: Length--><!--Device-ListDividerOptions-endMargin?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startMargin

```TypeScript
startMargin?: Length
```

Distance between the divider and the start edge of the list. Anonymous Object Rectification. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Default value\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: **0**\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_Unit: vp \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_ \_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_If this parameter is set to a negative number or a percentage, the default value will be used. \_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_If \_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_endMargin\_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_ and \_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_startMargin\_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_ add up to a value that exceeds the column width, they will be set to \_\_\_HTML\_TAG\_DESC\_USD\_13\_\_\_0\_\_\_HTML\_TAG\_DESC\_USD\_14\_\_\_. \_\_\_HTML\_TAG\_DESC\_USD\_15\_\_\_

**Type:** Length

**Default:** 0vp [since 18]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListDividerOptions-startMargin?: Length--><!--Device-ListDividerOptions-startMargin?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth: Length
```

Width of the divider. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Unit: vp Anonymous Object Rectification. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_If this parameter is set to a negative number, a percentage, or a value greater than or equal to the length of the list content area, the value \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_0\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_ will be used. \_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_

**Type:** Length

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListDividerOptions-strokeWidth: Length--><!--Device-ListDividerOptions-strokeWidth: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

