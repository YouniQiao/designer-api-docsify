# clearAllMissions (System API)

## Modules to Import

```TypeScript
```

## clearAllMissions

```TypeScript
function clearAllMissions(callback: AsyncCallback<void>): void
```

Clears all unlocked missions. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [clearAllMissions](arkts-ability-missionmanager-clearallmissions-f-sys.md#clearallmissions-system-api)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function clearAllMissions(callback: AsyncCallback<void>): void--><!--Device-missionManager-function clearAllMissions(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Examples**

```TypeScript
import missionManager from '@ohos.application.missionManager'

try {
  missionManager.clearAllMissions(err => {
    if (err) {
      console.error('clearAllMissions failed: ${err.message}');
    } else {
      console.info('clearAllMissions successfully.');
    }
  });
} catch (err) {
  console.error('clearAllMissions failed: ${err.message}');
}
```


## clearAllMissions

```TypeScript
function clearAllMissions(): Promise<void>
```

Clears all unlocked missions. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [clearAllMissions](arkts-ability-missionmanager-clearallmissions-f-sys.md#clearallmissions-system-api)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function clearAllMissions(): Promise<void>--><!--Device-missionManager-function clearAllMissions(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

```TypeScript
import missionManager from '@ohos.application.missionManager';
import { BusinessError } from '@ohos.base';

try {
  missionManager.clearAllMissions().then((data) => {
    console.info(`clearAllMissions successfully. Data: ${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`clearAllMissions failed: ${err.message}`);
  });
} catch (err) {
  console.error(`clearAllMissions failed: ${err.message}`);
}
```
