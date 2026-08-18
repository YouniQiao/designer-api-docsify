# Select

The **Select** component provides a drop-down menu that allows users to select among multiple options. > **NOTE**

## Child Components Not supported

## Select

```TypeScript
Select(options: Array<SelectOption>)
```

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SelectInterface-(options: Array<SelectOption>): SelectAttribute--><!--Device-SelectInterface-(options: Array<SelectOption>): SelectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | Array&lt;SelectOption&gt; | Yes | Options of the drop-down menu. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [MenuItemConfiguration](arkts-arkui-menuitemconfiguration-i.md) | You need a custom class to implement the **ContentModifier** API. Inherits from CommonConfiguration. |
| [MenuOutlineOptions](arkts-arkui-menuoutlineoptions-i.md) | Defines the outline of the drop-down menu. |

### Types

| Name | Description |
| --- | --- |
| [OnSelectCallback](arkts-arkui-onselectcallback-t.md) | Defines the callback invoked when a drop-down menu option is selected. |

### Enums

| Name | Description |
| --- | --- |
| [ArrowPosition](arkts-arkui-arrowposition-e.md) | Enumerates arrow positions. |
| [AvoidanceMode](arkts-arkui-avoidancemode-e.md) | Enumerates the drop-down menu avoidance modes. |
| [MenuAlignType](arkts-arkui-menualigntype-e.md) | Enumerates drop-down menu alignment modes. |

