# off (System API)

## Modules to Import

```TypeScript
import { missionManager } from 'kits/@kit.AbilityKit';
```

## off('mission')

```TypeScript
function off(type: 'mission', listenerId: number, callback: AsyncCallback<void>): void
```

Deregisters a mission status listener. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function off(type: 'mission', listenerId: long, callback: AsyncCallback<void>): void--><!--Device-missionManager-function off(type: 'mission', listenerId: long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'mission' | Yes |
| listenerId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16300002](../errorcode-ability.md#16300002-nonexistent-mission-listener) |

## Examples

```TypeScript
import { missionManager, UIAbility, AbilityConstant, common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

let listener: missionManager.MissionListener = {
  onMissionCreated: (mission: number) => {
    console.info('--------onMissionCreated-------');
  },
  onMissionDestroyed: (mission: number) => {
    console.info('--------onMissionDestroyed-------');
  },
  onMissionSnapshotChanged: (mission: number) => {
    console.info('--------onMissionSnapshotChanged-------');
  },
  onMissionMovedToFront: (mission: number) => {
    console.info('--------onMissionMovedToFront-------');
  },
  onMissionIconUpdated: (mission: number, icon: image.PixelMap) => {
    console.info('--------onMissionIconUpdated-------');
  },
  onMissionClosed: (mission: number) => {
    console.info('--------onMissionClosed-------');
  },
  onMissionLabelUpdated: (mission: number) => {
    console.info('--------onMissionLabelUpdated-------');
  }
};

let listenerId = -1;
let abilityWant: Want;
let context: common.UIAbilityContext;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info('[Demo] EntryAbility onCreate');
    abilityWant = want;
    context = this.context;
  }

  onDestroy() {
    try {
      if (listenerId !== -1) {
        missionManager.off('mission', listenerId, (error: BusinessError) => {
          if (error) {
            console.error(`MissionManager.off failed, error code: ${error.code}, error msg: ${error.message}`);
            return;
          }
          console.info(`MissionManager.off success.`);
        });
      }
    } catch (paramError) {
      let code = (paramError as BusinessError).code;
      let message = (paramError as BusinessError).message;
      console.error(`error: ${code}, ${message} `);
    }
    console.info('[Demo] EntryAbility onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    // The main window is created. Set a main page for this ability.
    console.info('[Demo] EntryAbility onWindowStageCreate');
    try {
      listenerId = missionManager.on('mission', listener);
    } catch (paramError) {
      let code = (paramError as BusinessError).code;
      let message = (paramError as BusinessError).message;
      console.error(`error: ${code}, ${message} `);
    }

    windowStage.loadContent('pages/index', (err: BusinessError, data) => {
      if (err.code) {
        console.error(`Failed to load the content. Cause: ${JSON.stringify(err)}`);
        return;
      }
      console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}`);
    });
  }
}
```


## off('mission')

```TypeScript
function off(type: 'mission', listenerId: number): Promise<void>
```

Unregisters a mission status listener. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function off(type: 'mission', listenerId: long): Promise<void>--><!--Device-missionManager-function off(type: 'mission', listenerId: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'mission' | Yes |
| listenerId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16300002](../errorcode-ability.md#16300002-nonexistent-mission-listener) |

## Examples

```TypeScript
import { missionManager, UIAbility, AbilityConstant, common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

let listener: missionManager.MissionListener = {
  onMissionCreated: (mission: number) => {
    console.info('--------onMissionCreated-------');
  },
  onMissionDestroyed: (mission: number) => {
    console.info('--------onMissionDestroyed-------');
  },
  onMissionSnapshotChanged: (mission: number) => {
    console.info('--------onMissionSnapshotChanged-------');
  },
  onMissionMovedToFront: (mission: number) => {
    console.info('--------onMissionMovedToFront-------');
  },
  onMissionIconUpdated: (mission: number, icon: image.PixelMap) => {
    console.info('--------onMissionIconUpdated-------');
  },
  onMissionClosed: (mission: number) => {
    console.info('--------onMissionClosed-------');
  },
  onMissionLabelUpdated: (mission: number) => {
    console.info('--------onMissionLabelUpdated-------');
  }
};

let listenerId = -1;
let abilityWant: Want;
let context: common.UIAbilityContext;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info('[Demo] EntryAbility onCreate');
    abilityWant = want;
    context = this.context;
  }

  onDestroy() {
    try {
      if (listenerId !== -1) {
        missionManager.off('mission', listenerId).catch((error: BusinessError) => {
          console.error(`MissionManager.off failed, error code: ${error.code}, error msg: ${error.message}.`);
        });
      }
    } catch (paramError) {
      let code = (paramError as BusinessError).code;
      let message = (paramError as BusinessError).message;
      console.error(`error: ${code}, ${message} `);
    }
    console.info('[Demo] EntryAbility onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    // The main window is created. Set a main page for this ability.
    console.info('[Demo] EntryAbility onWindowStageCreate');
    try {
      listenerId = missionManager.on('mission', listener);
    } catch (paramError) {
      let code = (paramError as BusinessError).code;
      let message = (paramError as BusinessError).message;
      console.error(`error: ${code}, ${message} `);
    }

    windowStage.loadContent('pages/index', (err: BusinessError, data) => {
      if (err.code) {
        console.error(`Failed to load the content. Cause: ${JSON.stringify(err)}`);
        return;
      }
      console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}`);
    });
  }
}
```


## off('missionEvent')

```TypeScript
function off(type: 'missionEvent', listenerId: number, callback: AsyncCallback<void>): void
```

Deregisters a mission status listener. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** missionManager#off(type:

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function off(type: 'missionEvent', listenerId: long, callback: AsyncCallback<void>): void--><!--Device-missionManager-function off(type: 'missionEvent', listenerId: long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'missionEvent' | Yes |
| listenerId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16300002](../errorcode-ability.md#16300002-nonexistent-mission-listener) |


## off('missionEvent')

```TypeScript
function off(type: 'missionEvent', listenerId: number): Promise<void>
```

Unregisters a mission status listener. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** missionManager#off(type:

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function off(type: 'missionEvent', listenerId: long): Promise<void>--><!--Device-missionManager-function off(type: 'missionEvent', listenerId: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'missionEvent' | Yes |
| listenerId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16300002](../errorcode-ability.md#16300002-nonexistent-mission-listener) |
