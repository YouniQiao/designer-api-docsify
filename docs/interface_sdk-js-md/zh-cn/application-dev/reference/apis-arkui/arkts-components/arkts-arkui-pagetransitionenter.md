# PageTransitionEnter

Defines PageTransitionEnter Component.

## PageTransitionEnter

```TypeScript
PageTransitionEnter(value: PageTransitionOptions)
```

设置当前页面的自定义入场动效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PageTransitionOptions](arkts-arkui-pagetransitionoptions-i.md) | 是 | 配置入场动效的参数。 |

## PageTransitionEnter

```TypeScript
PageTransitionEnter(event: PageTransitionCallback)
```

逐帧回调，直到入场动画结束，progress从0变化到1。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [PageTransitionCallback](arkts-arkui-pagetransitioncallback-t.md) | 是 | 入场动画的逐帧回调直到入场动画结束，progress从0变化到1。 |

## 汇总

### 接口

| 名称 | 说明 |
| --- | --- |
| [PageTransitionExitInterface](arkts-arkui-pagetransitionexitinterface-i.md) | 当前页面的自定义退场动效。继承自[CommonTransition](arkts-arkui-commontransition-c.md)。 |
| [PageTransitionOptions](arkts-arkui-pagetransitionoptions-i.md) | 退场/进场动效的参数。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [PageTransitionCallback](arkts-arkui-pagetransitioncallback-t.md) | 页面转场事件回调。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [RouteType](arkts-arkui-routetype-e.md) | 页面转场类型。 |
| [SlideEffect](arkts-arkui-slideeffect-e.md) | 页面转场时的滑入滑出效果。 |

## 示例

自定义方式1：通过不同的退入场类型配置不同的退场和入场动画。

```TypeScript
// Index.ets
@Entry
@Component
struct Index {
  @State pageScale: number = 1;
  @State pageOpacity: number = 1;

  build() {
    Column() {
      // $r("app.media.transition_image1")需要替换为开发者所需的图像资源文件。
      Image($r('app.media.transition_image1')).width('100%').height('100%')
    }
    .width('100%')
    .height('100%')
    .scale({ x: this.pageScale })
    .opacity(this.pageOpacity)
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Page1' });
    })
  }

  pageTransition() {
    PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
      .onEnter((type: RouteType, progress: number) => {
        if (type == RouteType.Push || type == RouteType.Pop) {
          this.pageScale = progress;
          this.pageOpacity = progress;
        }
      })
    PageTransitionExit({ duration: 1200, curve: Curve.Ease })
      .onExit((type: RouteType, progress: number) => {
        if (type == RouteType.Push) {
          this.pageScale = 1 - progress;
          this.pageOpacity = 1 - progress;
        }
      })
  }
}
```

```TypeScript
// Page1.ets
@Entry
@Component
struct Page1 {
  @State pageScale: number = 1;
  @State pageOpacity: number = 1;

  build() {
    Column() {
      // $r("app.media.transition_image2")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.transition_image2")).width('100%').height('100%') // 图片存放在media文件夹下
    }
    .width('100%')
    .height('100%')
    .scale({ x: this.pageScale })
    .opacity(this.pageOpacity)
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Index' });
    })
  }

  pageTransition() {
    PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
      .onEnter((type: RouteType, progress: number) => {
        if (type == RouteType.Push || type == RouteType.Pop) {
          this.pageScale = progress;
        }
        this.pageOpacity = progress;
      })
    PageTransitionExit({ duration: 1200, curve: Curve.Ease })
      .onExit((type: RouteType, progress: number) => {
        if (type == RouteType.Pop) {
          this.pageScale = 1 - progress;
          this.pageOpacity = 1 - progress;
        }
      })
  }
}
```

自定义方式2：配置了当前页面的入场动画为从左侧滑入，退场为平移加透明度变化。

```TypeScript
// Index.ets 
@Entry
@Component
struct Index {
  build() {
    Column() {
      // $r('app.media.bg1')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg1')).width('100%').height('100%') // 图片存放在media文件夹下
    }
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Page1' });
    })
  }

  // 自定义方式2：使用系统提供的多种默认效果（平移、缩放、透明度等）
  pageTransition() {
    // 该页面进入动画时长为1200ms，尽量与另一页面的退出动画时长匹配
    PageTransitionEnter({ duration: 1200 })
      .slide(SlideEffect.Left)
    // 该页面退出动画时长为1000ms，尽量与另一页面的进入动画时长匹配
    PageTransitionExit({ duration: 1000 })
      .translate({ x: 100.0, y: 100.0 })
      .opacity(0)
  }
}
```

```TypeScript
// Page1.ets
@Entry
@Component
struct Page1 {
  build() {
    Column() {
      // $r('app.media.bg2')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg2')).width('100%').height('100%') // 图片存放在media文件夹下
    }
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Index' });
    })
  }

  // 自定义方式2：使用系统提供的多种默认效果（平移、缩放、透明度等）
  pageTransition() {
    // 该页面进入动画时长为1000ms，尽量与另一页面的退出动画时长匹配
    PageTransitionEnter({ duration: 1000 })
      .slide(SlideEffect.Left)
    // 该页面退出动画时长为1200ms，尽量与另一页面的进入动画时长匹配
    PageTransitionExit({ duration: 1200 })
      .translate({ x: 100.0, y: 100.0 })
      .opacity(0)
  }
}
```

自定义方式1：配置提供的不同退入场平移效果，将系统语言排版模式改为RTL。

```TypeScript
// Index.ets
@Entry
@Component
struct Index {
  @State pageScale: number = 1;
  @State pageOpacity: number = 1;

  build() {
    Column() {
      Button("页面1").onClick(() => {
        this.getUIContext().getRouter().pushUrl({
          url: "pages/Page1"
        })
      })
        .width(200)
        .height(60)
        .fontSize(36)
      Text("START")
        .fontSize(36)
        .textAlign(TextAlign.Center)
    }
    .scale({ x: this.pageScale })
    .opacity(this.pageOpacity)
    .height("100%")
    .width("100%")
    .justifyContent(FlexAlign.Center)
  }

  // 自定义方式2：使用系统提供的多种默认效果（平移、缩放、透明度等）
  pageTransition() {
    // 设置入场动效
    PageTransitionEnter({ duration: 200 })
      .slide(SlideEffect.START)
    // 设置退场动效
    PageTransitionExit({ delay: 100 })
      .slide(SlideEffect.START) // Left
  }
}
```

```TypeScript
// Page1.ets
@Entry
@Component
struct Page1 {
  @State pageScale: number = 1;
  @State pageOpacity: number = 1;

  build() {
    Column() {
      Button("页面2").onClick(() => {
        this.getUIContext().getRouter().pushUrl({
          url: "pages/Index"
        });
      })
        .width(200)
        .height(60)
        .fontSize(36)
      Text("END")
        .fontSize(36)
        .textAlign(TextAlign.Center)
    }
    .scale({ x: this.pageScale })
    .opacity(this.pageOpacity)
    .height("100%")
    .width("100%")
    .justifyContent(FlexAlign.Center)
  }

  // 自定义方式2：使用系统提供的多种默认效果（平移、缩放、透明度等）
  pageTransition() {
    PageTransitionEnter({ duration: 200 })
      .slide(SlideEffect.END) // Right
    PageTransitionExit({ delay: 100 })
      .slide(SlideEffect.END)
  }
}
```

自定义方式2：使用系统默认的退入场效果，将系统语言排版模式改为RTL。

```TypeScript
// Index.ets
@Entry
@Component
struct Index {
  @State pageScale: number = 1;
  @State pageOpacity: number = 1;

  build() {
    Column() {
      Button("页面1").onClick(() => {
        this.getUIContext().getRouter().pushUrl({
          url: "pages/Page1"
        });
      })
        .width(200)
        .height(60)
        .fontSize(36)
    }
    .scale({ x: this.pageScale })
    .opacity(this.pageOpacity)
    .height("100%")
    .width("100%")
    .justifyContent(FlexAlign.Center)
  }
}
```

```TypeScript
// Page1.ets
@Entry
@Component
struct Page1 {
  @State pageScale: number = 1;
  @State pageOpacity: number = 1;

  build() {
    Column() {
      Button("页面2").onClick(() => {
        this.getUIContext().getRouter().pushUrl({
          url: "pages/Index"
        });
      })
        .width(200)
        .height(60)
        .fontSize(36)
    }
    .scale({ x: this.pageScale })
    .opacity(this.pageOpacity)
    .height("100%")
    .width("100%")
    .justifyContent(FlexAlign.Center)
  }
}
```
