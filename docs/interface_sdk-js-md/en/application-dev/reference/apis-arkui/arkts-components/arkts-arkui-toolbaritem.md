# ToolBarItem

You can use the **ToolBarItem** component to add toolbar items to the title bar using the
[toolbar](docroot://reference/apis-arkui/arkui-ts/ts-universal-attributes-toolbar.md#toolbar) universal attribute.

> **NOTE**
>
> This component is typically used with the
> [toolbar](docroot://reference/apis-arkui/arkui-ts/ts-universal-attributes-toolbar.md#toolbar) universal attribute.

## Child Components

This component can contain a single child component.

## ToolBarItem

```TypeScript
ToolBarItem(options?: ToolBarItemOptions)
```

Creates a toolbar item at the beginning of the corresponding column in the title bar by default. The column position is determined by the component's  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ attribute configuration.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarItemInterface-(options?: ToolBarItemOptions): ToolBarItemAttribute--><!--Device-ToolBarItemInterface-(options?: ToolBarItemOptions): ToolBarItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Optional parameters for **ToolBarItem**, including the **placement** parameter of the [ToolBarItemPlacement]\_\_\_JSDOC\_LINK\_USD\_0\_\_\_ type.\_\_\_HTML\_TAG\_USD\_1\_\_\_Default value: **placement: ToolBarItemPlacement.TOP\_BAR\_LEADING**  |

## Summary

