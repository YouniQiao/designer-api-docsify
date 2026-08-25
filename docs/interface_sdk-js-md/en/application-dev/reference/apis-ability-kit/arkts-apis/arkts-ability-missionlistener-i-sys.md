# MissionListener (System API)

The module defines the listeners used to observe the mission status. The listeners can be registered by using [on](arkts-ability-missionmanager-on-f-sys.md).

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## onMissionClosed

ArkTS-Dyn:
```TypeScript
onMissionClosed(mission: number): void
```

ArkTS-Sta:
```TypeScript
onMissionClosed(mission: int): void
```

Called when the system closes a mission.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mission | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |

**Examples**

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let listener: missionManager.MissionListener = {
  onMissionCreated: (mission) => {
    console.info(`onMissionCreated mission: ${JSON.stringify(mission)}`);
  },
  onMissionDestroyed: (mission) => {
    console.info(`onMissionDestroyed mission: ${JSON.stringify(mission)}`);
  },
  onMissionSnapshotChanged: (mission) => {
    console.info(`onMissionSnapshotChanged mission: ${JSON.stringify(mission)}`);
  },
  onMissionMovedToFront: (mission) => {
    console.info(`onMissionMovedToFront mission: ${JSON.stringify(mission)}`);
  },
  onMissionLabelUpdated: (mission) => {
    console.info(`onMissionLabelUpdated mission: ${JSON.stringify(mission)}`);
  },
  onMissionIconUpdated: (mission, icon) => {
    console.info(`onMissionIconUpdated mission: ${JSON.stringify(mission)}`);
    console.info(`onMissionIconUpdated icon: ${JSON.stringify(icon)}`);
  },
  onMissionClosed: (mission) => {
    console.info(`onMissionClosed mission: ${JSON.stringify(mission)}`);
  }
};

try {
  let listenerId = missionManager.on('mission', listener);
} catch (paramError) {
  console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
}
```

## onMissionCreated

ArkTS-Dyn:
```TypeScript
onMissionCreated(mission: number): void
```

ArkTS-Sta:
```TypeScript
onMissionCreated(mission: int): void
```

Called when the system creates a mission.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mission | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |

**Examples**

For details, see [onMissionClosed](#onmissionclosed).

## onMissionDestroyed

ArkTS-Dyn:
```TypeScript
onMissionDestroyed(mission: number): void
```

ArkTS-Sta:
```TypeScript
onMissionDestroyed(mission: int): void
```

Called when the system destroys a mission.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mission | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |

**Examples**

For details, see [onMissionClosed](#onmissionclosed).

## onMissionIconUpdated

ArkTS-Dyn:
```TypeScript
onMissionIconUpdated(mission: number, icon: image.PixelMap): void
```

ArkTS-Sta:
```TypeScript
onMissionIconUpdated(mission: int, icon: image.PixelMap): void
```

Called when the system updates the icon of a mission.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mission | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |
| icon | image.PixelMap | Yes |

**Examples**

For details, see [onMissionClosed](#onmissionclosed).

## onMissionLabelUpdated

ArkTS-Dyn:
```TypeScript
onMissionLabelUpdated(mission: number): void
```

ArkTS-Sta:
```TypeScript
onMissionLabelUpdated(mission: int): void
```

Called when the system updates the label of a mission.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mission | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |

**Examples**

For details, see [onMissionClosed](#onmissionclosed).

## onMissionMovedToFront

ArkTS-Dyn:
```TypeScript
onMissionMovedToFront(mission: number): void
```

ArkTS-Sta:
```TypeScript
onMissionMovedToFront(mission: int): void
```

Called when the system moves a mission to the foreground.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mission | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |

**Examples**

For details, see [onMissionClosed](#onmissionclosed).

## onMissionSnapshotChanged

ArkTS-Dyn:
```TypeScript
onMissionSnapshotChanged(mission: number): void
```

ArkTS-Sta:
```TypeScript
onMissionSnapshotChanged(mission: int): void
```

Called when the system updates the snapshot of a mission.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mission | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |

**Examples**

For details, see [onMissionClosed](#onmissionclosed).
