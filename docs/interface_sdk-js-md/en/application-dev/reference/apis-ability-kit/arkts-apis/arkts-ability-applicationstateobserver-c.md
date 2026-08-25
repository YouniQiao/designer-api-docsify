# ApplicationStateObserver

The module defines an observer to listen for application state changes. It can be used as an input parameter in [on('applicationState')](arkts-ability-appmanager-on-f.md#onapplicationstate) to listen for lifecycle changes of the application.

**Since:** 14

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onAbilityStateChanged

```TypeScript
onAbilityStateChanged(abilityStateData: AbilityStateData): void
```

Called when the ability state changes.

**Since:** 14

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| abilityStateData | [AbilityStateData](arkts-ability-abilitystatedata-c.md) | Yes |

## onAppStarted

```TypeScript
onAppStarted(appStateData: AppStateData): void
```

Called when the first process of the application is created.

**Since:** 14

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| appStateData | [AppStateData](arkts-ability-appstatedata-c.md) | Yes |

## onAppStopped

```TypeScript
onAppStopped(appStateData: AppStateData): void
```

Called when the last process of the application is destroyed.

**Since:** 14

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| appStateData | [AppStateData](arkts-ability-appstatedata-c.md) | Yes |

## onForegroundApplicationChanged

```TypeScript
onForegroundApplicationChanged(appStateData: AppStateData): void
```

Called when the foreground or background state of an application changes.

**Since:** 14

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| appStateData | [AppStateData](arkts-ability-appstatedata-c.md) | Yes |

## onProcessCreated

```TypeScript
onProcessCreated(processData: ProcessData): void
```

Called when a process is created.

**Since:** 14

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| processData | [ProcessData](arkts-ability-processdata-t.md) | Yes |

## onProcessDied

```TypeScript
onProcessDied(processData: ProcessData): void
```

Called when a process is destroyed.

**Since:** 14

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| processData | [ProcessData](arkts-ability-processdata-t.md) | Yes |

## onProcessStateChanged

```TypeScript
onProcessStateChanged(processData: ProcessData): void
```

Called when the process state is changed.

**Since:** 14

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| processData | [ProcessData](arkts-ability-processdata-t.md) | Yes |
