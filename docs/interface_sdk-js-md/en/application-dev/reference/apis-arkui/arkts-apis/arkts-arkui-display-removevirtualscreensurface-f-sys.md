# removeVirtualScreenSurface (System API)

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## removeVirtualScreenSurface

```TypeScript
function removeVirtualScreenSurface(screenId: long, surfaceId: string): Promise<void>
```

删除虚拟屏的surface。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-display-function removeVirtualScreenSurface(screenId: long, surfaceId: string): Promise<void>--><!--Device-display-function removeVirtualScreenSurface(screenId: long, surfaceId: string): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| screenId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 虚拟屏幕的屏幕ID。 |
| surfaceId | string | Yes | 代表虚拟屏幕绑定的surfaceId，由用户指定某一实际存在的surface对应的surfaceId， 该参数最大长度为4096个字节，超出最大长度时则取前4096个字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Function removeVirtualScreenSurface can not work correctly due to limited device capabilities. |
| 1400004 | Parameter error. Possible cause: 1. Invalid parameter range. |
| 1400001 | Invalid display or screen. |
| 1400003 | This display manager service works abnormally. |
| 202 | Permission verification failed. A non-system application calls a system API. |

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

