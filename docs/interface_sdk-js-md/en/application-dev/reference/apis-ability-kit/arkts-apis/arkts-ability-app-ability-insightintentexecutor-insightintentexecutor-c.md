# InsightIntentExecutor

The module provides the base class for intent execution. You can use this module to interface with the [InsightIntent framework](../../../application-models/insight-intent-overview.md) on the device side and implement intent service logic through [configuration files](../../../application-models/insight-intent-config-development.md). In addition to developing intents via configuration files, intents can also be developed using decorators. For API version 20 and later, you are advised to [develop intents using decorators](../../../application-models/insight-intent-decorator-development.md).

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { InsightIntentExecutor } from '@kit.AbilityKit';
```

## onExecuteInServiceExtensionAbility

```TypeScript
onExecuteInServiceExtensionAbility(name: string, param: Record<string, Object>):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

Called during the ServiceExtensionAbility lifecycle when the ServiceExtensionAbility that the intent execution depends on is started. Both synchronous calls and asynchronous calls using Promise are supported.  
- The ServiceExtensionAbility lifecycle callbacks are triggered in the following sequence during intent execution: **onCreate**, **onRequest**, and **onExecuteInServiceExtensionAbility**.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| param | Record & lt;string, Object & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| insightIntent.ExecuteResult \| Promise & lt;insightIntent.ExecuteResult & gt; |

**Examples**

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

Called during the ServiceExtensionAbility lifecycle when the ServiceExtensionAbility that the intent execution depends on is started. Both synchronous calls and asynchronous calls using Promise are supported.  
- The ServiceExtensionAbility lifecycle callbacks are triggered in the following sequence during intent execution: **onCreate**, **onRequest**, and **onExecuteInServiceExtensionAbility**.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| param | Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| insightIntent.ExecuteResult \| Promise & lt;insightIntent.ExecuteResult & gt; |

**Examples**

See [onExecuteInServiceExtensionAbility](#onexecuteinserviceextensionability)

## onExecuteInUIAbilityBackgroundMode

```TypeScript
onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, Object>):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

Called during the UIAbility lifecycle when the [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) that the intent execution depends on is started in the background. Both synchronous calls and asynchronous calls using Promise are supported.  
- If the UIAbility is cold started, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onCreate](arkts-ability-app-ability-uiability-uiability-c.md#oncreate), onExecuteInUIAbilityBackgroundMode, and [onBackground](arkts-ability-app-ability-uiability-uiability-c.md#onbackground). - If the UIAbility is hot started, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: onExecuteInUIAbilityBackgroundMode.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| param | Record & lt;string, Object & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| insightIntent.ExecuteResult \| Promise & lt;insightIntent.ExecuteResult & gt; |

**Examples**

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

Called during the UIAbility lifecycle when the [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) that the intent execution depends on is started in the background. Both synchronous calls and asynchronous calls using Promise are supported.  
- If the UIAbility is cold started, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onCreate](arkts-ability-app-ability-uiability-uiability-c.md#oncreate), onExecuteInUIAbilityBackgroundMode, and [onBackground](arkts-ability-app-ability-uiability-uiability-c.md#onbackground). - If the UIAbility is hot started, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: onExecuteInUIAbilityBackgroundMode.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| param | Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| insightIntent.ExecuteResult \| Promise & lt;insightIntent.ExecuteResult & gt; |

**Examples**

See [onExecuteInUIAbilityBackgroundMode](#onexecuteinuiabilitybackgroundmode)

## onExecuteInUIAbilityForegroundMode

```TypeScript
onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

Called during the UIAbility lifecycle when the [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) that the intent execution depends on is started in the foreground. Both synchronous calls and asynchronous calls using Promise are supported.  
- If the UIAbility is cold started, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onCreate](arkts-ability-app-ability-uiability-uiability-c.md#oncreate), [onWindowStageCreate](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate), onExecuteInUIAbilityForegroundMode, and [onForeground](arkts-ability-app-ability-uiability-uiability-c.md#onforeground). - If the UIAbility is hot started in the background, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onNewWant](arkts-ability-app-ability-uiability-uiability-c.md#onnewwant), onExecuteInUIAbilityForegroundMode, and [onForeground](arkts-ability-app-ability-uiability-uiability-c.md#onforeground). - If the UIAbility is hot started in the foreground, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: onExecuteInUIAbilityForegroundMode.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| param | Record & lt;string, Object & gt; | Yes |
| pageLoader | window.WindowStage | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| insightIntent.ExecuteResult \| Promise & lt;insightIntent.ExecuteResult & gt; |

**Examples**

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

Called during the UIAbility lifecycle when the [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) that the intent execution depends on is started in the foreground. Both synchronous calls and asynchronous calls using Promise are supported.  
- If the UIAbility is cold started, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onCreate](arkts-ability-app-ability-uiability-uiability-c.md#oncreate), [onWindowStageCreate](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate), onExecuteInUIAbilityForegroundMode, and [onForeground](arkts-ability-app-ability-uiability-uiability-c.md#onforeground). - If the UIAbility is hot started in the background, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onNewWant](arkts-ability-app-ability-uiability-uiability-c.md#onnewwant), onExecuteInUIAbilityForegroundMode, and [onForeground](arkts-ability-app-ability-uiability-uiability-c.md#onforeground). - If the UIAbility is hot started in the foreground, the UIAbility lifecycle callbacks are triggered in the following sequence during intent execution: onExecuteInUIAbilityForegroundMode.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| param | Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes |
| pageLoader | window.WindowStage | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| insightIntent.ExecuteResult \| Promise & lt;insightIntent.ExecuteResult & gt; |

**Examples**

See [onExecuteInUIAbilityForegroundMode](#onexecuteinuiabilityforegroundmode)

## onExecuteInUIExtensionAbility

```TypeScript
onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>, pageLoader: UIExtensionContentSession):
    insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>
```

Called during the UIExtensionAbility lifecycle when the [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md) that the intent execution depends on is started. Both synchronous calls and asynchronous calls using Promise are supported.  
- The UIExtensionAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onCreate](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#oncreate), [onSessionCreate](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#onsessioncreate), onExecuteInUIExtensionAbility, and [onForeground](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#onforeground).

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| param | Record & lt;string, Object & gt; | Yes |
| pageLoader | [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| insightIntent.ExecuteResult \| Promise & lt;insightIntent.ExecuteResult & gt; |

**Examples**

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

Called during the UIExtensionAbility lifecycle when the [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md) that the intent execution depends on is started. Both synchronous calls and asynchronous calls using Promise are supported.  
- The UIExtensionAbility lifecycle callbacks are triggered in the following sequence during intent execution: [onCreate](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#oncreate), [onSessionCreate](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#onsessioncreate), onExecuteInUIExtensionAbility, and [onForeground](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#onforeground).

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| param | Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes |
| pageLoader | [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| insightIntent.ExecuteResult \| Promise & lt;insightIntent.ExecuteResult & gt; |

**Examples**

See [onExecuteInUIExtensionAbility](#onexecuteinuiextensionability)

## context

```TypeScript
context: InsightIntentContext
```

Context for intent execution.

**Type:** [InsightIntentContext](arkts-ability-app-ability-insightintentcontext-insightintentcontext-c.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
