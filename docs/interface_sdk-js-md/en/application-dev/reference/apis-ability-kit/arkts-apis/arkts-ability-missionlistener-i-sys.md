# MissionListener (System API)

定义系统任务状态监听，可以通过[on](arkts-ability-missionmanager-on-f-sys.md#on)注册。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface MissionListener--><!--Device-unnamed-export interface MissionListener-End-->

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

当系统关闭任务时会触发该回调函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MissionListener-onMissionClosed(mission: int): void--><!--Device-MissionListener-onMissionClosed(mission: int): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示关闭的任务ID。 |

## onMissionCreated

ArkTS-Dyn:
```TypeScript
onMissionCreated(mission: number): void
```

ArkTS-Sta:
```TypeScript
onMissionCreated(mission: int): void
```

当系统创建任务时会触发该回调函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MissionListener-onMissionCreated(mission: int): void--><!--Device-MissionListener-onMissionCreated(mission: int): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示创建的任务ID。 |

## onMissionDestroyed

ArkTS-Dyn:
```TypeScript
onMissionDestroyed(mission: number): void
```

ArkTS-Sta:
```TypeScript
onMissionDestroyed(mission: int): void
```

当系统销毁任务时会触发该回调函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MissionListener-onMissionDestroyed(mission: int): void--><!--Device-MissionListener-onMissionDestroyed(mission: int): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示销毁的任务ID。 |

## onMissionIconUpdated

ArkTS-Dyn:
```TypeScript
onMissionIconUpdated(mission: number, icon: image.PixelMap): void
```

ArkTS-Sta:
```TypeScript
onMissionIconUpdated(mission: int, icon: image.PixelMap): void
```

当系统更新任务图标时会触发该回调函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MissionListener-onMissionIconUpdated(mission: int, icon: image.PixelMap): void--><!--Device-MissionListener-onMissionIconUpdated(mission: int, icon: image.PixelMap): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示任务ID。 |
| icon | image.PixelMap | Yes | 表示更新的任务图标。 |

## onMissionLabelUpdated

ArkTS-Dyn:
```TypeScript
onMissionLabelUpdated(mission: number): void
```

ArkTS-Sta:
```TypeScript
onMissionLabelUpdated(mission: int): void
```

当系统更新任务标签时会触发该回调函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MissionListener-onMissionLabelUpdated(mission: int): void--><!--Device-MissionListener-onMissionLabelUpdated(mission: int): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示任务ID。 |

## onMissionMovedToFront

ArkTS-Dyn:
```TypeScript
onMissionMovedToFront(mission: number): void
```

ArkTS-Sta:
```TypeScript
onMissionMovedToFront(mission: int): void
```

当系统将任务移动到前台时会触发该回调函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MissionListener-onMissionMovedToFront(mission: int): void--><!--Device-MissionListener-onMissionMovedToFront(mission: int): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示任务ID。 |

## onMissionSnapshotChanged

ArkTS-Dyn:
```TypeScript
onMissionSnapshotChanged(mission: number): void
```

ArkTS-Sta:
```TypeScript
onMissionSnapshotChanged(mission: int): void
```

当系统更新任务缩略图时会触发该回调函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-MissionListener-onMissionSnapshotChanged(mission: int): void--><!--Device-MissionListener-onMissionSnapshotChanged(mission: int): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mission | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示任务ID。 |

