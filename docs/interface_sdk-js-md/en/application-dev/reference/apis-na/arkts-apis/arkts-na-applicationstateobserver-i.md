# ApplicationStateObserver

The module defines an observer to listen for application state changes. It can be used as an input parameter in [on('applicationState')](../../apis-ability-kit/arkts-apis/arkts-ability-appmanager-onapplicationstate-f.md#on_applicationState) to listen for lifecycle changes of the application.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare interface ApplicationStateObserver--><!--Device-unnamed-declare interface ApplicationStateObserver-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onAbilityStateChanged

```TypeScript
onAbilityStateChanged(abilityStateData: AbilityStateData): void
```

Called when the ability state changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-ApplicationStateObserver-onAbilityStateChanged(abilityStateData: AbilityStateData): void--><!--Device-ApplicationStateObserver-onAbilityStateChanged(abilityStateData: AbilityStateData): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| abilityStateData | [AbilityStateData](../../apis-ability-kit/arkts-apis/arkts-ability-abilitystatedata-c.md) | Yes | Ability state data. |

## onAppStarted

```TypeScript
onAppStarted(appStateData: AppStateData): void
```

Called when the first process of the application is created.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-ApplicationStateObserver-onAppStarted(appStateData: AppStateData): void--><!--Device-ApplicationStateObserver-onAppStarted(appStateData: AppStateData): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appStateData | [AppStateData](../../apis-ability-kit/arkts-apis/arkts-ability-appstatedata-c.md) | Yes | Application state data. |

## onAppStopped

```TypeScript
onAppStopped(appStateData: AppStateData): void
```

Called when the last process of the application is destroyed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-ApplicationStateObserver-onAppStopped(appStateData: AppStateData): void--><!--Device-ApplicationStateObserver-onAppStopped(appStateData: AppStateData): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appStateData | [AppStateData](../../apis-ability-kit/arkts-apis/arkts-ability-appstatedata-c.md) | Yes | Application state data. |

## onForegroundApplicationChanged

```TypeScript
onForegroundApplicationChanged(appStateData: AppStateData): void
```

Called when the foreground or background state of an application changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-ApplicationStateObserver-onForegroundApplicationChanged(appStateData: AppStateData): void--><!--Device-ApplicationStateObserver-onForegroundApplicationChanged(appStateData: AppStateData): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appStateData | [AppStateData](../../apis-ability-kit/arkts-apis/arkts-ability-appstatedata-c.md) | Yes | Application state data. |

## onProcessCreated

```TypeScript
onProcessCreated(processData: ProcessData): void
```

Called when a process is created.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-ApplicationStateObserver-onProcessCreated(processData: ProcessData): void--><!--Device-ApplicationStateObserver-onProcessCreated(processData: ProcessData): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| processData | [ProcessData](arkts-na-processdata-t.md) | Yes | Process data. |

## onProcessDied

```TypeScript
onProcessDied(processData: ProcessData): void
```

Called when a process is destroyed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-ApplicationStateObserver-onProcessDied(processData: ProcessData): void--><!--Device-ApplicationStateObserver-onProcessDied(processData: ProcessData): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| processData | [ProcessData](arkts-na-processdata-t.md) | Yes | Process data. |

## onProcessStateChanged

```TypeScript
onProcessStateChanged(processData: ProcessData): void
```

Called when the process state is changed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-ApplicationStateObserver-onProcessStateChanged(processData: ProcessData): void--><!--Device-ApplicationStateObserver-onProcessStateChanged(processData: ProcessData): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| processData | [ProcessData](arkts-na-processdata-t.md) | Yes | Process data. |

