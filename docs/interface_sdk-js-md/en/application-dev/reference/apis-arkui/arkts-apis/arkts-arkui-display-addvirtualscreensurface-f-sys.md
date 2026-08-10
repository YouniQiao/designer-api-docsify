# addVirtualScreenSurface (System API)

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## addVirtualScreenSurface

```TypeScript
function addVirtualScreenSurface(screenId: long, surfaceId: string, surfaceRegion?: Rect): Promise<void>
```

为虚拟屏幕添加surface。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-display-function addVirtualScreenSurface(screenId: long, surfaceId: string, surfaceRegion?: Rect): Promise<void>--><!--Device-display-function addVirtualScreenSurface(screenId: long, surfaceId: string, surfaceRegion?: Rect): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| screenId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 虚拟屏幕的屏幕ID。 |
| surfaceId | string | Yes | 代表虚拟屏幕绑定的surfaceId，由用户指定某一实际存在的surface对应的surfaceId， 该参数最大长度为4096个字节，超出最大长度时则取前4096个字节。 |
| surfaceRegion | [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md) | No | surface显示的虚拟屏的矩形区域。 如果虚拟屏幕未通过[setVirtualScreenSurface()](arkts-arkui-display-setvirtualscreensurface-f.md#setvirtualscreensurface) 或 [addVirtualScreenSurface()](arkts-arkui-display-addvirtualscreensurface-f-sys.md#addvirtualscreensurface)绑定过surface，surfaceRegion无效，默认全屏。 在镜像模式下，surfaceRegion无效，默认全屏。在异源模式下，surfaceRegion有效。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Function addVirtualScreenSurface can not work correctly due to limited device capabilities. |
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

  addVirtualScreenSurface = () => {
    let screenId: number = 1;
    let surfaceId = this.xComponentController.getXComponentSurfaceId();
    display.addVirtualScreenSurface(screenId, surfaceId).then(() => {
      console.info('Succeeded in adding surface for the virtual screen.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to add surface for the virtual screen. Code:${err.code}, message is ${err.message}`);
    });
  }
  build() {
    RelativeContainer() {
      XComponent({
        type: XComponentType.SURFACE,
        controller: this.xComponentController
      })
      Button('addSurface')
        .onClick((event: ClickEvent) => {
          this.addVirtualScreenSurface();
      }).width('100%')
      .height(20)
    }
    .width('100%')
    .height('100%')
  }
}
```

