# Toggle

The **Toggle** component provides a clickable element of the checkbox, button, or switch type. > **NOTE**

## Child Components This component can contain child components only when **ToggleType** is set to **Button**.

## Toggle

```TypeScript
Toggle(options: ToggleOptions)
```

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ToggleInterface-(options: ToggleOptions): ToggleAttribute--><!--Device-ToggleInterface-(options: ToggleOptions): ToggleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToggleOptions](arkts-arkui-toggleoptions-i.md) | Yes | Options of the toggle. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [SwitchStyle](arkts-arkui-switchstyle-i.md) | Sets the style for the component of the **Switch** type. |
| [ToggleConfiguration](arkts-arkui-toggleconfiguration-i.md) | You need a custom class to implement the **ContentModifier** API. This API inherits from CommonConfiguration. |
| [ToggleOptions](arkts-arkui-toggleoptions-i.md) | Options of the toggle. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is larger than inner elements'. This does not affect interface usability. |

### Enums

| Name | Description |
| --- | --- |
| [ToggleType](arkts-arkui-toggletype-e.md) | Enumerates toggle types. |

