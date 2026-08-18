# FilterCallback (System API)

Enumerates the callbacks to filter. It can be used with [AppStateFilter](arkts-ability-appmanager-appstatefilter-i-sys.md#appstatefilter-system-api) to filter the callbacks you want to listen for.

**Since:** 23

<!--Device-appManager-export enum FilterCallback--><!--Device-appManager-export enum FilterCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## ON_FOREGROUND_APPLICATION_CHANGED

```TypeScript
ON_FOREGROUND_APPLICATION_CHANGED = 1 << 0
```

Corresponds to the [ApplicationStateObserver.onForegroundApplicationChanged](arkts-ability-applicationstateobserver-c.md#onforegroundapplicationchanged) callback, which is executed when the application's foreground/background state changes.

**Since:** 23

<!--Device-FilterCallback-ON_FOREGROUND_APPLICATION_CHANGED = 1 << 0--><!--Device-FilterCallback-ON_FOREGROUND_APPLICATION_CHANGED = 1 << 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## ON_ABILITY_STATE_CHANGED

```TypeScript
ON_ABILITY_STATE_CHANGED = 1 << 1
```

Corresponds to the [ApplicationStateObserver.onAbilityStateChanged](arkts-ability-applicationstateobserver-c.md#onabilitystatechanged) callback, which is executed when the ability state changes.

**Since:** 23

<!--Device-FilterCallback-ON_ABILITY_STATE_CHANGED = 1 << 1--><!--Device-FilterCallback-ON_ABILITY_STATE_CHANGED = 1 << 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## ON_PROCESS_CREATED

```TypeScript
ON_PROCESS_CREATED = 1 << 2
```

Corresponds to the [ApplicationStateObserver.onProcessCreated](arkts-ability-applicationstateobserver-c.md#onprocesscreated) callback, which is executed when a process is created.

**Since:** 23

<!--Device-FilterCallback-ON_PROCESS_CREATED = 1 << 2--><!--Device-FilterCallback-ON_PROCESS_CREATED = 1 << 2-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## ON_PROCESS_DIED

```TypeScript
ON_PROCESS_DIED = 1 << 3
```

Corresponds to the [ApplicationStateObserver.onProcessDied](arkts-ability-applicationstateobserver-c.md#onprocessdied) callback, which is executed when a process is destroyed.

**Since:** 23

<!--Device-FilterCallback-ON_PROCESS_DIED = 1 << 3--><!--Device-FilterCallback-ON_PROCESS_DIED = 1 << 3-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## ON_PROCESS_STATE_CHANGED

```TypeScript
ON_PROCESS_STATE_CHANGED = 1 << 4
```

Corresponds to the [ApplicationStateObserver.onProcessStateChanged](arkts-ability-applicationstateobserver-c.md#onprocessstatechanged) callback, which is executed when the process state is updated.

**Since:** 23

<!--Device-FilterCallback-ON_PROCESS_STATE_CHANGED = 1 << 4--><!--Device-FilterCallback-ON_PROCESS_STATE_CHANGED = 1 << 4-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## ON_APP_STARTED

```TypeScript
ON_APP_STARTED = 1 << 5
```

Corresponds to the [ApplicationStateObserver.onAppStarted](arkts-ability-applicationstateobserver-c.md#onappstarted) callback, which is executed when the application's first process is created.

**Since:** 23

<!--Device-FilterCallback-ON_APP_STARTED = 1 << 5--><!--Device-FilterCallback-ON_APP_STARTED = 1 << 5-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## ON_APP_STOPPED

```TypeScript
ON_APP_STOPPED = 1 << 6
```

Corresponds to the [ApplicationStateObserver.onAppStopped](arkts-ability-applicationstateobserver-c.md#onappstopped) callback, which is executed when the application's last process is destroyed.

**Since:** 23

<!--Device-FilterCallback-ON_APP_STOPPED = 1 << 6--><!--Device-FilterCallback-ON_APP_STOPPED = 1 << 6-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.
