# @ohos.graphics.colorSpaceManager(Color Space Management)

/*
 Copyright (C) 2022-2023 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 23

<!--Device-unnamed-declare namespace colorSpaceManager--><!--Device-unnamed-declare namespace colorSpaceManager-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

## Modules to Import

```TypeScript
import { colorSpaceManager } from '@kit.ArkGraphics2D';
import { colorSpaceManager } from '@kit.ArkGraphics2D';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [create](arkts-arkgraphics2d-colorspacemanager-create-f.md#create) | Creates a standard color space object. |
| [create](arkts-arkgraphics2d-colorspacemanager-create-f.md#create) | Creates a custom color space object. |

### Interfaces

| Name | Description |
| --- | --- |
| [ColorSpaceManager](arkts-arkgraphics2d-colorspacemanager-colorspacemanager-i.md) | Implements management of color space objects. Before calling any of the following APIs, you must use [create()](arkts-arkgraphics2d-colorspacemanager-create-f.md#create) to create a color space manager. |
| [ColorSpacePrimaries](arkts-arkgraphics2d-colorspacemanager-colorspaceprimaries-i.md) | The three primary colors (red, green, blue) and white as defined by the color space standard, whose positions in the color space are represented by (x, y) coordinates based on real-world chromaticity. |

### Enums

| Name | Description |
| --- | --- |
| [ColorSpace](arkts-arkgraphics2d-colorspacemanager-colorspace-e.md) | Enumerates the color space types. |

