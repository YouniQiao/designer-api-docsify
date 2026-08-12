# init

## Modules to Import

```TypeScript
import { matrix4 } from '@kit.ArkUI';
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
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) |
