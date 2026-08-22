# InsightIntentEntryExecutor

The class of insight intent entry executor.

@class InsightIntentEntryExecutor&lt;T&gt;

**Since:** 26.0.0

<!--Device-unnamed-declare class InsightIntentEntryExecutor--><!--Device-unnamed-declare class InsightIntentEntryExecutor-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { InsightIntentEntryExecutor } from '@kit.AbilityKit';
```

## onExecute

```TypeScript
onExecute(): Promise<insightIntent.IntentResult<T>>
```

Called when insight intent execute.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-InsightIntentEntryExecutor-onExecute(): Promise<insightIntent.IntentResult<T>>--><!--Device-InsightIntentEntryExecutor-onExecute(): Promise<insightIntent.IntentResult<T>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;insightIntent.IntentResult&lt;T&gt;&gt; | The result of insight intent execution, support promise. |

**Examples**

```TypeScript
import { insightIntent, InsightIntentEntry, InsightIntentEntryExecutor } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const LOG_TAG: string = 'testTag-EntryIntent';

// Use the @InsightIntentEntry decorator to define an intent.
@InsightIntentEntry({
  intentName: 'PlayMusic',
  domain: 'MusicDomain',
  intentVersion: '1.0.1',
  displayName: 'Play Music',
  displayDescription: 'Intent to play music',
  icon: $r('app.media.app_icon'), // $r indicates a local icon, which must be defined in the resource catalog.
  llmDescription: 'Supports passing song names to play music',
  keywords: ['music playback', 'play music', 'PlayMusic'],
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
    // Start the PlayMusicPage page based on the executeMode parameter.
    if (this.executeMode == insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND) {
      this.windowStage?.loadContent('pages/PlayMusicPage', storage);
    } else if (this.executeMode == insightIntent.ExecuteMode.UI_EXTENSION_ABILITY) {
      this.uiExtensionSession?.loadContent('pages/PlayMusicPage', storage);
    }
    // Define the intent execution result.
    let result: insightIntent.IntentResult<string> = {
      code: 123,
      result: 'result'
    }
    hilog.info(0x0000, LOG_TAG, 'PlayMusicDemo return %{public}s', JSON.stringify(result));
    // Return the intent execution result in Promise mode.
    return Promise.reject(result);
  }
}
```

## context

```TypeScript
context: InsightIntentContext
```

The insight intent context.

**Type:** [InsightIntentContext](arkts-ability-app-ability-insightintentcontext-insightintentcontext-c.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-InsightIntentEntryExecutor-context: InsightIntentContext--><!--Device-InsightIntentEntryExecutor-context: InsightIntentContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## executeMode

```TypeScript
executeMode: insightIntent.ExecuteMode
```

The insight intent execute mode.

**Type:** insightIntent.ExecuteMode

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-InsightIntentEntryExecutor-executeMode: insightIntent.ExecuteMode--><!--Device-InsightIntentEntryExecutor-executeMode: insightIntent.ExecuteMode-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uiExtensionSession

```TypeScript
uiExtensionSession?: UIExtensionContentSession
```

The UIExtension content session.

**Type:** [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-InsightIntentEntryExecutor-uiExtensionSession?: UIExtensionContentSession--><!--Device-InsightIntentEntryExecutor-uiExtensionSession?: UIExtensionContentSession-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## windowStage

```TypeScript
windowStage?: window.WindowStage
```

The window stage.

**Type:** window.WindowStage

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-InsightIntentEntryExecutor-windowStage?: window.WindowStage--><!--Device-InsightIntentEntryExecutor-windowStage?: window.WindowStage-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

