# @ohos.arkui.componentSnapshot

The **componentSnapshot** module provides APIs for obtaining component snapshots, including snapshots of components that have been loaded and snapshots of components that have not been loaded yet. Snapshots are strictly limited to the component's layout bounds. Content drawn outside the area of the owning component or the parent component is not visible in the snapshots. In addition, sibling components stacked in the component's area are not displayed in the snapshot. Transformation attributes such as scaling, translation, and rotation only apply to the child components of the target component. Applying these transformation attributes directly to the target component itself has no effect; the snapshot will still display the component as it appears before any transformations are applied. For typical use cases (for example, long screenshots) and best practices of component snapshots, see [Using Component Snapshot (ComponentSnapshot)](../../../ui/arkts-uicontext-component-snapshot.md). > **NOTE：**> > - In scenarios where XComponent is used to, for example, display video or camera streams, > obtain images through > [createPixelMapFromSurface](../../apis-image-kit/arkts-apis/arkts-image-image-createpixelmapfromsurface-f.md#createPixelMapFromSurface), > instead of through an API in this module. > > - If the content of a component does not fill the entire area allocated for it, any remaining space in the snapshot > will be rendered as transparent pixels. In addition, if the component uses image effects or other > effect-related attributes, the resulting snapshot may not be as expected. To address these potential issues, check > whether the component's transparent content area needs to be filled, or use the window screenshot API > [snapshot](arkts-arkui-window-window-i.md#snapshot) instead. > > - You can preview how this component looks on a real device, but not in DevEco Studio Previewer.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace componentSnapshot--><!--Device-unnamed-declare namespace componentSnapshot-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { componentSnapshot } from '@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createFromBuilder](arkts-arkui-componentsnapshot-createfrombuilder-f.md#createFromBuilder) |
| [createFromBuilder](arkts-arkui-componentsnapshot-createfrombuilder-f.md#createFromBuilder) |
| [get](arkts-arkui-componentsnapshot-get-f.md#get) |
| [get](arkts-arkui-componentsnapshot-get-f.md#get) |
| [getSync](arkts-arkui-componentsnapshot-getsync-f.md#getSync) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ColorModeOptions](arkts-arkui-componentsnapshot-colormodeoptions-i.md) |
| [DynamicRangeModeOptions](arkts-arkui-componentsnapshot-dynamicrangemodeoptions-i.md) |
| [LocalizedSnapshotRegion](arkts-arkui-componentsnapshot-localizedsnapshotregion-i.md) |
| [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) |
| [SnapshotRegion](arkts-arkui-componentsnapshot-snapshotregion-i.md) |
| [SnapshotSizeLimitation](arkts-arkui-componentsnapshot-snapshotsizelimitation-i.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SnapshotRegionType](arkts-arkui-componentsnapshot-snapshotregiontype-t.md) |
