# init

## Modules to Import

```TypeScript
```

## init

```TypeScript
function init(
    options: [
      number,
      number,
      number,
      number,
      number,
      number,
      number,
      number,
      number,
      number,
      number,
      number,
      number,
      number,
      number,
      number
    ]
  ): Matrix4Transit
```

Matrix constructor, which is used to create a 4 x 4 matrix with the input parameters. Column-major order is used.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-matrix4-function init(    options: [      number,      number,      number,      number,      number,      number,      number,      number,      number,      number,      number,      number,      number,      number,      number,      number    ]  ): Matrix4Transit--><!--Device-matrix4-function init(    options: [      number,      number,      number,      number,      number,      number,      number,      number,      number,      number,      number,      number,      number,      number,      number,      number    ]  ): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [       number,       number,       number,       number,       number,       number,       number,       number,       number,       number,       number,       number,       number,       number,       number,       number     ] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Matrix4Transit](../../apis-na/arkts-apis/arkts-na-matrix4-matrix4transit-i.md) |

**Examples**

```TypeScript
import { matrix4 } from '@kit.ArkUI';

// Create a 4 x 4 matrix.
let matrix = matrix4.init(
  [1.0, 0.0, 0.0, 0.0,
    0.0, 1.0, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0,
    0.0, 0.0, 0.0, 1.0]);

@Entry
@Component
struct Tests {
  build() {
    Column() {
      // Replace $r("app.media.zh") with the image resource file you use.
      Image($r("app.media.zh"))
        .width('40%')
        .height(100)
        .transform(matrix)
    }
  }
}
```
