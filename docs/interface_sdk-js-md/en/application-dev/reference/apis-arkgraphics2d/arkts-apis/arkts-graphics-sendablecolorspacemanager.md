# @ohos.graphics.sendableColorSpaceManager(Sendable Color Space Management)

This module provides APIs for creating and managing sendable color space objects and obtaining basic attributes of sendable color spaces. It is applicable to scenarios where color space information needs to be transferred between multiple threads. It solves the problem that color management objects cannot be shared across threads, improving the efficiency and consistency of color processing.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare namespace sendableColorSpaceManager--><!--Device-unnamed-declare namespace sendableColorSpaceManager-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

## Summary

### Functions

| Name | Description |
| --- | --- |
| [create](arkts-arkgraphics2d-sendablecolorspacemanager-create-f.md#create) | Creates a criterion color space management instance that is sendable. |
| [create](arkts-arkgraphics2d-sendablecolorspacemanager-create-f.md#create-1) | Creates a custom color space object that is sendable. |

### Interfaces

| Name | Description |
| --- | --- |
| [ColorSpaceManager](arkts-arkgraphics2d-sendablecolorspacemanager-colorspacemanager-i.md) | Implements management of color space objects. ColorSpaceManager is a core class used to manage and operate color space objects. It provides functions such as obtaining the color space type, white point value, and gamma value,and supports transfer between concurrent ArkTS instances.  Before calling any of the following APIs, you must use [create()]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ to create a color space manager. |

### Types

| Name | Description |
| --- | --- |
| [ISendable](arkts-arkgraphics2d-sendablecolorspacemanager-isendable-t.md) | The ISendable type alias is defined to align with the API specifications of the current module. |

