# createDragAction

## Modules to Import

```TypeScript
import { dragController } from '@kit.ArkUI';
```

## createDragAction

```TypeScript
function createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: DragInfo): DragAction
```

Initiates a drag action, with the object to be dragged and the drag information passed in. This API uses a promise to return the result.

> **NOTE：**
> 
> - Since API version 11, you can use the
> [getDragController](arkts-arkui-arkui-uicontext-uicontext-c.md#getDragController) API in
> [UIContext](@ohos.arkui.UIContext) to obtain the
> [DragController](arkts-arkui-arkui-uicontext-dragcontroller-c.md#DragController) object associated with the current UI context.
> 
> - For optimal drag and drop performance, limit the number of drag previews.

**Since:** 11

**Deprecated since:** 18

**Substitutes:** [createDragAction](ohos.arkui.UIContext.DragController#createDragAction)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-dragController-function createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: DragInfo): DragAction--><!--Device-dragController-function createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: DragInfo): DragAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| customArray | Array&lt;[CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| [DragItemInfo](../arkts-components/arkts-arkui-dragiteminfo-i.md)&gt; | Yes |
| dragInfo | [DragInfo](arkts-arkui-dragcontroller-draginfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DragAction](arkts-arkui-dragcontroller-dragaction-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-internal.md#100001-internal-error) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

You are advised to use [getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11) in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the DragController object associated with the current UI context.

```TypeScript
import { dragController } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';
import { unifiedDataChannel } from '@kit.ArkData';

@Entry
@Component
struct DragControllerPage {
  @State pixmap: image.PixelMap | null = null
  @State text: string = ''
  private dragAction: dragController.DragAction | null = null;
  customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();

  @Builder
  DraggingBuilder() {
    Column() {
      Text("DraggingBuilder")
        .fontColor(Color.White)
        .fontSize(12)
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {

      Column() {
        Text(this.text)
          .width('100%')
          .height('100%')
          .fontColor(Color.White)
          .fontSize(18)
          .onDrop((dragEvent?: DragEvent) => {
            if (dragEvent) {
              let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
              let plainText: unifiedDataChannel.PlainText = records[0] as unifiedDataChannel.PlainText;
              this.text = plainText.textContent;
            }
          })
      }
      .width(100)
      .height(100)
      .backgroundColor(Color.Red)
      .margin(10)

      Button('Drag Multiple Objects').onTouch((event?: TouchEvent) => {
        if (event) {
          if (event.type == TouchType.Down) {
            console.info("multi drag Down by listener");
            this.customBuilders.splice(0, this.customBuilders.length);
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            this.customBuilders.push(() => {
              this.DraggingBuilder()
            });
            let text = new unifiedDataChannel.PlainText()
            text.textContent = 'drag text'
            let unifiedData = new unifiedDataChannel.UnifiedData(text)
            let dragInfo: dragController.DragInfo = {
              pointerId: 0,
              data: unifiedData,
              extraParams: ''
            }
            try {
              this.dragAction = this.getUIContext()
                .getDragController()
                .createDragAction(this.customBuilders,
                  dragInfo) // You are advised to use this.getUIContext().getDragController().createDragAction().
              if (!this.dragAction) {
                console.info("listener dragAction is null");
                return
              }
              this.dragAction.on('statusChange', (dragAndDropInfo: dragController.DragAndDropInfo) => {
                if (dragAndDropInfo.status == dragController.DragStatus.STARTED) {
                  console.info("drag has start");
                } else if (dragAndDropInfo.status == dragController.DragStatus.ENDED) {
                  console.info("drag has end");
                  if (!this.dragAction) {
                    return
                  }
                  this.dragAction.off('statusChange')
                }
              })
              this.dragAction.startDrag().then(() => {
              }).catch((err: Error) => {
                console.error(`Failed to start drag. Code: ${err.code}, message: ${err.message}`);
              })
            } catch (err) {
              console.error(`Failed to create dragAction. Code: ${err.code}, message: ${err.message}`);
            }
          }
        }
      }).margin({ top: 20 })
    }
  }
}
```
