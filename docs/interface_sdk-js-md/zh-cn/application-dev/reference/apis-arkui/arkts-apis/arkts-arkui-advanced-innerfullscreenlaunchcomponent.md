# @ohos.arkui.advanced.InnerFullScreenLaunchComponent(系统接口)

## 子组件

无。

## 属性

不支持通用属性。

## 事件

不支持通用事件。

## 导入模块

```TypeScript
import { InnerFullScreenLaunchComponent, LaunchController } from '@kit.ArkUI';
```

## 汇总

<!--Del-->
### 类（系统接口）

| 名称 | 说明 |
| --- | --- |
| [LaunchController](arkts-arkui-arkui-advanced-innerfullscreenlaunchcomponent-launchcontroller-c-sys.md) | 拉起原子化服务的控制器。 |
<!--DelEnd-->

<!--Del-->
### 结构体（系统接口）

| 名称 | 说明 |
| --- | --- |
| [InnerFullScreenLaunchComponent](arkts-arkui-arkui-advanced-innerfullscreenlaunchcomponent-innerfullscreenlaunchcomponent-s-sys.md) | 非显式全屏拉起原子化服务组件，拉起方可以选择拉起原子化服务的时机。当被拉起方授权使用方嵌入式运行原子化服务时，使用方全屏嵌入式运行原子化服务；未授权时，使用方跳出式拉起原子化服务。 |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 | 说明 |
| --- | --- |
| [LaunchAtomicServiceCallback](arkts-arkui-launchatomicservicecallback-t-sys.md) | 拉起原子化服务触发的回调。 |
<!--DelEnd-->

## 示例

> 说明：

```TypeScript
import { InnerFullScreenLaunchComponent, LaunchController } from '@kit.ArkUI';

@Entry
@Component
struct Index {

  @Builder
  ColumnChild() {
    Column() {
      Text('InnerFullScreenLaunchComponent').fontSize(16).margin({top: 100})
      Button('start 日出日落')
        .onClick(() => {
          let appId1: string = '576****************';
          this.controller.launchAtomicService(appId1, {});
        }).height(30).width('50%').margin({top: 50})
      Button('start 充值')
        .onClick(() => {
          let appId2: string = '576****************';
          this.controller.launchAtomicService(appId2, {});
        }).height(30).width('50%').margin({top: 50})
    }.backgroundColor(Color.Pink).height('100%').width('100%')
  }
  controller: LaunchController = new LaunchController();

  build() {
    Column() {
      InnerFullScreenLaunchComponent({
          content: this.ColumnChild,
          controller: this.controller,
          onReceive: (data) => {
            console.info('onReceive, data: ' + JSON.stringify(data['ohos.atomicService.window']));
          },
          onError: (err: BusinessError) => {
            console.error(`onError, code: ${err.code}, message: ${err.message}`);
          },
          onTerminated: (info: TerminationInfo) => {
            console.info('onTerminated, info: ' + JSON.stringify(info));
          }
        })
    }
    .width('100%').height('100%')
  }
}
```
