# @ohos.arkui.advanced.ToolBarContainer

## Modules to Import

```TypeScript
import { ToolBarState, DockArea, DockCornerMode, ToolBarSafeAreaMode, HandednessAdaptationMode, ToolBarFloatingOptions, ToolBarFloatingConfigs, ToolBarMinimizeOptions, ToolBarMinimizeConfigs, ToolBarController, ToolBarInitialParams, ToolBarParams, ToolBarConfigs, ToolBarCallbacks, ToolBarDockOffsetOptions, ToolBarSafeAreaOptions, ToolBarContainerOptions, ToolBarContainerConfigs, ToolBarContainer, ToolBarDragStateCallback, ToolBarDragOffsetCallback, ToolBarStateCallback, ToolBarDockCallback, } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ToolBarCallbacks](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcallbacks-c.md) | Defines a collection of callbacks for toolbar dragging, snapping, and state changes. |
| [ToolBarConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarconfigs-c.md) | Observable configuration store for the toolbar, corresponding to [ToolBarParams](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarparams-i.md). |
| [ToolBarContainerConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcontainerconfigs-c.md) | Observable configuration store for the toolbar container, corresponding to [ToolBarContainerOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcontaineroptions-i.md). |
| [ToolBarController](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcontroller-c.md) | Defines a controller for imperatively managing toolbar docking, pinning, and minimization states. |
| [ToolBarFloatingConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarfloatingconfigs-c.md) | Observable configuration store for floating toolbar behavior, corresponding to [ToolBarFloatingOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarfloatingoptions-i.md). |
| [ToolBarMinimizeConfigs](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarminimizeconfigs-c.md) | Observable configuration store for the minimized floating ball, corresponding to [ToolBarMinimizeOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarminimizeoptions-i.md). |

### Structs

| Name | Description |
| --- | --- |
| [ToolBarContainer](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcontainer-s.md) | The ToolBarContainer component hosts one or more floating toolbars, and supports docking, safe area avoidance, and handedness adaptation. |

### Interfaces

| Name | Description |
| --- | --- |
| [ToolBarContainerOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarcontaineroptions-i.md) | Defines options for configuring the layout, safe area avoidance, and handedness adaptation of the toolbar container. |
| [ToolBarDockOffsetOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbardockoffsetoptions-i.md) | Defines options for configuring the docking offsets of the floating toolbar on each edge. |
| [ToolBarFloatingOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarfloatingoptions-i.md) | Defines options for configuring the floating behavior of the toolbar. |
| [ToolBarInitialParams](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarinitialparams-i.md) | Initial position parameters of the toolbar, specifying the docking area, direction, and state at creation. |
| [ToolBarMinimizeOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarminimizeoptions-i.md) | Defines options for configuring the minimized floating ball of the toolbar. |
| [ToolBarParams](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarparams-i.md) | Parameters for constructing a toolbar, including the item list, modifier, floating configuration, and callbacks. |
| [ToolBarSafeAreaOptions](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarsafeareaoptions-i.md) | Defines options for configuring the safe area avoidance mode of the toolbar on each edge. |

### Types

| Name | Description |
| --- | --- |
| [ToolBarDockCallback](arkts-arkui-toolbardockcallback-t.md) | Defines the callback invoked when the toolbar docks to the specified area and direction. |
| [ToolBarDragOffsetCallback](arkts-arkui-toolbardragoffsetcallback-t.md) | Defines the callback for the drag offset relative to the ToolBarContainer container. |
| [ToolBarDragStateCallback](arkts-arkui-toolbardragstatecallback-t.md) | Defines the callback invoked when the drag state of the toolbar changes, specifically when dragging starts or ends. |
| [ToolBarStateCallback](arkts-arkui-toolbarstatecallback-t.md) | Defines the callback invoked when the toolbar state changes. |

### Enums

| Name | Description |
| --- | --- |
| [DockArea](arkts-arkui-arkui-advanced-toolbarcontainer-dockarea-e.md) | Defines the areas where the floating toolbar can dock. |
| [DockCornerMode](arkts-arkui-arkui-advanced-toolbarcontainer-dockcornermode-e.md) | Defines the snapping mode used when the floating toolbar is dragged to a corner. |
| [HandednessAdaptationMode](arkts-arkui-arkui-advanced-toolbarcontainer-handednessadaptationmode-e.md) | Defines the handedness adaptation mode for the toolbar. |
| [ToolBarSafeAreaMode](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarsafeareamode-e.md) | Defines the safe area padding mode of the toolbar. |
| [ToolBarState](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarstate-e.md) | Defines the toolbar states. |
