# on (System API)

## Modules to Import

```TypeScript
import { missionManager } from 'kits/@kit.AbilityKit';
```

## on('mission')

```TypeScript
function on(type: 'mission', listener: MissionListener): number
```

Registers a listener to observe the mission status.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function on(type: 'mission', listener: MissionListener): long--><!--Device-missionManager-function on(type: 'mission', listener: MissionListener): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'mission' | Yes |
| listener | [MissionListener](arkts-ability-missionmanager-missionlistener-t-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { missionManager, UIAbility, AbilityConstant, common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

let listener: missionManager.MissionListener = {
  onMissionCreated: (mission: number) => {console.info('--------onMissionCreated-------');},
  onMissionDestroyed: (mission: number) => {console.info('--------onMissionDestroyed-------');},
  onMissionSnapshotChanged: (mission: number) => {console.info('--------onMissionSnapshotChanged-------');},
  onMissionMovedToFront: (mission: number) => {console.info('--------onMissionMovedToFront-------');},
  onMissionIconUpdated: (mission: number, icon: image.PixelMap) => {console.info('--------onMissionIconUpdated-------');},
  onMissionClosed: (mission: number) => {console.info('--------onMissionClosed-------');},
  onMissionLabelUpdated: (mission: number) => {console.info('--------onMissionLabelUpdated-------');}
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
          console.info(JSON.stringify(error));
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

    windowStage.loadContent('pages/index', (err, data) => {
      if (err.code) {
        console.error(`Failed to load the content. Cause: ${JSON.stringify(err)}`);
        return;
      }
      console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}`);
    });
  }
}
```


## on('missionEvent')

```TypeScript
function on(type: 'missionEvent', listener: MissionListener): number
```

Registers a listener to observe the mission status.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** missionManager#on(type:

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function on(type: 'missionEvent', listener: MissionListener): long--><!--Device-missionManager-function on(type: 'missionEvent', listener: MissionListener): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'missionEvent' | Yes |
| listener | [MissionListener](arkts-ability-missionmanager-missionlistener-t-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
