# gesture

定义手势竞争结果。

## 导入模块

```TypeScript
```

## 汇总

### 命名空间

| 名称 | 说明 |
| --- | --- |
| [GestureControl](arkts-arkui-gesturecontrol-n.md) | 定义手势竞争结果。 |

### 类

| 名称 | 说明 |
| --- | --- |
| [EventTargetInfo](arkts-arkui-eventtargetinfo-c.md) | 手势识别器对应组件的信息。 |
| [GestureGroupHandler](arkts-arkui-gesturegrouphandler-c.md) | 手势组处理器对象类型。 |
| [GestureHandler](arkts-arkui-gesturehandler-c.md) | 手势处理器的基础类型。 |
| [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md) | 手势识别器对象。 |
| [LongPressGestureHandler](arkts-arkui-longpressgesturehandler-c.md) | 长按手势处理器对象类型。 |
| [LongPressRecognizer](arkts-arkui-longpressrecognizer-c.md) | 长按手势识别器对象，继承于[GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)。 |
| [PanGestureHandler](arkts-arkui-pangesturehandler-c.md) | 滑动手势处理器对象类型。 |
| [PanGestureOptions](arkts-arkui-pangestureoptions-c.md) | 定义PanGesture配置参数选项。 |
| [PanRecognizer](arkts-arkui-panrecognizer-c.md) | 手势识别器对象。 |
| [PinchGestureHandler](arkts-arkui-pinchgesturehandler-c.md) | 捏合手势处理器对象类型。 |
| [PinchRecognizer](arkts-arkui-pinchrecognizer-c.md) | 捏合手势识别器对象，继承于[GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)。 |
| [RotationGestureHandler](arkts-arkui-rotationgesturehandler-c.md) | 旋转手势处理器对象类型。 |
| [RotationRecognizer](arkts-arkui-rotationrecognizer-c.md) | 旋转手势识别器对象，继承于[GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)。 |
| [ScrollableTargetInfo](arkts-arkui-scrollabletargetinfo-c.md) | 手势识别器对应的滚动类容器组件的信息，继承于[EventTargetInfo](arkts-arkui-eventtargetinfo-c.md)。 |
| [SwipeGestureHandler](arkts-arkui-swipegesturehandler-c.md) | 快滑手势处理器对象类型。 |
| [SwipeRecognizer](arkts-arkui-swiperecognizer-c.md) | 快滑手势识别器对象，继承于[GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)。 |
| [TapGestureHandler](arkts-arkui-tapgesturehandler-c.md) | 点击手势处理器对象类型。 |
| [TapRecognizer](arkts-arkui-taprecognizer-c.md) | 点击手势识别器对象，继承自[GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)。 |
| [TouchRecognizer](arkts-arkui-touchrecognizer-c.md) | 触摸识别器对象。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [BaseGestureEvent](arkts-arkui-basegestureevent-i.md) | 基础手势事件类型。继承自[BaseEvent](../arkts-components/arkts-arkui-baseevent-i.md)。 |
| [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md) | 基础手势处理器配置参数。 |
| [EventLocationInfo](arkts-arkui-eventlocationinfo-i.md) | 用于点击手势获取点击位置坐标。 |
| [FingerInfo](arkts-arkui-fingerinfo-i.md) | 手指信息类型。 |
| [GestureEvent](arkts-arkui-gestureevent-i.md) | 定义手势的事件信息。继承自[BaseEvent](../arkts-components/arkts-arkui-baseevent-i.md)。 |
| [GestureGroupGestureHandlerOptions](arkts-arkui-gesturegroupgesturehandleroptions-i.md) | 手势组处理器配置参数。 |
| [GestureGroupInterface](arkts-arkui-gesturegroupinterface-i.md) | 手势识别组合，即两种及以上手势组合为复合手势，支持顺序识别、并发识别和互斥识别。 |
| [GestureInfo](arkts-arkui-gestureinfo-i.md) | 手势信息类型。 |
| [GestureInterface](arkts-arkui-gestureinterface-i.md) | 定义Gesture接口。 |
| [LongPressGestureEvent](arkts-arkui-longpressgestureevent-i.md) | 继承自[BaseGestureEvent](arkts-arkui-basegestureevent-i.md)。可将该对象作为[onGestureJudgeBegin](../arkts-components/arkts-arkui-commonmethod-c.md#ongesturejudgebegin)的event参数来传递。 |
| [LongPressGestureHandlerOptions](arkts-arkui-longpressgesturehandleroptions-i.md) | 长按手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。 |
| [LongPressGestureInterface](arkts-arkui-longpressgestureinterface-i.md) | 用于触发长按手势事件，触发长按手势的最少手指数为1，默认最短长按时间为500毫秒。可配置duration参数控制最短长按时长。 |
| [PanGestureEvent](arkts-arkui-pangestureevent-i.md) | 继承自[BaseGestureEvent](arkts-arkui-basegestureevent-i.md)。可将该对象作为[onGestureJudgeBegin](../arkts-components/arkts-arkui-commonmethod-c.md#ongesturejudgebegin)的event参数来传递。 |
| [PanGestureHandlerOptions](arkts-arkui-pangesturehandleroptions-i.md) | 滑动手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。 |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) | 滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。 |
| [PinchGestureEvent](arkts-arkui-pinchgestureevent-i.md) | 继承自[BaseGestureEvent](arkts-arkui-basegestureevent-i.md)。可将该对象作为[onGestureJudgeBegin](../arkts-components/arkts-arkui-commonmethod-c.md#ongesturejudgebegin)的event参数来传递。 |
| [PinchGestureHandlerOptions](arkts-arkui-pinchgesturehandleroptions-i.md) | 捏合手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。 |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) | 用于触发捏合手势，最少需要2指，最多5指，最小识别距离为5vp。在支持鼠标和键盘输入的设备上，通过“Ctrl+鼠标滚轮”也可以触发捏合手势。 |
| [RotationGestureEvent](arkts-arkui-rotationgestureevent-i.md) | 继承自[BaseGestureEvent](arkts-arkui-basegestureevent-i.md)。可将该对象作为[onGestureJudgeBegin](../arkts-components/arkts-arkui-commonmethod-c.md#ongesturejudgebegin)的event参数来传递。 |
| [RotationGestureHandlerOptions](arkts-arkui-rotationgesturehandleroptions-i.md) | 旋转手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。 |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) | 用于触发旋转手势，最少需要2指，最多5指，最小改变度数为1度。该手势不支持通过触控板双指旋转操作触发。 |
| [SwipeGestureEvent](arkts-arkui-swipegestureevent-i.md) | 继承自[BaseGestureEvent](arkts-arkui-basegestureevent-i.md)。可将该对象作为[onGestureJudgeBegin](../arkts-components/arkts-arkui-commonmethod-c.md#ongesturejudgebegin)的event参数来传递。 |
| [SwipeGestureHandlerOptions](arkts-arkui-swipegesturehandleroptions-i.md) | 快滑手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。 |
| [SwipeGestureInterface](arkts-arkui-swipegestureinterface-i.md) | 用于触发快滑手势，滑动速度需大于速度阈值，默认最小速度为100vp/s。 |
| [TapGestureEvent](arkts-arkui-tapgestureevent-i.md) | 继承自[BaseGestureEvent](arkts-arkui-basegestureevent-i.md)。可将该对象作为[onGestureJudgeBegin](../arkts-components/arkts-arkui-commonmethod-c.md#ongesturejudgebegin)的event参数来传递。 |
| [TapGestureHandlerOptions](arkts-arkui-tapgesturehandleroptions-i.md) | 点击手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。 |
| [TapGestureInterface](arkts-arkui-tapgestureinterface-i.md) | 支持单击、双击和多次点击事件的识别。 |
| [TapGestureParameters](arkts-arkui-tapgestureparameters-i.md) | 点击手势参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [GestureJudgeResult](arkts-arkui-gesturejudgeresult-e.md) | 定义手势竞争结果。 |
| [GestureMask](arkts-arkui-gesturemask-e.md) | 定义是否屏蔽子组件手势。 |
| [GestureMode](arkts-arkui-gesturemode-e.md) | 定义手势组的识别模式。 |
| [GesturePriority](arkts-arkui-gesturepriority-e.md) | 绑定手势的优先级。 |
| [GestureRecognizerState](arkts-arkui-gesturerecognizerstate-e.md) | 定义手势识别器状态。 |
| [PanDirection](arkts-arkui-pandirection-e.md) | 与SwipeDirection不同，PanDirection没有角度限制。 |
| [SwipeDirection](arkts-arkui-swipedirection-e.md) | 定义滑动手势的触发方向。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [GestureType](arkts-arkui-gesturetype-t.md) | Defines the Gesture Type. |

### 常量

| 名称 | 说明 |
| --- | --- |
| [GestureGroup](arkts-arkui-gesture-con.md#gesturegroup) | Defines GestureGroup Component. |
| [LongPressGesture](arkts-arkui-gesture-con.md#longpressgesture) | Defines LongPressGesture Component. |
| [PanGesture](arkts-arkui-gesture-con.md#pangesture) | Defines PanGesture Component. |
| [PinchGesture](arkts-arkui-gesture-con.md#pinchgesture) | Defines PinchGesture Component. |
| [RotationGesture](arkts-arkui-gesture-con.md#rotationgesture) | Defines RotationGesture Component. |
| [SwipeGesture](arkts-arkui-gesture-con.md#swipegesture) | Defines SwipeGesture Component. |
| [TapGesture](arkts-arkui-gesture-con.md#tapgesture) | Defines TapGesture Component. |

## 示例

该示例通过LongPressGesture实现了长按手势的识别。从API version 22开始，支持通过[LongPressGestureHandlerOptions](./ts-gesturehandler.md#longpressgesturehandleroptions)的allowableMovement属性设置识别手势的最大移动距离。

```TypeScript
// xxx.ets
@Entry
@Component
struct LongPressGestureExample {
  @State count: number = 0;

  build() {
    Column() {
      Text('LongPress onAction:' + this.count).fontSize(28)
        // 单指长按文本触发该手势事件。
        .gesture(
        // 设置长按手势识别器识别的手势的最大移动距离为200px。
        LongPressGesture({ repeat: true, allowableMovement: 200 })
          // 由于repeat设置为true，长按动作存在时会连续触发，触发间隔为duration（默认值500ms）。
          .onAction((event: GestureEvent) => {
            if (event && event.repeat) {
              this.count++;
            }
          })
            // 长按动作一结束触发。
          .onActionEnd(() => {
            this.count = 0;
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

该示例通过TapGesture实现了双击手势的识别。

```TypeScript
// xxx.ets
@Entry
@Component
struct TapGestureExample {
  @State value: string = '';

  build() {
    Column() {
      // 单指双击文本触发手势事件
      Text('Click twice').fontSize(28)
        .gesture(
        TapGesture({ count: 2 })
          .onAction((event: GestureEvent) => {
            if (event) {
              this.value = JSON.stringify(event.fingerList[0]);
            }
          })
        );
      Text(this.value);
    }
    .height(300)
    .width(300)
    .padding(20)
    .border({ width: 3 })
    .margin(30);
  }
}
```

该示例通过TapGesture获取单击手势点击位置的坐标。

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
                console.info(`x = ${JSON.stringify(event.tapLocation?.x)}`);
                console.info(`y = ${JSON.stringify(event.tapLocation?.y)}`);
                console.info(`windowX = ${JSON.stringify(event.tapLocation?.windowX)}`);
                console.info(`windowY = ${JSON.stringify(event.tapLocation?.windowY)}`);
                console.info(`displayX = ${JSON.stringify(event.tapLocation?.displayX)}`);
                console.info(`displayY = ${JSON.stringify(event.tapLocation?.displayY)}`);
                // 从API version 23开始，新增globalDisplayX和globalDisplayY属性。
                console.info(`globalDisplayX = ${JSON.stringify(event.tapLocation?.globalDisplayX)}`);
                console.info(`globalDisplayY = ${JSON.stringify(event.tapLocation?.globalDisplayY)}`);
              }
            })
        );
    }
    .height(200)
    .width(300)
    .padding(20)
    .border({ width: 3 })
    .margin(30)
  }
}
```

该示例通过getCurrentLocalPosition方法获取点击位置相对于当前组件实时位置左上角的坐标。
从API版本26.0.0开始，新增支持getCurrentLocalPosition接口。

```TypeScript
// xxx.ets
@Entry
@Component
struct GetCurrentLocalPositionExample {
  @State positionText: string = '';
  @State textOffsetY: number = 0;

  build() {
    Column() {
      Button('点击获取点击位置相对于当前组件实时位置左上角的坐标').translate({ y: this.textOffsetY })
        .gesture(
          TapGesture({ count: 1 })
            .onAction((event: GestureEvent) => {
              if (event) {
                // 移动组件后延迟获取点击位置相对于组件实时位置左上角的坐标。
                this.textOffsetY = -200;
                setTimeout(() => {
                  let localPos: Coordinate2D | undefined = event?.tapLocation?.getCurrentLocalPosition?.();
                  this.positionText = `相对于当前组件实时位置左上角的坐标:\n  x: ${localPos?.x ?? 0}\n  y: ${localPos?.y ?? 0}`;
                }, 2000);
              }
            })
        );

      Text(this.positionText);
    }.width('100%');
  }
}
```

该示例通过PanGesture实现了单指/双指滑动手势的识别。

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
      .translate({ x: this.offsetX, y: this.offsetY, z: 0 }) // 以组件左上角为坐标原点进行移动
      // 左右滑动触发该手势事件
      .gesture(
      PanGesture(this.panOption)
        .onActionStart((event: GestureEvent) => {
          console.info('Pan start');
          console.info(`Pan start timeStamp is: ${event.timestamp}`);
        })
        .onActionUpdate((event: GestureEvent) => {
          if (event) {
            // 根据滑动偏移量更新组件当前位置
            this.offsetX = this.positionX + event.offsetX;
            this.offsetY = this.positionY + event.offsetY;
          }
        })
        .onActionEnd((event: GestureEvent) => {
          // 滑动结束后保存当前位置，作为下一次滑动的起始位置
          this.positionX = this.offsetX;
          this.positionY = this.offsetY;
          console.info('Pan end');
          console.info(`Pan end timeStamp is: ${event.timestamp}`);
        })
      )

      Button('修改PanGesture触发条件')
        .onClick(() => {
          // 将PanGesture手势事件触发条件改为双指以任意方向滑动
          this.panOption.setDirection(PanDirection.All);
          this.panOption.setFingers(2);
        })
    }
  }
}
```

该示例展示了如何实现快滑手势的识别。

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
        Text('SwipeGesture speed\n' + this.speed)
        Text('SwipeGesture angle\n' + this.rotateAngle)
      }
      .border({ width: 3 })
      .width(300)
      .height(200)
      .margin(100)
      .rotate({ angle: this.rotateAngle })
      // 单指竖直方向快滑时触发该事件
      .gesture(
      SwipeGesture({ direction: SwipeDirection.Vertical })
        .onAction((event: GestureEvent) => {
          if (event) {
            this.speed = event.speed;
            this.rotateAngle = event.angle;
          }
        })
      )
    }.width('100%');
  }
}
```

该示例通过配置RotationGesture实现了双指旋转手势的识别。

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
      // 双指旋转触发该手势事件
      .gesture(
      RotationGesture()
        .onActionStart(() => {
          console.info('Rotation start');
        })
        .onActionUpdate((event: GestureEvent) => {
          if (event) {
            // 根据本次手势变化角度和已保存旋转角度，更新组件当前旋转角度。
            this.angle = this.rotateValue + event.angle;
          }
        })
        .onActionEnd(() => {
          // 手势结束时保存当前旋转角度，作为下一次旋转计算的初始值。
          this.rotateValue = this.angle;
          console.info('Rotation end');
        })
      )
    }.width('100%')
  }
}
```

该示例通过配置PinchGesture实现了三指捏合手势的识别功能。

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
      // 三指捏合触发该手势事件
      .gesture(
      PinchGesture({ fingers: 3 }) // 三指捏合手势，用于缩放操作
        .onActionStart(() => {
          console.info('Pinch start');
        })
        // 捏合手势更新时，根据缩放比例和中心点坐标更新展示状态
        .onActionUpdate((event: GestureEvent) => {
          if (event) {
            this.scaleValue = this.pinchValue * event.scale;
            this.pinchX = event.pinchCenterX;
            this.pinchY = event.pinchCenterY;
          }
        })
        // 手势结束时保存当前缩放比例，作为下一次缩放的基准值
        .onActionEnd(() => {
          this.pinchValue = this.scaleValue;
          console.info('Pinch end');
        })
      )
    }.width('100%')
  }
}
```

通过配置PinchGesture，该示例实现了图片的跟手缩放效果。

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
  @State pointRatioX: number = 0;
  @State pointRatioY: number = 0;
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
      // $r('app.media.img')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.img'))
        .objectFit(ImageFit.Contain)
        .draggable(false)
        .onComplete((event) => {
          this.contentWidth = this.uiContext.px2vp(event!.contentWidth);
          this.contentHeight = this.uiContext.px2vp(event!.contentHeight);
        })
        .transform(this.matrix)
    }
    // 双指捏合触发该手势事件
    .gesture(
      PinchGesture({ fingers: 2 }) // 双指捏合手势，用于缩放图片
        .onActionStart((event: GestureEvent) => {
          // 图片本次缩放前展示大小
          const displayWidth = this.contentWidth * this.curScale;
          const displayHeight = this.contentHeight * this.curScale;
          // 图片本次缩放前左上角顶点
          const left = (this.screenWidth - displayWidth) / 2 + this.offsetX;
          const top = (this.screenHeight - displayHeight) / 2 + this.offsetY;
          // 本次缩放前手指中点相对图片左上角顶点尺寸占图片展示尺寸的百分比
          this.pointRatioX = (event.pinchCenterX - left) / displayWidth;
          this.pointRatioY = (event.pinchCenterY - top) / displayHeight;
          // 图片本次缩放前的缩放比例
          this.preScale = this.curScale;
        })
        .onActionUpdate((event: GestureEvent) => {
          // 目标缩放比
          this.curScale = this.preScale * event.scale;
          let targetDisplayWidth = this.contentWidth * this.curScale;
          let targetDisplayHeight = this.contentHeight * this.curScale;
          // 本次缩放前手指中点在本次缩放后的坐标
          const pointX = (this.screenWidth - targetDisplayWidth) / 2 + targetDisplayWidth * this.pointRatioX;
          const pointY = (this.screenHeight - targetDisplayHeight) / 2 + targetDisplayHeight * this.pointRatioY;
          // 将pointX、pointY移动到缩放后的手指中点，需要移动的距离
          this.offsetX = event.pinchCenterX - pointX;
          this.offsetY = event.pinchCenterY - pointY;
          this.updateMatrix();
        })
        .onActionEnd((event: GestureEvent) => {
          // 缩放比例超出允许范围时，重置图片的缩放比例和偏移量
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

该示例通过配置GestureGroup，实现了长按和拖动的组合手势顺序识别功能。

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
      // 以下组合手势为顺序识别，当长按手势事件未正常触发时则不会触发拖动手势事件
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
