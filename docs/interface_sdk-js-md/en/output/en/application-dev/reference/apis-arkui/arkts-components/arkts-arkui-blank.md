# Blank

The **Blank** component is a spacer in the layout, automatically filling the remaining space along the main axis of its parent container. It works only when the parent component is [Row]{@link Row}, [Column]{@link Column}, or [Flex]{@link Flex}. > **Child Components** > > No child component can be set.

## Blank

```TypeScript
Blank(min?: number | string)
```

Creates a **Blank** component. Since API version 10: - When the **Blank** component is used within a [Row]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, [Column]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, or [Flex]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ container, it will automatically stretch or shrink along the main axis if it does not have a main axis size specified. If the **Blank** component has a main axis size specified or if the container is set to adapt to the size of its child nodes, the component will not automatically stretch or shrink. - Relationship between **size** and **min** of the **Blank** component on the main axis: max(min, size). - If the **Blank** component has a cross axis size specified, it will not fill up the parent container on the cross axis. If it does not have a cross axis size specified, it will fill up the parent container on the cross axis, following the **ItemAlign.Stretch** mode, the default setting of **alignSelf**.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BlankInterface-(min?: number | string): BlankAttribute--><!--Device-BlankInterface-(min?: number | string): BlankAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| min | number \| string | No | Minimum size of the **Blank** component in the container along the main axis.\_\_\_HTML\_TAG\_USD\_0\_\_\_ Default value: **0**\_\_\_HTML\_TAG\_USD\_1\_\_\_If the type is number, the default unit is vp. If the type is string, the pixel unit can be explicitly specified, for example, '**10px**'. If the unit is not specified, the default unit vp is used, in which case **'10'** is equivalent to **10vp**.\_\_\_HTML\_TAG\_USD\_2\_\_\_Invalid values are treated as the default value.\_\_\_HTML\_TAG\_USD\_3\_\_\_**NOTE**\_\_\_HTML\_TAG\_USD\_4\_\_\_This parameter cannot be set in percentage. If the value is negative, the default value is used. If the minimum size is larger than the available space of the container, it is used as the component size, and the component extends beyond the container.  |

## Summary

