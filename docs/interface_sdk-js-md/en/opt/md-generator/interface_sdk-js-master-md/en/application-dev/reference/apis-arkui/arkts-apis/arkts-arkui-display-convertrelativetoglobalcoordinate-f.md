# convertRelativeToGlobalCoordinate

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## convertRelativeToGlobalCoordinate

```TypeScript
function convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position
```

Converts relative coordinates (based on the top-left corner of the screen) into global coordinates (based on the top-left corner of the primary screen). This API supports only coordinate conversion between the primary screen and extended screen.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-display-function convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position--><!--Device-display-function convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| relativePosition | [RelativePosition](arkts-arkui-display-relativeposition-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-display-position-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1400004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400004-parameter-error) |
| [1400003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400003-abnormal-display-manager-service) |

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
