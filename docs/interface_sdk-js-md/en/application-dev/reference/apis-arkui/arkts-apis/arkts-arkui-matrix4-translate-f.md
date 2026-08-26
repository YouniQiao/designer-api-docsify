# translate

## Modules to Import

```TypeScript
import matrix4 from '@kit.ArkUI';
```

## translate

```TypeScript
function translate(options: TranslateOption): Matrix4Transit
```

Translates this matrix object along the x, y, and z axes.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [translate](arkts-arkui-matrix4-matrix4transit-i.md#translate)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TranslateOption](arkts-arkui-matrix4-translateoption-i.md) | Yes | Translation configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) | Matrix object after translation. |

**Examples**

```TypeScript
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().translate({ x: 100, y: 200, z: 30 });

  build() {
    Column() {
      // Replace $r("app.media.bg1") with the image resource file you use.
      Image($r("app.media.bg1")).transform(this.matrix1)
        .width('40%')
        .height(100)
    }
  }
}
```
