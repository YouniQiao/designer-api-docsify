# AppForegroundStateObserver (System API)

The module defines the listener used to listen for application startup and exit state changes. It can be used as an input parameter of [appManager.on('appForegroundState')](../../apis-ability-kit/arkts-apis/arkts-ability-appmanager-onapplicationstate-f.md#onapplicationstate) to listen for the state changes of all applications.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface AppForegroundStateObserver--><!--Device-unnamed-declare interface AppForegroundStateObserver-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## onAppStateChanged

```TypeScript
onAppStateChanged(appStateData: AppStateData): void
```

Called when the application launch or exit state changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AppForegroundStateObserver-onAppStateChanged(appStateData: AppStateData): void--><!--Device-AppForegroundStateObserver-onAppStateChanged(appStateData: AppStateData): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appStateData | [AppStateData](../../apis-ability-kit/arkts-apis/arkts-ability-appstatedata-c.md) | Yes | Application state data. |

