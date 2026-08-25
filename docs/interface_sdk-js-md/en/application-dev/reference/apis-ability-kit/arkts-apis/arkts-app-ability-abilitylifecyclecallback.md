# @ohos.app.ability.AbilityLifecycleCallback

The lifecycle of a [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) dynamically changes from creation to
 destruction.
 The AbilityLifecycleCallback module provides the capability to listen for these lifecycle changes, which can be used
 for scenarios such as tracking the runtime duration of each UIAbility and performing data loading decoupled from the
 service logic of UIAbility.
 > **NOTE**
 >
 > The APIs provided by this module can listen for lifecycle changes of the UIAbility within the same process.


## Modules to Import

```TypeScript
import { AbilityLifecycleCallback } from '@kit.AbilityKit';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilityLifecycleCallback](arkts-ability-app-ability-abilitylifecyclecallback-abilitylifecyclecallback-c.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [OnAbilitySaveStateFn](arkts-ability-onabilitysavestatefn-t.md) |
| [OnAbilityWillBackgroundFn](arkts-ability-onabilitywillbackgroundfn-t.md) |
| [OnAbilityWillContinueFn](arkts-ability-onabilitywillcontinuefn-t.md) |
| [OnAbilityWillCreateFn](arkts-ability-onabilitywillcreatefn-t.md) |
| [OnAbilityWillDestroyFn](arkts-ability-onabilitywilldestroyfn-t.md) |
| [OnAbilityWillForegroundFn](arkts-ability-onabilitywillforegroundfn-t.md) |
| [OnAbilityWillSaveStateFn](arkts-ability-onabilitywillsavestatefn-t.md) |
| [OnNewWantFn](arkts-ability-onnewwantfn-t.md) |
| [OnWillNewWantFn](arkts-ability-onwillnewwantfn-t.md) |
| [OnWindowStageRestoreFn](arkts-ability-onwindowstagerestorefn-t.md) |
| [OnWindowStageWillCreateFn](arkts-ability-onwindowstagewillcreatefn-t.md) |
| [OnWindowStageWillDestroyFn](arkts-ability-onwindowstagewilldestroyfn-t.md) |
| [OnWindowStageWillRestoreFn](arkts-ability-onwindowstagewillrestorefn-t.md) |
