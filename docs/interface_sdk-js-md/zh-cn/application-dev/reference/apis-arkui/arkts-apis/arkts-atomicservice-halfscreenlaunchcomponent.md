# @ohos.atomicservice.HalfScreenLaunchComponent(Defines the halfScreen launch component)

## 子组件

无。

## 属性

不支持通用属性。

## 导入模块

```TypeScript
import { HalfScreenLaunchComponent } from '@kit.ArkUI';
```

## 汇总

### 结构体

| 名称 | 说明 |
| --- | --- |
| [HalfScreenLaunchComponent](arkts-arkui-atomicservice-halfscreenlaunchcomponent-halfscreenlaunchcomponent-s.md) | 半屏嵌入式启动原子化服务组件，当被拉起方未授权嵌入式运行原子化服务时，宿主将使用跳出式拉起原子化服务。 |

## 示例

该示例展示如何嵌入式拉起手机充值服务。

```TypeScript
import { HalfScreenLaunchComponent } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  appId: string = '576****************'; // 原子化服务appId。

  build() {
    Column() {
      HalfScreenLaunchComponent({
        appId: this.appId,
        options: {},
        onTerminated: (info: TerminationInfo) => {
          console.info('onTerminated info = ' + info.want);
        },
        onError: (err: BusinessError) => {
          console.error(`onError code: ${err.code}, message: ${err.message}`);
        },
        onReceive: (data: Record<string, Object>) => {
          console.info('onReceive, data: ' + data['ohos.atomicService.window']);
        }
      }) {
        Column() {
          Image($r('app.media.app_icon'))
          Text('拉起手机充值')
        }.width('80vp').height('80vp').margin({bottom:30})
      } // 通过尾随闭包形式传入content。
    }
  }

}
```
