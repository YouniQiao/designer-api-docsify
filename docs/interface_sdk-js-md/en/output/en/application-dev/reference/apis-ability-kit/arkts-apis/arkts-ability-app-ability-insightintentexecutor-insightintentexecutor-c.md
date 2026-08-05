# InsightIntentExecutor

The module provides the base class for intent execution. You can use this module to interface with the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ on the device side and implement intent service logic through \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ . In addition to developing intents via configuration files, intents can also be developed using decorators. For API version 20 and later, you are advised to \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class InsightIntentExecutor--><!--Device-unnamed-declare class InsightIntentExecutor-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onExecuteInServiceExtensionAbility

```TypeScript
onExecuteInServiceExtensionAbility(name: string, param: Record<string, Object>):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

Called during the ServiceExtensionAbility lifecycle when the ServiceExtensionAbility that the intent execution depends on is started. Both synchronous calls and asynchronous calls using Promise are supported. - The ServiceExtensionAbility lifecycle callbacks are triggered in the following sequence during intent execution: **onCreate**, **onRequest**, and **onExecuteInServiceExtensionAbility**.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentExecutor-onExecuteInServiceExtensionAbility(name: string, param: Record<string, Object>):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>--><!--Device-InsightIntentExecutor-onExecuteInServiceExtensionAbility(name: string, param: Record<string, Object>):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Intent name. |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, Object&gt; | Yes | Intent parameter, which is the data passed from the system entry point to the application for this intent execution. |

**Return value:**

| Type | Description |
| --- | --- |
| insightIntent.ExecuteResult | Intent execution result or a Promise |

**Example**

The code snippet below shows the synchronous call that returns the intent execution result:

```TypeScript
import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class IntentExecutorImpl extends InsightIntentExecutor {
  onExecuteInServiceExtensionAbility(name: string, param: Record<string, Object>): insightIntent.ExecuteResult {
    let result: insightIntent.ExecuteResult;
    if (name !== 'SupportedInsightIntentName') {
      hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
      result = {
        // decided by developer
        code: 404,
        result: {
          message: 'Unsupported insight intent.',
        }
      };
      return result;
    }

    result = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    return result;
  }
}
```

The code snippet below shows the promise-based asynchronous call that returns the intent execution result:

```TypeScript
import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function executeInsightIntent(param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
  return new Promise((resolve, reject) => {
    let result: insightIntent.ExecuteResult = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    resolve(result);
  });
}

export default class IntentExecutorImpl extends InsightIntentExecutor {
  // Use the async/await syntax to implement an asynchronous API. The async keyword declares that the API is asynchronous.
  async onExecuteInServiceExtensionAbility(name: string,
    param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
    let result: insightIntent.ExecuteResult;
    if (name !== 'SupportedInsightIntentName') {
      hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
      result = {
        // decided by developer
        code: 404,
        result: {
          message: 'Unsupported insight intent.',
        }
      };
      return result;
    }

    result = await executeInsightIntent(param);
    return result;
  }
}
```

## onExecuteInServiceExtensionAbility

```TypeScript
onExecuteInServiceExtensionAbility(name: string, param: Record<string, RecordData>):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

Called during the ServiceExtensionAbility lifecycle when the ServiceExtensionAbility that the intent execution depends on is started. Both synchronous calls and asynchronous calls using Promise are supported. - The ServiceExtensionAbility lifecycle callbacks are triggered in the following sequence during intent execution: **onCreate**, **onRequest**, and **onExecuteInServiceExtensionAbility**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentExecutor-onExecuteInServiceExtensionAbility(name: string, param: Record<string, RecordData>):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>--><!--Device-InsightIntentExecutor-onExecuteInServiceExtensionAbility(name: string, param: Record<string, RecordData>):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | InsightIntent name. |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, RecordData&gt; | Yes | InsightIntent call parameter. |

**Return value:**

| Type | Description |
| --- | --- |
| insightIntent.ExecuteResult | Intent execution result or a Promise |

## onExecuteInUIAbilityBackgroundMode

```TypeScript
onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, Object>):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

Called during the UIAbility lifecycle when the [UIAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ that the intent execution depends on is started in the background. Both synchronous calls and asynchronous calls using Promise are supported. - If the UIAbility is cold started, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onCreate]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, onExecuteInUIAbilityBackgroundMode, and [onBackground]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_. - If the UIAbility is hot started, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: onExecuteInUIAbilityBackgroundMode.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-InsightIntentExecutor-onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, Object>):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>--><!--Device-InsightIntentExecutor-onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, Object>):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Intent name. |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, Object&gt; | Yes | Intent parameter, which is the data passed from the system entry point to the application for this intent execution. |

**Return value:**

| Type | Description |
| --- | --- |
| insightIntent.ExecuteResult | Intent execution result or a Promise |

**Example**

The code snippet below shows the synchronous call that returns the intent execution result:

```TypeScript
import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';

export default class IntentExecutorImpl extends InsightIntentExecutor {
  onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, Object>): insightIntent.ExecuteResult {
    let result: insightIntent.ExecuteResult = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    return result;
  }
}
```

The code snippet below shows the promise-based asynchronous call that returns the intent execution result:

```TypeScript
import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';

async function executeInsightIntent(param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
  return new Promise((resolve, reject) => {
    let result: insightIntent.ExecuteResult = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    resolve(result);
  })
}

export default class IntentExecutorImpl extends InsightIntentExecutor {
  // Use the async/await syntax to implement an asynchronous API. The async keyword declares that the API is asynchronous.
  async onExecuteInUIAbilityBackgroundMode(name: string,
    param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
    let result: insightIntent.ExecuteResult = await executeInsightIntent(param);
    return result;
  }
}
```

## onExecuteInUIAbilityBackgroundMode

```TypeScript
onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, RecordData>):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

Called during the UIAbility lifecycle when the [UIAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ that the intent execution depends on is started in the background. Both synchronous calls and asynchronous calls using Promise are supported. - If the UIAbility is cold started, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onCreate]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, onExecuteInUIAbilityBackgroundMode, and [onBackground]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_. - If the UIAbility is hot started, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: onExecuteInUIAbilityBackgroundMode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentExecutor-onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, RecordData>):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>--><!--Device-InsightIntentExecutor-onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, RecordData>):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | InsightIntent name. |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, RecordData&gt; | Yes | InsightIntent call parameter. |

**Return value:**

| Type | Description |
| --- | --- |
| insightIntent.ExecuteResult | Intent execution result or a Promise |

## onExecuteInUIAbilityForegroundMode

```TypeScript
onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

Called during the UIAbility lifecycle when the [UIAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ that the intent execution depends on is started in the foreground. Both synchronous calls and asynchronous calls using Promise are supported. - If the UIAbility is cold started, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onCreate]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, [onWindowStageCreate]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, onExecuteInUIAbilityForegroundMode, and [onForeground]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_. - If the UIAbility is hot started in the background, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onNewWant]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_, onExecuteInUIAbilityForegroundMode, and [onForeground]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_. - If the UIAbility is hot started in the foreground, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: onExecuteInUIAbilityForegroundMode.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-InsightIntentExecutor-onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>--><!--Device-InsightIntentExecutor-onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Intent name. |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, Object&gt; | Yes | Intent parameter, which is the data passed from the system entry point to the application for this intent execution. |
| pageLoader | window.WindowStage | Yes | WindowStage instance, which is the same as the WindowStage instance in the [onWindowStageCreate]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ API and can be used to load the page for intent execution. |

**Return value:**

| Type | Description |
| --- | --- |
| insightIntent.ExecuteResult | Intent execution result or a Promise |

**Example**

The code snippet below shows the synchronous call that returns the intent execution result:

```TypeScript
import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class IntentExecutorImpl extends InsightIntentExecutor {
  onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>,
    pageLoader: window.WindowStage): insightIntent.ExecuteResult {
    let result: insightIntent.ExecuteResult;
    if (name !== 'SupportedInsightIntentName') {
      hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
      result = {
        // decided by developer
        code: 404,
        result: {
          message: 'Unsupported insight intent.',
        }
      };
      return result;
    }

    // if developer need load intent content, 'pages/IntentPage' is intent page.
    pageLoader.loadContent('pages/IntentPage', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
      } else {
        hilog.info(0x0000, 'testTag', '%{public}s', 'Succeeded in loading the content');
      }
    });

    result = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    return result;
  }
}
```

The code snippet below shows the promise-based asynchronous call that returns the intent execution result:

```TypeScript
import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function executeInsightIntent(param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
  return new Promise((resolve, reject) => {
    let result: insightIntent.ExecuteResult = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    resolve(result);
  })
}

export default class IntentExecutorImpl extends InsightIntentExecutor {
  // Use the async/await syntax to implement an asynchronous API. The async keyword declares that the API is asynchronous.
  async onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>,
    pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
    let result: insightIntent.ExecuteResult;
    if (name !== 'SupportedInsightIntentName') {
      hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
      result = {
        // decided by developer
        code: 404,
        result: {
          message: 'Unsupported insight intent.',
        }
      };
      return result;
    }

    result = await executeInsightIntent(param);
    return result;
  }
}
```

## onExecuteInUIAbilityForegroundMode

```TypeScript
onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, RecordData>, pageLoader: window.WindowStage):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

Called during the UIAbility lifecycle when the [UIAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ that the intent execution depends on is started in the foreground. Both synchronous calls and asynchronous calls using Promise are supported. - If the UIAbility is cold started, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onCreate]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, [onWindowStageCreate]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, onExecuteInUIAbilityForegroundMode, and [onForeground]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_. - If the UIAbility is hot started in the background, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onNewWant]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_, onExecuteInUIAbilityForegroundMode, and [onForeground]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_. - If the UIAbility is hot started in the foreground, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: onExecuteInUIAbilityForegroundMode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentExecutor-onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, RecordData>, pageLoader: window.WindowStage):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>--><!--Device-InsightIntentExecutor-onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, RecordData>, pageLoader: window.WindowStage):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | InsightIntent name. |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, RecordData&gt; | Yes | InsightIntent call parameter. |
| pageLoader | window.WindowStage | Yes | Page loader. |

**Return value:**

| Type | Description |
| --- | --- |
| insightIntent.ExecuteResult | Intent execution result or a Promise |

## onExecuteInUIExtensionAbility

```TypeScript
onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>, pageLoader: UIExtensionContentSession):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

Called during the UIExtensionAbility lifecycle when the [UIExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ that the intent execution depends on is started. Both synchronous calls and asynchronous calls using Promise are supported. - The UIExtensionAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onCreate]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, [onSessionCreate]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, onExecuteInUIExtensionAbility, and [onForeground]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentExecutor-onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>, pageLoader: UIExtensionContentSession):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>--><!--Device-InsightIntentExecutor-onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>, pageLoader: UIExtensionContentSession):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Intent name. |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, Object&gt; | Yes | Intent parameter, which is the data passed from the system entry point to the application for this intent execution. |
| pageLoader | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | UIExtensionContentSession instance, which is the same as the UIExtensionContentSession instance in the [onSessionCreate]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ API and can be used to load the page for intent execution. |

**Return value:**

| Type | Description |
| --- | --- |
| insightIntent.ExecuteResult | Intent execution result or a Promise |

**Example**

The code snippet below shows the synchronous call that returns the intent execution result:

```TypeScript
import { InsightIntentExecutor, insightIntent, UIExtensionContentSession } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class IntentExecutorImpl extends InsightIntentExecutor {
  onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>,
    pageLoader: UIExtensionContentSession): insightIntent.ExecuteResult {
    let result: insightIntent.ExecuteResult;
    if (name !== 'SupportedInsightIntentName') {
      hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
      result = {
        // decided by developer
        code: 404,
        result: {
          message: 'Unsupported insight intent.',
        }
      };
      return result;
    }

    // if developer need load intent content, 'pages/IntentPage' is intent page.
    pageLoader.loadContent('pages/Index');

    result = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    return result;
  }
}
```

The code snippet below shows the promise-based asynchronous call that returns the intent execution result:

```TypeScript
import { InsightIntentExecutor, insightIntent, UIExtensionContentSession } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function executeInsightIntent(param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
  return new Promise((resolve, reject) => {
    let result: insightIntent.ExecuteResult = {
      code: 0,
      result: {
        message: 'Execute insight intent succeed.',
      }
    };
    resolve(result);
  })
}

export default class IntentExecutorImpl extends InsightIntentExecutor {
  // Use the async/await syntax to implement an asynchronous API. The async keyword declares that the API is asynchronous.
  async onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>,
    pageLoader: UIExtensionContentSession): Promise<insightIntent.ExecuteResult> {
    let result: insightIntent.ExecuteResult;
    if (name !== 'SupportedInsightIntentName') {
      hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
      result = {
        // decided by developer
        code: 404,
        result: {
          message: 'Unsupported insight intent.',
        }
      };
      return result;
    }

    result = await executeInsightIntent(param);
    return result;
  }
}
```

## onExecuteInUIExtensionAbility

```TypeScript
onExecuteInUIExtensionAbility(name: string, param: Record<string, RecordData>, pageLoader: UIExtensionContentSession):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

Called during the UIExtensionAbility lifecycle when the [UIExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ that the intent execution depends on is started. Both synchronous calls and asynchronous calls using Promise are supported. - The UIExtensionAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onCreate]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, [onSessionCreate]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, onExecuteInUIExtensionAbility, and [onForeground]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentExecutor-onExecuteInUIExtensionAbility(name: string, param: Record<string, RecordData>, pageLoader: UIExtensionContentSession):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>--><!--Device-InsightIntentExecutor-onExecuteInUIExtensionAbility(name: string, param: Record<string, RecordData>, pageLoader: UIExtensionContentSession):    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | InsightIntent name. |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, RecordData&gt; | Yes | InsightIntent call parameter. |
| pageLoader | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Page loader. |

**Return value:**

| Type | Description |
| --- | --- |
| insightIntent.ExecuteResult | Intent execution result or a Promise |

## context

```TypeScript
context: InsightIntentContext
```

Context for intent execution.

**Type:** InsightIntentContext

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-InsightIntentExecutor-context: InsightIntentContext--><!--Device-InsightIntentExecutor-context: InsightIntentContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

