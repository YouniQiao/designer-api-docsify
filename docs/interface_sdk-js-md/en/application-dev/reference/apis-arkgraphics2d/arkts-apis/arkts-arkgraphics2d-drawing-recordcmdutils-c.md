# RecordCmdUtils

This class offers a set of operations to generate drawing commands.

**Since:** 26.1.0

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## beginRecording

```TypeScript
beginRecording(width: number, height: number): Canvas
```

Gets the canvas that records the drawing commands.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes | Indicates the width of the canvas object. Unit: px. Value range: An integer greater than 0. The width value must be greater than 0. |
| height | number | Yes | Indicates the height of the canvas object. Unit: px. Value range: An integer greater than 0. The height value must be greater than 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Canvas | Returns the canvas that records the drawing commands. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) | Parameter error. Possible causes: Incorrect parameter range. |

## finishRecording

```TypeScript
finishRecording(): RecordCmd
```

Finishes recording and returns the recorded command object.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [RecordCmd](arkts-arkgraphics2d-drawing-recordcmd-i.md) | Returns the recorded drawing commands. |

## getHeight

```TypeScript
getHeight(): number
```

Gets the height of the recording canvas.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the height of recording canvas. |

**Examples**

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let height = canvas.getHeight();
    console.info('get canvas height:' + height);
  }
}
```

## getWidth

```TypeScript
getWidth(): number
```

Gets the width of the recording canvas.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the width of recording canvas. |

**Examples**

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let width = canvas.getWidth();
    console.info('get canvas width:' + width);
  }
}
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
let width = pen.getWidth();
```
