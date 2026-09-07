# MissionListener (System API)

The module defines the listeners used to observe the mission status. The listeners can be registered by using [on](arkts-ability-missionmanager-on-f-sys.md).

**Since:** 8

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## onMissionClosed

```TypeScript
onMissionClosed(mission: number): void
```

Called when the system closes a mission.

**Since:** 9

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | number | Yes | Mission ID. |

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

```TypeScript
onMissionCreated(mission: number): void
```

Called when the system creates a mission.

**Since:** 8

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | number | Yes | Mission ID. |

**Examples**

For details, see [onMissionClosed](#onmissionclosed).

## onMissionDestroyed

```TypeScript
onMissionDestroyed(mission: number): void
```

Called when the system destroys a mission.

**Since:** 8

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | number | Yes | Mission ID. |

**Examples**

For details, see [onMissionClosed](#onmissionclosed).

## onMissionIconUpdated

```TypeScript
onMissionIconUpdated(mission: number, icon: image.PixelMap): void
```

Called when the system updates the icon of a mission.

**Since:** 9

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | number | Yes | Mission ID. |
| icon | image.PixelMap | Yes | New mission icon. |

**Examples**

For details, see [onMissionClosed](#onmissionclosed).

## onMissionLabelUpdated

```TypeScript
onMissionLabelUpdated(mission: number): void
```

Called when the system updates the label of a mission.

**Since:** 9

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | number | Yes | Mission ID. |

**Examples**

For details, see [onMissionClosed](#onmissionclosed).

## onMissionMovedToFront

```TypeScript
onMissionMovedToFront(mission: number): void
```

Called when the system moves a mission to the foreground.

**Since:** 8

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | number | Yes | Mission ID. |

**Examples**

For details, see [onMissionClosed](#onmissionclosed).

## onMissionSnapshotChanged

```TypeScript
onMissionSnapshotChanged(mission: number): void
```

Called when the system updates the snapshot of a mission.

**Since:** 8

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | number | Yes | Mission ID. |

**Examples**

For details, see [onMissionClosed](#onmissionclosed).
