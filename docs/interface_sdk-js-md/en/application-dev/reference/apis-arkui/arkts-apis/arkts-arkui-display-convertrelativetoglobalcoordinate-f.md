# convertRelativeToGlobalCoordinate

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## convertRelativeToGlobalCoordinate

```TypeScript
function convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position
```

将指定屏幕左上角为原点的相对坐标转换成主屏左上角为原点的全局坐标，仅支持主屏和扩展屏的坐标转换。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-display-function convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position--><!--Device-display-function convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| relativePosition | [RelativePosition](arkts-arkui-display-relativeposition-i.md) | Yes | 需要转化为全局坐标的相对坐标。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Position](arkts-arkui-display-position-i.md) | 返回相对于主屏左上角的全局坐标。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1400004 | Parameter error. Possible cause: 1. Invalid parameter range. |
| 1400003 | This display manager service works abnormally. |

## Examples

```TypeScript
// Define the relative coordinates to convert.
let relativePosition: display.RelativePosition = {
  displayId: 0,
  position: {
    x: 100,
    y: 200
  }
};

try {
   // Convert the relative coordinates to global coordinates.
  let position: display.Position = display.convertRelativeToGlobalCoordinate(relativePosition);
  console.info(`The global coordinate is ${position.x}, ${position.y}`)
} catch (exception) {
  console.error(`Failed to convert the relative coordinate to the global coordinate. Code: ${exception.code}, message: ${exception.message}`);
}
```

