# removeVirtualScreenSurface (System API)

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## removeVirtualScreenSurface

```TypeScript
function removeVirtualScreenSurface(screenId: number, surfaceId: string): Promise<void>
```

Remove surface for the virtual screen.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-display-function removeVirtualScreenSurface(screenId: long, surfaceId: string): Promise<void>--><!--Device-display-function removeVirtualScreenSurface(screenId: long, surfaceId: string): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| screenId | number | Yes |
| surfaceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1400004](../errorcode-display.md#1400004-parameter-error) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
// Index.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  xComponentController: XComponentController = new XComponentController();

  removeVirtualScreenSurface = () => {
    let screenId: number = 1;
    let surfaceId = this.xComponentController.getXComponentSurfaceId();
    display.removeVirtualScreenSurface(screenId, surfaceId).then(() => {
      console.info('Succeeded in removing surface for the virtual screen.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to remove surface for the virtual screen. Code:${err.code}, message is ${err.message}`);
    });
  }
  build() {
    RelativeContainer() {
      XComponent({
        type: XComponentType.SURFACE,
        controller: this.xComponentController
      })
      Button('removeSurface')
        .onClick((event: ClickEvent) => {
          this.removeVirtualScreenSurface();
      }).width('100%')
      .height(20)
    }
    .width('100%')
    .height('100%')
  }
}
```
