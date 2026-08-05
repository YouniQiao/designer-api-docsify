# RenderFit

Enum of RenderFit

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum RenderFit--><!--Device-unnamed-export declare enum RenderFit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CENTER

```TypeScript
CENTER = 0
```

Without scaling the content area, the content area is drawn in the center of the node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-CENTER = 0--><!--Device-RenderFit-CENTER = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TOP

```TypeScript
TOP = 1
```

Without scaling the content area, the content area is drawn in the top center of the node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-TOP = 1--><!--Device-RenderFit-TOP = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BOTTOM

```TypeScript
BOTTOM = 2
```

Without scaling the content area, the content area is drawn in the bottom center of the node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-BOTTOM = 2--><!--Device-RenderFit-BOTTOM = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LEFT

```TypeScript
LEFT = 3
```

Without scaling the content area, the content area is drawn in the left center of the node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-LEFT = 3--><!--Device-RenderFit-LEFT = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RIGHT

```TypeScript
RIGHT = 4
```

Without scaling the content area, the content area is drawn in the right center of the node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-RIGHT = 4--><!--Device-RenderFit-RIGHT = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TOP_LEFT

```TypeScript
TOP_LEFT = 5
```

Without scaling the content area, the content area is drawn in the top left of the node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-TOP_LEFT = 5--><!--Device-RenderFit-TOP_LEFT = 5-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TOP_RIGHT

```TypeScript
TOP_RIGHT = 6
```

Without scaling the content area, the content area is drawn in the top right of the node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-TOP_RIGHT = 6--><!--Device-RenderFit-TOP_RIGHT = 6-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BOTTOM_LEFT

```TypeScript
BOTTOM_LEFT = 7
```

Without scaling the content area, the content area is drawn in the bottom left of the node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-BOTTOM_LEFT = 7--><!--Device-RenderFit-BOTTOM_LEFT = 7-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BOTTOM_RIGHT

```TypeScript
BOTTOM_RIGHT = 8
```

Without scaling the content area, the content area is drawn in the bottom right of the node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-BOTTOM_RIGHT = 8--><!--Device-RenderFit-BOTTOM_RIGHT = 8-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RESIZE_FILL

```TypeScript
RESIZE_FILL = 9
```

Scale the length and width of the content area to the node size to fill the node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-RESIZE_FILL = 9--><!--Device-RenderFit-RESIZE_FILL = 9-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RESIZE_CONTAIN

```TypeScript
RESIZE_CONTAIN = 10
```

Scale the length or width of the content to the length or width of the node, ensuring that one side is equal, the other side is less than or equal to the corresponding side of the node, and the content after scaling is centered.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-RESIZE_CONTAIN = 10--><!--Device-RenderFit-RESIZE_CONTAIN = 10-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RESIZE_CONTAIN_TOP_LEFT

```TypeScript
RESIZE_CONTAIN_TOP_LEFT = 11
```

Scale the length or width of the content to the length or width of the node, ensuring that one side is equal, the other side is less than or equal to the corresponding side of the node. If the height of the scaled content is less than or equal to the height of the node, the scaled content area is displayed at the top; otherwise, the width of the scaled content is less than or equal to the width of the node, the scaled content area is displayed at the left.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-RESIZE_CONTAIN_TOP_LEFT = 11--><!--Device-RenderFit-RESIZE_CONTAIN_TOP_LEFT = 11-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RESIZE_CONTAIN_BOTTOM_RIGHT

```TypeScript
RESIZE_CONTAIN_BOTTOM_RIGHT = 12
```

Scale the length or width of the content to the length or width of the node, ensuring that one side is equal, the other side is less than or equal to the corresponding side of the node. If the height of the scaled content is less than or equal to the height of the node, the scaled content area is displayed at the bottom; otherwise, the width of the scaled content is less than or equal to the width of the node, the scaled content area is displayed at the right.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-RESIZE_CONTAIN_BOTTOM_RIGHT = 12--><!--Device-RenderFit-RESIZE_CONTAIN_BOTTOM_RIGHT = 12-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RESIZE_COVER

```TypeScript
RESIZE_COVER = 13
```

Scale the length or width of the content to the length or width of the node, ensuring that one side is equal, the other side is greater than or equal to the corresponding side of the node, and the content after scaling displays the center area.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-RESIZE_COVER = 13--><!--Device-RenderFit-RESIZE_COVER = 13-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RESIZE_COVER_TOP_LEFT

```TypeScript
RESIZE_COVER_TOP_LEFT = 14
```

Scale the length or width of the content to the length or width of the node, ensuring that one side is equal, the other side is greater than or equal to the corresponding side of the node. If the height of the scaled content is greater than or equal to the height of the node, the scaled content area displays the top area; otherwise, the width of the scaled content is greater than or equal to the width of the node, the scaled content area displays the left area.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-RESIZE_COVER_TOP_LEFT = 14--><!--Device-RenderFit-RESIZE_COVER_TOP_LEFT = 14-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RESIZE_COVER_BOTTOM_RIGHT

```TypeScript
RESIZE_COVER_BOTTOM_RIGHT = 15
```

Scale the length or width of the content to the length or width of the node, ensuring that one side is equal, the other side is greater than or equal to the corresponding side of the node. If the height of the scaled content is greater than or equal to the height of the node, the scaled content area displays the bottom area; otherwise, the width of the scaled content is greater than or equal to the width of the node, the scaled content area displays the right area.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderFit-RESIZE_COVER_BOTTOM_RIGHT = 15--><!--Device-RenderFit-RESIZE_COVER_BOTTOM_RIGHT = 15-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

