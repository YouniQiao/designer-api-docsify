# @ohos.arkui.componentUtils

The **componentUtils** module provides API for obtaining the coordinates and size of the drawing area of a component.

**Since:** 10

<!--Device-unnamed-declare namespace componentUtils--><!--Device-unnamed-declare namespace componentUtils-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { componentUtils } from '@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getRectangleById](arkts-arkui-getrectanglebyid-f.md#getrectanglebyid-1) | Obtains a **ComponentInfo** object based on the component ID and synchronously returns the geometric properties of the component. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getItemsInShapePath](arkts-arkui-getitemsinshapepath-f-sys.md#getitemsinshapepath-1) | Get the image objects located within the selected area. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [ComponentInfo](arkts-arkui-componentinfo-i.md) | Implements a **ComponentInfo** object, which provides the size, position, translation, scaling, rotation, and affine matrix information of the component. |
| [Offset](arkts-arkui-offset-i.md) | Defines the offset property. |
| [RotateResult](arkts-arkui-rotateresult-i.md) | Rotation Result. |
| [ScaleResult](arkts-arkui-scaleresult-i.md) | Scale Result |
| [Size](arkts-arkui-size-i.md) | Defines the size property. |
| [TranslateResult](arkts-arkui-translateresult-i.md) | Translation Result |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [GetItemsInShapePathParams](arkts-arkui-getitemsinshapepathparams-i-sys.md) | Image options setted when need to get the image objects. |
| [ImageItem](arkts-arkui-imageitem-i-sys.md) | Image object with layout information. |
| [Rotation2D](arkts-arkui-rotation2d-i-sys.md) | Describes a rotation in 2D, which can be defined by rotation angle and rotation center. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [Matrix4Result](arkts-arkui-matrix4result-t.md) | The matrix is column-first fourth-order matrix. |

