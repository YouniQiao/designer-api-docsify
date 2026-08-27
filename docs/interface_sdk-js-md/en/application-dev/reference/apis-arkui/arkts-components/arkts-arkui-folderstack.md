# FolderStack

**FolderStack** extends the [Stack](../../apis-default/arkts-apis/arkts-lib-es5-error-i.md#stack) container, adding the <!--RP1-->foldable phone hover<!--RP1End--> capability. Child components specified in the **upperItems** array of [FolderStackOptions](arkts-arkui-folderstackoptions-i.md) automatically avoid the screen crease area and reposition to the upper display. > **NOTE** > > The hover capability is designed for and only works on <!--RP2-->dual-fold devices<!--RP2End-->. > > When the component's parent is an > [if/else conditional render](../../../ui/rendering-control/arkts-rendering-control-ifelse.md) node, the foldable > hover feature is disabled. > > **Child Components** > > Multiple child components are supported.

## FolderStack

```TypeScript
FolderStack(options?: FolderStackOptions)
```

Defines the constructor of FolderStack component.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FolderStackOptions](arkts-arkui-folderstackoptions-i.md) | No | Configuration of the **FolderStack** component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [FolderStackOptions](arkts-arkui-folderstackoptions-i.md) | > **NOTE：**
> 
> To standardize anonymous object definitions, the element definitions here have been revised in API version 18.
> While historical version information is preserved for anonymous objects, there may be cases where the outer
> element's |
| [HoverEventParam](arkts-arkui-hovereventparam-i.md) | The param of hover event. |
| [OnFoldStatusChangeInfo](arkts-arkui-onfoldstatuschangeinfo-i.md) | Called when the folding state changes. This API takes effect only in landscape mode. |

### Types

| Name | Description |
| --- | --- |
| [OnFoldStatusChangeCallback](arkts-arkui-onfoldstatuschangecallback-t.md) | Current fold state of the device. |
| [OnHoverStatusChangeCallback](arkts-arkui-onhoverstatuschangecallback-t.md) | Defines the current callback invoked when the hover state of the device changes. |
| [WindowStatusType](arkts-arkui-windowstatustype-t.md) | Enumerates the window modes. |

## Examples

This example implements the foldable device hover capability.

```TypeScript
@Entry
@Component
struct Index {
  build() {
    Column() {
      // Set upperItems to IDs of the child components to be moved to the upper half screen in the hover state. Other components are stacked in the lower half screen.
      FolderStack({ upperItems: ['upperitemsId'] }) {
        // This column is automatically moved up to the upper half screen.
        Column() {
          Text('video zone').height('100%').width('100%').textAlign(TextAlign.Center).fontSize(25)
        }.backgroundColor('rgb(0, 74, 175)').width('100%').height('100%').id('upperitemsId')

        // The following two columns are stacked in the lower half screen.
        Column() {
          Text('video title')
            .width('100%')
            .height(50)
            .textAlign(TextAlign.Center)
            .backgroundColor('rgb(213, 213, 213)')
            .fontSize(25)
        }.width('100%').height('100%').justifyContent(FlexAlign.Start)

        Column() {
          Text('video bar ')
            .width('100%')
            .height(50)
            .textAlign(TextAlign.Center)
            .backgroundColor('rgb(213, 213, 213)')
            .fontSize(25)
        }.width('100%').height('100%').justifyContent(FlexAlign.End)
      }
      .backgroundColor('rgb(39, 135, 217)')
      // Set whether to enable animation.
      .enableAnimation(true)
      // Set whether to enable auto-rotate.
      .autoHalfFold(true)
      // Called when the folding status changes.
      .onFolderStateChange((msg) => {
        if (msg.foldStatus === FoldStatus.FOLD_STATUS_EXPANDED) {
          console.info('The device is currently in the expanded state')
        } else if (msg.foldStatus === FoldStatus.FOLD_STATUS_HALF_FOLDED) {
          console.info('The device is currently in the half folded state')
        } else {
          // ...
        }
      })
      // The hoverStatusChange callback is invoked when the hover status changes.
      .onHoverStatusChange((msg) => {
        console.info('this foldStatus:' + msg.foldStatus);
        console.info('this isHoverMode:' + msg.isHoverMode);
        console.info('this appRotation:' + msg.appRotation);
        console.info('this windowStatusType:' + msg.windowStatusType);
      })
      // If the folderStack component does not occupy the full screen, it is used as a common stack.
      .alignContent(Alignment.Bottom)
      .height('100%')
      .width('100%')

    }
    .height('100%')
    .width('100%')
    .borderWidth(1)
    .borderColor('rgb(213, 213, 213)')
    .backgroundColor('rgb(0, 74, 175)')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
  }
}
```

This example demonstrates how to dynamically set the onFolderStateChange and onHoverStatusChange methods of the FolderStack component using attributeModifier.

```TypeScript
// xxx.ets
class MyFolderStackModifier implements AttributeModifier<FolderStackAttribute> {
  applyNormalAttribute(instance: FolderStackAttribute): void {
    // Called when the folding status changes.
    instance.onFolderStateChange((msg) => {
      if (msg.foldStatus === FoldStatus.FOLD_STATUS_EXPANDED) {
        console.info('The device is currently in the expanded state')
      } else if (msg.foldStatus === FoldStatus.FOLD_STATUS_HALF_FOLDED) {
        console.info('The device is currently in the half folded state')
      } else if (msg.foldStatus === FoldStatus.FOLD_STATUS_FOLDED) {
        console.info('The device is currently in the folded state')
      } else {
        // ...
      }
    })
    // The hoverStatusChange callback is invoked when the hover status changes.
    instance.onHoverStatusChange((msg) => {
      console.info('this foldStatus:' + msg.foldStatus);
      console.info('this isHoverMode:' + msg.isHoverMode);
      console.info('this appRotation:' + msg.appRotation);
      console.info('this windowStatusType:' + msg.windowStatusType);
    })
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyFolderStackModifier = new MyFolderStackModifier()

  build() {
    Column() {
      // Set upperItems to IDs of the child components to be moved to the upper half screen in the hover state. Other components are stacked in the lower half screen.
      FolderStack({ upperItems: ['upperitemsId'] }) {
        // This column is automatically moved up to the upper half screen.
        Column() {
          Text('video zone').height('100%').width('100%').textAlign(TextAlign.Center).fontSize(25)
        }.backgroundColor('rgb(0, 74, 175)').width('100%').height('100%').id('upperitemsId')

        // The following two columns are stacked in the lower half screen.
        Column() {
          Text('video title')
            .width('100%')
            .height(50)
            .textAlign(TextAlign.Center)
            .backgroundColor('rgb(213, 213, 213)')
            .fontSize(25)
        }.width('100%').height('100%').justifyContent(FlexAlign.Start)

        Column() {
          Text('video bar ')
            .width('100%')
            .height(50)
            .textAlign(TextAlign.Center)
            .backgroundColor('rgb(213, 213, 213)')
            .fontSize(25)
        }.width('100%').height('100%').justifyContent(FlexAlign.End)
      }
      .backgroundColor('rgb(39, 135, 217)')
      // Set whether to enable animation.
      .enableAnimation(true)
      // Set whether to enable auto-rotate.
      .autoHalfFold(true)
      .attributeModifier(this.modifier)
      // If the <folderStack> component does not occupy the full screen, it is used as a common stack.
      .alignContent(Alignment.Bottom)
      .height('100%')
      .width('100%')
    }
    .height('100%')
    .width('100%')
    .borderWidth(1)
    .borderColor('rgb(213, 213, 213)')
    .backgroundColor('rgb(0, 74, 175)')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
  }
}
```
