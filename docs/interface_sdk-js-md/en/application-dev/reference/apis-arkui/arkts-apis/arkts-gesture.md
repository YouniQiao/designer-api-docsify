# gesture

Enumerates gesture competition results.

## Modules to Import

```TypeScript
```

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [GestureControl](arkts-arkui-gesturecontrol-n.md) | Enumerates gesture competition results. |

### Classes

| Name | Description |
| --- | --- |
| [EventTargetInfo](arkts-arkui-eventtargetinfo-c.md) | Provides the information about the component corresponding to the gesture recognizer. |
| [GestureGroupHandler](arkts-arkui-gesturegrouphandler-c.md) | Defines a gesture group handler object. |
| [GestureHandler](arkts-arkui-gesturehandler-c.md) | Represents the base type for gesture handlers. |
| [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md) | Gesture recognizer object. |
| [LongPressGestureHandler](arkts-arkui-longpressgesturehandler-c.md) | Defines a number press gesture handler object. |
| [LongPressRecognizer](arkts-arkui-longpressrecognizer-c.md) | Implements a number press gesture recognizer. Inherits from [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md). |
| [PanGestureHandler](arkts-arkui-pangesturehandler-c.md) | Defines a pan gesture handler object. |
| [PanGestureOptions](arkts-arkui-pangestureoptions-c.md) | Defines the PanGesture options. |
| [PanRecognizer](arkts-arkui-panrecognizer-c.md) | Gesture recognizer object. |
| [PinchGestureHandler](arkts-arkui-pinchgesturehandler-c.md) | Defines a type of gesture handler object for pinch gestures. |
| [PinchRecognizer](arkts-arkui-pinchrecognizer-c.md) | Implements a pinch gesture recognizer. Inherits from [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md). |
| [RotationGestureHandler](arkts-arkui-rotationgesturehandler-c.md) | Defines a rotation gesture handler object. |
| [RotationRecognizer](arkts-arkui-rotationrecognizer-c.md) | Implements a rotation gesture recognizer. Inherits from [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md). |
| [ScrollableTargetInfo](arkts-arkui-scrollabletargetinfo-c.md) | Provides the information about the scrollable container component corresponding to the gesture recognizer. It inherits from [EventTargetInfo](arkts-arkui-eventtargetinfo-c.md). |
| [SwipeGestureHandler](arkts-arkui-swipegesturehandler-c.md) | Defines a swipe gesture handler object. |
| [SwipeRecognizer](arkts-arkui-swiperecognizer-c.md) | Implements a swipe gesture recognizer. Inherits from [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md). |
| [TapGestureHandler](arkts-arkui-tapgesturehandler-c.md) | Defines a type of gesture handler object for tap gestures. |
| [TapRecognizer](arkts-arkui-taprecognizer-c.md) | Implements a tap gesture recognizer object. Inherits from [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md). |
| [TouchRecognizer](arkts-arkui-touchrecognizer-c.md) | Represents a touch gesture recognizer. |

### Interfaces

| Name | Description |
| --- | --- |
| [BaseGestureEvent](arkts-arkui-basegestureevent-i.md) | Defines the basic gesture event type. Inherits from [BaseEvent](../arkts-components/arkts-arkui-baseevent-i.md). |
| [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md) | Provides the parameters of the basic gesture handler. |
| [EventLocationInfo](arkts-arkui-eventlocationinfo-i.md) | Provides coordinate information for tap gestures. |
| [FingerInfo](arkts-arkui-fingerinfo-i.md) | Defines the finger information type. |
| [GestureEvent](arkts-arkui-gestureevent-i.md) | Defines the gesture event information. Inherits from [BaseEvent](../arkts-components/arkts-arkui-baseevent-i.md). |
| [GestureGroupGestureHandlerOptions](arkts-arkui-gesturegroupgesturehandleroptions-i.md) | Provides the parameters of the gesture group handler. |
| [GestureGroupInterface](arkts-arkui-gesturegroupinterface-i.md) | Combined gestures integrate two or more gestures into a compound gesture, supporting sequential recognition, parallel recognition, and exclusive recognition. |
| [GestureInfo](arkts-arkui-gestureinfo-i.md) | Defines the gesture information type. |
| [GestureInterface](arkts-arkui-gestureinterface-i.md) | Defines the gesture API. |
| [LongPressGestureEvent](arkts-arkui-longpressgestureevent-i.md) | Inherits from [BaseGestureEvent](arkts-arkui-basegestureevent-i.md). This object can be passed as the **event** parameter of [onGestureJudgeBegin](../arkts-components/arkts-arkui-commonmethod-c.md#ongesturejudgebegin). |
| [LongPressGestureHandlerOptions](arkts-arkui-longpressgesturehandleroptions-i.md) | Provides the parameters of the number press gesture handler. Inherits from [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md). |
| [LongPressGestureInterface](arkts-arkui-longpressgestureinterface-i.md) | **LongPressGesture** is used to trigger a number press gesture. This gesture requires one or more fingers to be held down for a specified duration, which is 500 ms by default and can be adjusted using the **duration** parameter. |
| [PanGestureEvent](arkts-arkui-pangestureevent-i.md) | Inherits from [BaseGestureEvent](arkts-arkui-basegestureevent-i.md). This object can be passed as the **event** parameter of [onGestureJudgeBegin](../arkts-components/arkts-arkui-commonmethod-c.md#ongesturejudgebegin). |
| [PanGestureHandlerOptions](arkts-arkui-pangesturehandleroptions-i.md) | Provides the parameters of the pan gesture handler. Inherits from [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md). |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) | PanGesture is used to trigger a pan gesture when the movement distance of a finger on the screen reaches the minimum value. |
| [PinchGestureEvent](arkts-arkui-pinchgestureevent-i.md) | Inherits from [BaseGestureEvent](arkts-arkui-basegestureevent-i.md). This object can be passed as the **event** parameter of [onGestureJudgeBegin](../arkts-components/arkts-arkui-commonmethod-c.md#ongesturejudgebegin). |
| [PinchGestureHandlerOptions](arkts-arkui-pinchgesturehandleroptions-i.md) | Provides the parameters of the pinch gesture handler. Inherits from [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md). |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) | **PinchGesture** is used to trigger a pinch gesture, which requires two to five fingers with a minimum 5 vp distance between the fingers. |
| [RotationGestureEvent](arkts-arkui-rotationgestureevent-i.md) | Inherits from [BaseGestureEvent](arkts-arkui-basegestureevent-i.md). This object can be passed as the **event** parameter of [onGestureJudgeBegin](../arkts-components/arkts-arkui-commonmethod-c.md#ongesturejudgebegin). |
| [RotationGestureHandlerOptions](arkts-arkui-rotationgesturehandleroptions-i.md) | Provides the parameters of the rotation gesture handler. Inherits from [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md). |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) | **RotationGesture** is used to trigger a rotation gesture, which recognizes rotational movements using two to five fingers, with a minimum angular change of 1 degree. This gesture cannot be triggered using a two-finger rotation operation on a trackpad. |
| [SwipeGestureEvent](arkts-arkui-swipegestureevent-i.md) | Inherits from [BaseGestureEvent](arkts-arkui-basegestureevent-i.md). This object can be passed as the **event** parameter of [onGestureJudgeBegin](../arkts-components/arkts-arkui-commonmethod-c.md#ongesturejudgebegin). |
| [SwipeGestureHandlerOptions](arkts-arkui-swipegesturehandleroptions-i.md) | Provides the parameters of the swipe gesture handler. Inherits from [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md). |
| [SwipeGestureInterface](arkts-arkui-swipegestureinterface-i.md) | **SwipeGesture** is used to trigger a swipe gesture. This gesture is successfully recognized when the swipe speed exceeds the specified threshold, which is 100 vp/s by default. |
| [TapGestureEvent](arkts-arkui-tapgestureevent-i.md) | Inherits from [BaseGestureEvent](arkts-arkui-basegestureevent-i.md). This object can be passed as the **event** parameter of [onGestureJudgeBegin](../arkts-components/arkts-arkui-commonmethod-c.md#ongesturejudgebegin). |
| [TapGestureHandlerOptions](arkts-arkui-tapgesturehandleroptions-i.md) | Provides the parameters of the tap gesture handler. Inherits from [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md). |
| [TapGestureInterface](arkts-arkui-tapgestureinterface-i.md) | TapGesture is used to trigger a tap gesture with one, two, or more taps. |
| [TapGestureParameters](arkts-arkui-tapgestureparameters-i.md) | Defines tap gesture parameters. Inherits from [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md). |

### Enums

| Name | Description |
| --- | --- |
| [GestureJudgeResult](arkts-arkui-gesturejudgeresult-e.md) | Enumerates gesture competition results. |
| [GestureMask](arkts-arkui-gesturemask-e.md) | Enumerates masking modes of child component gestures. |
| [GestureMode](arkts-arkui-gesturemode-e.md) | Defines the recognition mode of a gesture group. |
| [GesturePriority](arkts-arkui-gesturepriority-e.md) | Enumerates gesture priority levels. |
| [GestureRecognizerState](arkts-arkui-gesturerecognizerstate-e.md) | Enumerates the gesture recognizer states. |
| [PanDirection](arkts-arkui-pandirection-e.md) | Enumerates the pan directions. Unlike **SwipeDirection**, **PanDirection** has no angular restrictions. |
| [SwipeDirection](arkts-arkui-swipedirection-e.md) | Enumerates the directions in which the swipe gesture can be recognized. |

### Types

| Name | Description |
| --- | --- |
| [GestureType](arkts-arkui-gesturetype-t.md) | Defines the Gesture Type. |

### Constants

| Name | Description |
| --- | --- |
| [GestureGroup](arkts-arkui-gesture-con.md#gesturegroup) | Defines GestureGroup Component. |
| [LongPressGesture](arkts-arkui-gesture-con.md#longpressgesture) | Defines LongPressGesture Component. |
| [PanGesture](arkts-arkui-gesture-con.md#pangesture) | Defines PanGesture Component. |
| [PinchGesture](arkts-arkui-gesture-con.md#pinchgesture) | Defines PinchGesture Component. |
| [RotationGesture](arkts-arkui-gesture-con.md#rotationgesture) | Defines RotationGesture Component. |
| [SwipeGesture](arkts-arkui-gesture-con.md#swipegesture) | Defines SwipeGesture Component. |
| [TapGesture](arkts-arkui-gesture-con.md#tapgesture) | Defines TapGesture Component. |

## Examples

This example demonstrates the recognition of a long press gesture using LongPressGesture. Since API version 22, the allowableMovement attribute in [LongPressGestureHandlerOptions](./ts-gesturehandler.md#longpressgesturehandleroptions) can be used to set the maximum movement distance of a gesture to be recognized.

```TypeScript
// xxx.ets
@Entry
@Component
struct LongPressGestureExample {
  @State count: number = 0;

  build() {
    Column() {
      Text('LongPress onAction:' + this.count).fontSize(28)
        // This gesture event is triggered when the text is long-pressed with a single finger.
        .gesture(
        // Set the maximum movement distance allowed for gesture recognition by the long press gesture recognizer to 200 px.
        LongPressGesture({ repeat: true, allowableMovement: 200 })
          // Since repeat is set to true, the event callback is continuously triggered during the long press, with the triggering interval specified by duration (500 ms by default).
          .onAction((event: GestureEvent) => {
            if (event && event.repeat) {
              this.count++
            }
          })
            // Triggered when the long press gesture ends.
          .onActionEnd((event: GestureEvent) => {
            this.count = 0
          })
        )
    }
    .height(200)
    .width(300)
    .padding(20)
    .border({ width: 3 })
    .margin(30)
  }
}
```

This example demonstrates the recognition of a double-tap gesture using TapGesture.

```TypeScript
// xxx.ets
@Entry
@Component
struct TapGestureExample {
  @State value: string = '';

  build() {
    Column() {
      // The gesture event is triggered by double-tapping.
      Text('Click twice').fontSize(28)
        .gesture(
        TapGesture({ count: 2 })
          .onAction((event: GestureEvent) => {
            if (event) {
              this.value = JSON.stringify(event.fingerList[0])
            }
          })
        )
      Text(this.value)
    }
    .height(300)
    .width(300)
    .padding(20)
    .border({ width: 3 })
    .margin(30)
  }
}
```

This example demonstrates how to obtain the coordinates of a single-tap gesture using TapGesture.

```TypeScript
// xxx.ets
@Entry
@Component
struct TapGestureExample {

  build() {
    Column() {
      Text('Click Once').fontSize(28)
        .gesture(
          TapGesture({ count: 1, fingers: 1 })
            .onAction((event: GestureEvent | undefined) => {
              if (event) {
                console.info(`x = ${JSON.stringify(event.tapLocation?.x)}`)
                console.info(`y = ${JSON.stringify(event.tapLocation?.y)}`)
                console.info(`windowX = ${JSON.stringify(event.tapLocation?.windowX)}`)
                console.info(`windowY = ${JSON.stringify(event.tapLocation?.windowY)}`)
                console.info(`displayX = ${JSON.stringify(event.tapLocation?.displayX)}`)
                console.info(`displayY = ${JSON.stringify(event.tapLocation?.displayY)}`)
                // The globalDisplayX and globalDisplayY attributes are added since API version 23.
                console.info(`globalDisplayX = ${JSON.stringify(event.tapLocation?.globalDisplayX)}`)
                console.info(`globalDisplayY = ${JSON.stringify(event.tapLocation?.globalDisplayY)}`)
              }
            })
        )
    }
    .height(200)
    .width(300)
    .padding(20)
    .border({ width: 3 })
    .margin(30)
  }
}
```

This example demonstrates the recognition of single-finger and double-finger pan gestures using PanGesture.

```TypeScript
// xxx.ets
@Entry
@Component
struct PanGestureExample {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right });

  build() {
    Column() {
      Column() {
        Text('PanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
      }
      .height(200)
      .width(300)
      .padding(20)
      .border({ width: 3 })
      .margin(50)
      .translate({ x: this.offsetX, y: this.offsetY, z: 0}) // Move the component with its upper left corner as the coordinate origin.
      // Pan left and right to trigger the gesture event
      .gesture(
      PanGesture(this.panOption)
        .onActionStart((event: GestureEvent) => {
          console.info('Pan start');
          console.info(`Pan start timeStamp is: ${event.timestamp}`);
        })
        .onActionUpdate((event: GestureEvent) => {
          if (event) {
            this.offsetX = this.positionX + event.offsetX;
            this.offsetY = this.positionY + event.offsetY;
          }
        })
        .onActionEnd((event: GestureEvent) => {
          this.positionX = this.offsetX;
          this.positionY = this.offsetY;
          console.info('Pan end');
          console.info(`Pan end timeStamp is: ${event.timestamp}`);
        })
      )

      Button('Set PanGesture Trigger Condition')
        .onClick(() => {
          // Change the trigger condition to double-finger panning in any direction.
          this.panOption.setDirection(PanDirection.All);
          this.panOption.setFingers(2);
        })
    }
  }
}
```

This example demonstrates how to implement swipe gesture recognition.

```TypeScript
// xxx.ets
@Entry
@Component
struct SwipeGestureExample {
  @State rotateAngle: number = 0;
  @State speed: number = 1;

  build() {
    Column() {
      Column() {
        Text("SwipeGesture speed\n" + this.speed)
        Text("SwipeGesture angle\n" + this.rotateAngle)
      }
      .border({ width: 3 })
      .width(300)
      .height(200)
      .margin(100)
      .rotate({ angle: this.rotateAngle })
      // This event is triggered when the user swipes vertically with one finger.
      .gesture(
      SwipeGesture({ direction: SwipeDirection.Vertical })
        .onAction((event: GestureEvent) => {
          if (event) {
            this.speed = event.speed
            this.rotateAngle = event.angle
          }
        })
      )
    }.width('100%')
  }
}
```

This example demonstrates the recognition of a two-finger rotation gesture using RotationGesture.

```TypeScript
// xxx.ets
@Entry
@Component
struct RotationGestureExample {
  @State angle: number = 0;
  @State rotateValue: number = 0;

  build() {
    Column() {
      Column() {
        Text('RotationGesture angle:' + this.angle)
      }
      .height(200)
      .width(300)
      .padding(20)
      .border({ width: 3 })
      .margin(80)
      .rotate({ angle: this.angle })
      // The gesture event is triggered by rotating with two fingers.
      .gesture(
      RotationGesture()
        .onActionStart((event: GestureEvent) => {
          console.info('Rotation start')
        })
        .onActionUpdate((event: GestureEvent) => {
          if (event) {
            this.angle = this.rotateValue + event.angle
          }
        })
        .onActionEnd((event: GestureEvent) => {
          this.rotateValue = this.angle
          console.info('Rotation end')
        })
      )
    }.width('100%')
  }
}
```

This example demonstrates the sequential recognition of combined gestures, specifically long press and pan gestures, using GestureGroup.

```TypeScript
// xxx.ets
@Entry
@Component
struct GestureGroupExample {
  @State count: number = 0;
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  @State borderStyles: BorderStyle = BorderStyle.Solid;

  build() {
    Column() {
      Text('sequence gesture\n' + 'LongPress onAction:' + this.count + '\nPanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
        .fontSize(15);
    }
    .translate({ x: this.offsetX, y: this.offsetY, z: 0 })
    .height(150)
    .width(200)
    .padding(20)
    .margin(20)
    .border({ width: 3, style: this.borderStyles })
    .gesture(
      // The following combined gestures use sequence recognition. If the long press gesture event is not triggered normally, the drag gesture event will not be triggered.
      GestureGroup(GestureMode.Sequence,
        LongPressGesture({ repeat: true })
          .onAction((event?: GestureEvent) => {
            if (event && event.repeat) {
              this.count++;
            }
            console.info('LongPress onAction');
          }),
        PanGesture()
          .onActionStart(() => {
            this.borderStyles = BorderStyle.Dashed;
            console.info('pan start');
          })
          .onActionUpdate((event?: GestureEvent) => {
            if (event) {
              this.offsetX = this.positionX + event.offsetX;
              this.offsetY = this.positionY + event.offsetY;
            }
            console.info('pan update');
          })
          .onActionEnd(() => {
            this.positionX = this.offsetX;
            this.positionY = this.offsetY;
            this.borderStyles = BorderStyle.Solid;
            console.info('pan end');
          })
      )
        .onCancel(() => {
          console.info('sequence gesture canceled');
        })
    );
  }
}
```

This example demonstrates the recognition of a three-finger pinch gesture using PinchGesture.

```TypeScript
// xxx.ets
@Entry
@Component
struct PinchGestureExample {
  @State scaleValue: number = 1;
  @State pinchValue: number = 1;
  @State pinchX: number = 0;
  @State pinchY: number = 0;

  build() {
    Column() {
      Column() {
        Text('PinchGesture scale:\n' + this.scaleValue)
        Text('PinchGesture center:\n(' + this.pinchX + ',' + this.pinchY + ')')
      }
      .height(200)
      .width(300)
      .padding(20)
      .border({ width: 3 })
      .margin({ top: 100 })
      .scale({ x: this.scaleValue, y: this.scaleValue, z: 1 })
      // The gesture event is triggered by pinching three fingers together.
      .gesture(
      PinchGesture({ fingers: 3 }) // Three-finger pinch gesture for zooming in or out.
        .onActionStart((event: GestureEvent) => {
          console.info('Pinch start')
        })
        .onActionUpdate((event: GestureEvent) => {
          if (event) {
            this.scaleValue = this.pinchValue * event.scale
            this.pinchX = event.pinchCenterX
            this.pinchY = event.pinchCenterY
          }
        })
        .onActionEnd((event: GestureEvent) => {
          this.pinchValue = this.scaleValue
          console.info('Pinch end')
        })
      )
    }.width('100%')
  }
}
```

This example demonstrates how to implement image scaling with finger tracking by configuring PinchGesture.

```TypeScript
// xxx.ets
import { UIContext, display, matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct PinchGestureExample {
  private uiContext: UIContext = new UIContext();
  private contentWidth: number = 0;
  private contentHeight: number = 0;
  private scaleMin: number = 0.3;
  private scaleMax: number = 30.0;
  private screenWidth: number = 0;
  private screenHeight: number = 0;
  @State pntX: number = 0;
  @State pntY: number = 0;
  @State curScale: number = 1;
  @State preScale: number = 1;
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State matrix: matrix4.Matrix4Transit = matrix4.identity()
    .translate({ x: this.offsetX, y: this.offsetY })
    .scale({ x: this.curScale, y: this.curScale });

  public updateMatrix(): void {
    this.matrix = matrix4.identity()
      .scale({ x: this.curScale, y: this.curScale })
      .translate({ x: this.uiContext.vp2px(this.offsetX), y: this.uiContext.vp2px(this.offsetY) });
  }

  aboutToAppear(): void {
    this.uiContext = this.getUIContext();
    let screenSize = display.getDefaultDisplaySync();
    this.screenWidth = this.uiContext.px2vp(screenSize.width);
    this.screenHeight = this.uiContext.px2vp(screenSize.height);
  }

  build() {
    Column() {
      // Replace $r('app.media.img') with the image resource file you use.
      Image($r('app.media.img'))
        .objectFit(ImageFit.Contain)
        .draggable(false)
        .onComplete((event) => {
          this.contentWidth = this.uiContext.px2vp(event!.contentWidth);
          this.contentHeight = this.uiContext.px2vp(event!.contentHeight);
        })
        .transform(this.matrix)
    }
    // The gesture event is triggered by a two-finger pinch.
    .gesture(
      PinchGesture({ fingers: 2 }) // Two-finger pinch gesture for zooming in or out.
        .onActionStart((event: GestureEvent) => {
          // Displayed size of the image before scaling
          const displayWidth = this.contentWidth * this.curScale;
          const displayHeight = this.contentHeight * this.curScale;
          // Upper left corner coordinates before scaling
          const left = (this.screenWidth - displayWidth) / 2 + this.offsetX;
          const top = (this.screenHeight - displayHeight) / 2 + this.offsetY;
          // Pinch center position (as a percentage) relative to the upper left corner of the displayed image
          this.pntX = (event.pinchCenterX - left) / displayWidth;
          this.pntY = (event.pinchCenterY - top) / displayHeight;
          // Scale factor before the current operation
          this.preScale = this.curScale;
        })
        .onActionUpdate((event: GestureEvent) => {
          // Target scale factor
          this.curScale = this.preScale * event.scale;
          let targetDisplayWidth = this.contentWidth * this.curScale;
          let targetDisplayHeight = this.contentHeight * this.curScale;
          // Coordinates of the pinch center after scaling
          const pointX = (this.screenWidth - targetDisplayWidth) / 2 + targetDisplayWidth * this.pntX;
          const pointY = (this.screenHeight - targetDisplayHeight) / 2 + targetDisplayHeight * this.pntY;
          // Offset required to align the calculated point (pointX, pointY) with the actual pinch center after scaling
          this.offsetX = event.pinchCenterX - pointX;
          this.offsetY = event.pinchCenterY - pointY;
          this.updateMatrix();
        })
        .onActionEnd((event: GestureEvent) => {
          if (this.curScale < this.scaleMin || this.curScale > this.scaleMax) {
            this.curScale = 1;
            this.offsetX = 0;
            this.offsetY = 0;
            this.updateMatrix();
          }
        })
    )
  }
}
```
