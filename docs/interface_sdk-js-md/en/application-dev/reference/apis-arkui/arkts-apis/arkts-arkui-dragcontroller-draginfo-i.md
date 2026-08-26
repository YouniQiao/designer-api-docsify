# DragInfo

Defines the attributes required for initiating a drag action and information carried in the dragging process.

**Since:** 10

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import dragController from '@kit.ArkUI';
```

## autoHideComponentUniqueIds

```TypeScript
autoHideComponentUniqueIds?: number | number[]
```

Unique ID of the component that is automatically hidden by the system during proactive dragging. A single unique ID or an array of unique IDs can be passed.After the proactive dragging is successfully initiated, the system automatically hides the target component before displaying the drag preview window.If the proactive dragging source also needs to be hidden, its unique ID must be passed as well.The unique ID of a component can be obtained by using [UIContext.getFrameNodeById()](arkts-arkui-arkui-uicontext-uicontext-c.md#getframenodebyid) together with [FrameNode.getUniqueId()](arkts-arkui-framenode-c.md#getuniqueid).You need to restore the component display status as required in the drag end callback.

**Type:** number \| number[]

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## data

```TypeScript
data?: unifiedDataChannel.UnifiedData
```

Data carried in the dragging process.The default value is null.

**Type:** unifiedDataChannel.UnifiedData

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dataLoadParams

```TypeScript
dataLoadParams?: unifiedDataChannel.DataLoadParams
```

Parameters for deferred data loading from the drag source. This API provides data loading parameters to the system instead of directly providing complete data objects. When the user drops data on the target application, the system will use these parameters to request the actual data from the drag source. If set together with **data**, **dataLoadParams** takes effect.The default value is null.

**Type:** unifiedDataChannel.DataLoadParams

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## extraParams

```TypeScript
extraParams?: string
```

Additional information about the drag action. Not supported currently.The default value is null.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pointerId

```TypeScript
pointerId: number
```

ID of the touch point on the screen when dragging is started. The value is an integer in the [0, 9] range.

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## previewOptions

```TypeScript
previewOptions?: DragPreviewOptions
```

Processing mode of the drag preview and the display of the number badge during dragging.

**Type:** [DragPreviewOptions](../arkts-components/arkts-arkui-dragpreviewoptions-i.md)

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## touchPoint

```TypeScript
touchPoint?: TouchPoint
```

Coordinates of the touch point. If this parameter is not set, the touch point is centered horizontally and shifted downward by 20% from the top.

**Type:** TouchPoint

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

The autoHideComponentUniqueIds attribute is added for DragInfo since API version 26.0.0.

```TypeScript
import { dragController } from '@kit.ArkUI';
import { unifiedDataChannel } from '@kit.ArkData';

@Entry
@Component
struct DragInfoAutoHideSample {
  @State sourceVisibility: Visibility = Visibility.Visible;
  @State badgeVisibility: Visibility = Visibility.Visible;
  @State statusText: string = 'Status: waiting for proactive dragging'

  @Builder
  PreviewBuilder() {
    Text('Drag Preview')
      .width(140)
      .height(60)
      .backgroundColor('#3F51B5')
      .borderRadius(10)
      .fontColor(Color.White);
  }

  private buildData(content: string): unifiedDataChannel.UnifiedData {
    let plainText = new unifiedDataChannel.PlainText();
    plainText.textContent = content;
    plainText.abstract = content;
    return new unifiedDataChannel.UnifiedData(plainText);
  }

  private collectHideIds(): number[] {
    let hideIds: number[] = [];
    let sourceNode = this.getUIContext().getFrameNodeById('active_source');
    let badgeNode = this.getUIContext().getFrameNodeById('active_badge');
    if (sourceNode?.getUniqueId() !== undefined) {
      hideIds.push(sourceNode.getUniqueId());
    }
    if (badgeNode?.getUniqueId() !== undefined) {
      hideIds.push(badgeNode.getUniqueId());
    }
    return hideIds;
  }

  private hideTargets(): void {
    this.sourceVisibility = Visibility.Hidden;
    this.badgeVisibility = Visibility.Hidden;
    this.statusText = 'Status: Proactively dragging. The target component has been hidden.';
  }

  private restoreTargets(): void {
    this.sourceVisibility = Visibility.Visible;
    this.badgeVisibility = Visibility.Visible;
    this.statusText = 'Status: Dragging ended. The component has been displayed.';
  }

  build() {
    Column({ space: 12 }) {
      Text(this.statusText)
        .width('100%')
        .fontSize(14)
        .fontColor('#BF360C');

      Row({ space: 12 }) {
        Column() {
          Text('Proactive dragging source')
            .fontColor(Color.White)
            .fontWeight(FontWeight.Medium);
          Text('id: active_source')
            .fontSize(10)
            .fontColor('#E8F5E9');
        }
          .id('active_source')
          .width(140)
          .height(90)
          .backgroundColor('#2E7D32')
          .borderRadius(12)
          .justifyContent(FlexAlign.Center)
          .visibility(this.sourceVisibility);

        Column() {
          Text('Follow the hidden component')
            .fontColor(Color.White)
            .fontWeight(FontWeight.Medium);
          Text('id: active_badge')
            .fontSize(10)
            .fontColor('#E3F2FD');
        }
          .id('active_badge')
          .width(140)
          .height(90)
          .backgroundColor('#1565C0')
          .borderRadius(12)
          .justifyContent(FlexAlign.Center)
          .visibility(this.badgeVisibility);
      }

      Button ('Initiate Drag')
        .width('100%')
        .height(56)
        .backgroundColor('#FF8F00')
        .onTouch((touchEvent) => {
          if (!touchEvent || touchEvent.type !== TouchType.Down) {
            return;
          }
          let hideIds = this.collectHideIds();
          let dragInfo: dragController.DragInfo = {
            pointerId: 0,
            data: this.buildData('active drag data'),
            extraParams: '',
            autoHideComponentUniqueIds: hideIds
          };
          this.hideTargets();
          this.getUIContext().getDragController().executeDrag(() => {
            this.PreviewBuilder();
          }, dragInfo, () => {
            this.restoreTargets();
          });
        })
    }
    .width('100%')
    .padding(16)
  }
}
```
