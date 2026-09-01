# @ohos.arkui.advanced.FullScreenLaunchComponent(Defines the fullScreen launch component)

## 子组件

无。

## 属性

不支持通用属性。

## 事件

不支持通用事件。

## 导入模块

```TypeScript
import { FullScreenLaunchComponent } from '@kit.ArkUI';
```

## 汇总

### 结构体

| 名称 | 说明 |
| --- | --- |
| [FullScreenLaunchComponent](arkts-arkui-arkui-advanced-fullscreenlaunchcomponent-fullscreenlaunchcomponent-s.md) | 全屏启动原子化服务组件，当提供方授权使用方嵌入式运行原子化服务时，使用方全屏嵌入式运行原子化服务；未授权时，使用方跳出式拉起原子化服务。 |

## 示例

本示例展示组件使用方法和提供方原子化服务的实现。实际运行时请使用开发者自己的原子化服务appId。

```TypeScript
// 使用方入口界面Index.ets内容如下：
import { FullScreenLaunchComponent } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State appId: string = '6917573653426122083'; // 原子化服务appId

  build() {
    Row() {
      Column() {
        FullScreenLaunchComponent({
          content: ColumnChild,
          appId: this.appId,
          options: {},
          onTerminated: (info) => {
            console.info(`onTerminated code: ${info.code.toString()}`);
          },
          onError: (err) => {
            console.error(`onError code: ${err.code}, message: ${err.message}`);
          },
          onReceive: (data) => {
            console.info(`onReceive, data: ${JSON.stringify(data)}`);
          }
        }).width('80vp').height('80vp')
      }
      .width('100%')
    }
    .height('100%')
  }
}

@Builder
function ColumnChild() {
  Column() {
    Image($r('app.media.startIcon'))
    Text('test')
  }
}
```

组件提供方

```TypeScript
import { AbilityConstant, Want, EmbeddableUIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends EmbeddableUIAbility {
  storage = new LocalStorage();
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    let mainWindow = windowStage.getMainWindowSync();
    this.storage.setOrCreate('window', mainWindow);
    this.storage.setOrCreate('windowStage', windowStage);
    windowStage.loadContent('pages/Index', this.storage);
  }

  onWindowStageDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

提供方扩展Ability入口页面文件：/src/main/ets/pages/Index.ets。

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();

  build() {
    Row() {
      Column() {
        GridRow({ columns: 2 }) {
          GridCol() {
            Button('setWindowSystemBar')
              .onClick(() => {
                this.testSetSystemBarEnable();
              }).width(120)
          }.height(60)

          GridCol() {
            Button('setGestureBack')
              .onClick(() => {
                this.testSetGestureBackEnable();
              }).width(120)
          }.height(60)

          GridCol() {
            Button('setImmersive')
              .onClick(() => {
                this.testSetImmersiveEnable();
              }).width(120)
          }.height(60)

          GridCol() {
            Button('setSpecificSystemBarEnabled')
              .onClick(() => {
                this.testSetSpecificSystemBarEnabled();
              }).width(120)
          }.height(60)
        }
      }
      .width('100%')
    }
    .height('100%')
  }

  testSetSystemBarEnable() {
    let window: window.Window | undefined = this.storage?.get('window');
    let promise = window?.setWindowSystemBarEnable(['status']);
    promise?.then(() => {
      console.info('setWindowSystemBarEnable success');
    }).catch((err: BusinessError) => {
      console.error(`setWindowSystemBarEnable failed, code: ${err.code}, message: ${err.message}`);
    });
  }

  testSetGestureBackEnable() {
    let window: window.Window | undefined = this.storage?.get('window');
    let promise = window?.setGestureBackEnabled(true);
    promise?.then(() => {
      console.info('setGestureBackEnabled success');
    }).catch((err: BusinessError) => {
      console.error(`setGestureBackEnabled failed, code: ${err.code}, message: ${err.message}`);
    });
  }

  testSetImmersiveEnable() {
    let window: window.Window | undefined = this.storage?.get('window');
    try {
      window?.setImmersiveModeEnabledState(true);
    } catch (err) {
      console.error(`setImmersiveModeEnabledState failed, code: ${err.code}, message: ${err.message}`);
    }
  }

  testSetSpecificSystemBarEnabled() {
    let window: window.Window | undefined = this.storage?.get('window');
    let promise = window?.setSpecificSystemBarEnabled('navigationIndicator', false, false);
    promise?.then(() => {
      console.info('setSpecificSystemBarEnabled success');
    }).catch((err: BusinessError) => {
      console.error(`setSpecificSystemBarEnabled failed, code: ${err.code}, message: ${err.message}`);
    });
  }
}
```
