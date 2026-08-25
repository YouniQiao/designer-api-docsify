# AppForegroundStateObserver (System API)

The module defines the listener used to listen for application startup and exit state changes. It can be used as an input parameter of [appManager.on('appForegroundState')](arkts-ability-appmanager-on-f-sys.md#onappforegroundstate) to listen for the state changes of all applications.

**Since:** 11

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## onAppStateChanged

```TypeScript
onAppStateChanged(appStateData: AppStateData): void
```

Called when the application launch or exit state changes.

**Since:** 11

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| appStateData | [AppStateData](arkts-ability-appstatedata-c.md) | Yes |
