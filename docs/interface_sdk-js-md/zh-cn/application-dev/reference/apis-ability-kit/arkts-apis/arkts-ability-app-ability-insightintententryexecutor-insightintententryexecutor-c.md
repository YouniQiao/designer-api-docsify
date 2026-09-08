# InsightIntentEntryExecutor

本模块提供[@InsightIntentEntry](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintententry)装饰器的意图执行基类，必须与@InsightIntentEntry装饰器联合使用。开发者需要在继承该基类的子类中，实现[onExecute()](#onexecute)意图执行回调，并使用@ InsightIntentEntry装饰器来装饰子类。

**起始版本：** 20

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { InsightIntentEntryExecutor } from '@kit.AbilityKit';
```

## onExecute

```TypeScript
onExecute(): Promise<insightIntent.IntentResult<T>>
```

当AI入口触发意图执行时，系统拉起绑定的Ability组件，触发回调，开发者在此实现意图操作。使用Promise异步回调。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;insightIntent.IntentResult&lt;T&gt;&gt; | Promise对象。返回[insightIntent.IntentResult&lt;T&gt;]{ |

**示例**

```TypeScript
import { insightIntent, InsightIntentEntry, InsightIntentEntryExecutor } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const LOG_TAG: string = 'testTag-EntryIntent';

// 使用@InsightIntentEntry装饰器定义意图
@InsightIntentEntry({
  intentName: 'PlayMusic',
  domain: 'MusicDomain',
  intentVersion: '1.0.1',
  displayName: '播放歌曲',
  displayDescription: '播放音乐意图',
  icon: $r('app.media.app_icon'), // $r表示本地图标，需要在资源目录中定义
  llmDescription: '支持传递歌曲名称，播放音乐',
  keywords: ['音乐播放', '播放歌曲', 'PlayMusic'],
  abilityName: 'EntryAbility',
  executeMode: [insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND],
  parameters: {
    'schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'title': 'Song Schema',
    'description': 'A schema for describing songs and their artists',
    'properties': {
      'songName': {
        'type': 'string',
        'description': 'The name of the song',
        'minLength': 1
      }
    },
    'required': ['songName']
  }
})
export default class PlayMusicDemo extends InsightIntentEntryExecutor<string> {
  songName: string = '';

  onExecute(): Promise<insightIntent.IntentResult<string>> {
    hilog.info(0x0000, LOG_TAG, 'PlayMusicDemo executeMode %{public}s', JSON.stringify(this.executeMode));
    hilog.info(0x0000, LOG_TAG, '%{public}s', JSON.stringify(this));
    let storage = new LocalStorage();
    storage.setOrCreate('songName', this.songName);
    // 根据executeMode参数的不同情况，提供不同拉起PlayMusicPage页面的方式。
    if (this.executeMode == insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND) {
      this.windowStage?.loadContent('pages/PlayMusicPage', storage);
    } else if (this.executeMode == insightIntent.ExecuteMode.UI_EXTENSION_ABILITY) {
      this.uiExtensionSession?.loadContent('pages/PlayMusicPage', storage);
    }
    // 定义意图的执行结果
    let result: insightIntent.IntentResult<string> = {
      code: 123,
      result: 'result'
    };
    hilog.info(0x0000, LOG_TAG, 'PlayMusicDemo return %{public}s', JSON.stringify(result));
    // 以Promise的方式返回意图执行结果
    return Promise.reject(result);
  }
}
```

## context

```TypeScript
context: InsightIntentContext
```

表示意图执行上下文。

**类型：** [InsightIntentContext](arkts-ability-app-ability-insightintentcontext-insightintentcontext-c.md)

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## executeMode

```TypeScript
executeMode: insightIntent.ExecuteMode
```

表示意图执行模式。即拉起绑定的Ability组件时支持的执行模式。

**类型：** insightIntent.ExecuteMode

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## uiExtensionSession

```TypeScript
uiExtensionSession?: UIExtensionContentSession
```

表示UIExtensionContentSession实例对象，和[onSessionCreate](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#onsessioncreate)接口的UIExtensionContentSession实例是同一个，可用于加载意图执行的页面。仅当executeMode字段取值为UI_EXTENSION_ABILITY（即意图执行需要拉起UIExtensionAbility时），该属性生效。

**类型：** [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md)

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## windowStage

```TypeScript
windowStage?: window.WindowStage
```

表示windowStage实例对象，和[onWindowStageCreate](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate)接口的windowStage实例是同一个，可用于加载意图执行的页面。仅当executeMode字段取值为UI_ABILITY_FOREGROUND（即意图执行需要将UIAbility显示在前台时），该属性生效。

**类型：** window.WindowStage

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
