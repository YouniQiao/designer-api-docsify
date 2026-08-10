# convertGlobalToRelativeCoordinate

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## convertGlobalToRelativeCoordinate

```TypeScript
function convertGlobalToRelativeCoordinate(position: Position, displayId?: long): RelativePosition
```

将主屏左上角为原点的全局坐标转换成displayId指定屏幕左上角为原点的相对坐标。若未传入displayId，默认转换为全局坐标所在屏幕的相对坐标系。若全局坐标不在任何屏幕上，默认转换成主屏的相对坐标。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-display-function convertGlobalToRelativeCoordinate(position: Position, displayId?: long): RelativePosition--><!--Device-display-function convertGlobalToRelativeCoordinate(position: Position, displayId?: long): RelativePosition-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | [Position](arkts-arkui-display-position-i.md) | Yes | 需要转化为相对坐标的全局坐标。 |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | No | 相对坐标系原点所在的屏幕ID，传递该参数表示以指定屏幕左上角为原点转换相对坐标。不指定则不传参，默认转换成全局坐标所在屏幕的相对坐标，若全局坐标不在任何屏幕上，则默认转换 成主屏的相对坐标。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RelativePosition](arkts-arkui-display-relativeposition-i.md) | 返回对应屏幕的相对坐标。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1400004 | Parameter error. Possible cause: 1. Invalid parameter range. |
| 1400003 | This display manager service works abnormally. |

## Examples

```TypeScript
// Define the global coordinates to convert.
let position: display.Position = {
    x: 100,
    y: 200
};

try {
  // Convert the global coordinates to relative coordinates.
  let relPos: display.RelativePosition = display.convertGlobalToRelativeCoordinate(position, 0);
  console.info(`The relative coordinate is ${relPos.displayId}, ${relPos.position.x}, ${relPos.position.y}`)
} catch (exception) {
  console.error(`Failed to convert the global coordinate to the relative coordinate. Code: ${exception.code}, message: ${exception.message}`);
}
```

