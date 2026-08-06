# ContextMenuOptions

Configures menu item information.

**Table 1: Menu offset when both offset and placement are set**

| Value of placement | Menu Offset |  
| ------------------------------------------------------------ | ------------------------------------------------------------ |  
| Placement.TopLeft, Placement.Top, or Placement.TopRight | If the value of **x** is a positive number for **offset**, the menu shifts to the right relative to the component. If the value of **y** is a positive number, the menu shifts upward relative to the component.|  
| Placement.BottomLeft, Placement.Bottom, or Placement.BottomRight| If the value of **x** is a positive number for **offset**, the menu shifts to the left relative to the component. If the value of **y** is a positive number, the menu shifts downward relative to the component.|  
| Placement.RightTop, Placement.Right, or Placement.RightBottom | If the value of **x** is a positive number for **offset**, the menu shifts to the right relative to the component. If the value of **y** is a positive number, the menu shifts downward relative to the component.|

**Table 2: Default position of the menu arrow when both arrowOffset and placement are set**

| Value of placement | Menu Arrow Position |  
| ------------------------------------------- | ------------------------------------------------------------ |  
| Placement.Top or Placement.Bottom | The arrow is displayed horizontally and centered by default, with a distance from the left edge of the menu equal to the arrow's safe distance.|  
| Placement.Left or Placement.Right | The arrow is displayed vertically and centered by default, with a distance from the top edge of the menu equal to the arrow's safe distance.|  
| Placement.TopLeft or Placement.BottomLeft | The arrow is displayed horizontally by default, with a distance from the left edge of the menu equal to the arrow's safe distance.|  
| Placement.TopRight or Placement.BottomRight | The arrow is displayed horizontally by default, with a distance from the right edge of the menu equal to the arrow's safe distance. |  
| Placement.LeftTop or Placement.RightTop | The arrow is displayed vertically by default, with a distance from the top edge of the menu equal to the arrow's safe distance. |  
| Placement.LeftBottom or Placement.RightBottom| The arrow is displayed vertically by default, with a distance from the bottom edge of the menu equal to the arrow's safe distance. |

**Table 3 Default menu position when enableArrow is set to true and placement is not set or set to an invalid value**  
| API| Default Menu Position|  
|------|-------------|  
| [bindMenu]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ | Placement.BottomLeft |  
| [bindMenu\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_11+\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ | Placement.BottomLeft |  
| [bindContextMenu\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_8+\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ | Placement.Top |  
| [bindContextMenu\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_12+\_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ | Placement.BottomLeft |  
| [bindContextMenuWithResponse\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_23+\_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ | Placement.Top |

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface ContextMenuOptions--><!--Device-unnamed-declare interface ContextMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## distortionMode

```TypeScript
distortionMode?: DistortionMode
```

Sets the distortion animation Mode of the menu.

**Type:** DistortionMode

**Default:** DistortionMode.DISTORTION_AUTO

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-distortionMode?: DistortionMode--><!--Device-ContextMenuOptions-distortionMode?: DistortionMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## edgeLightMode

```TypeScript
edgeLightMode?: EdgeLightMode
```

Sets the edgeLight animation Mode of the menu.

**Type:** EdgeLightMode

**Default:** EdgeLightMode.EDGELIGHT_DISABLED

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-edgeLightMode?: EdgeLightMode--><!--Device-ContextMenuOptions-edgeLightMode?: EdgeLightMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

