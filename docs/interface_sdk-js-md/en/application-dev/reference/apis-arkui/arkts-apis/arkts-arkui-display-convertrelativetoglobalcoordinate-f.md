# convertRelativeToGlobalCoordinate

## Modules to Import

```TypeScript
import { display } from 'display';
```

## convertRelativeToGlobalCoordinate

```TypeScript
function convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position
```

Converts relative coordinates (based on the top-left corner of the screen) into global coordinates (based on the top-left corner of the primary screen). This API supports only coordinate conversion between the primary screen and extended screen.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-display-function convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position--><!--Device-display-function convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| relativePosition | [RelativePosition](arkts-arkui-display-relativeposition-i.md) | Yes | Relative coordinates to convert. |

**Return value:**

| Type | Description |
| --- | --- |
| Position | Global coordinates based on the top-left corner of the primary screen. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400004](../errorcode-display.md#1400004-parameter-error) | Parameter error. Possible cause: 1. Invalid parameter range. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

## Examples

```TypeScript
import { display } from '@kit.ArkUI';

let relativePosition: display.RelativePosition = {
  displayId: 0,
  position: {
    x: 100,
    y: 200
  }
};

try {
  let position: display.Position = display.convertRelativeToGlobalCoordinate(relativePosition);
  console.info(`The global coordinate is ${position.x}, ${position.y}`)
} catch (exception) {
  console.error(`Failed to convert the relative coordinate to the global coordinate. Code: ${exception.code}, message: ${exception.message}`);
}
```

