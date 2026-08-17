# @ohos.app.ability.UIAbility

## Modules to Import

```TypeScript
import { Callee } from 'Callee';
import { CalleeCallback } from 'CalleeCallback';
import { Caller } from 'Caller';
import { OnReleaseCallback } from 'OnReleaseCallback';
import { OnRemoteStateChangeCallback } from 'OnRemoteStateChangeCallback';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Application component that has the UI. It provides lifecycle callbacks such as component creation, destruction, and foreground/background switching, and supports background communication. |

### Interfaces

| Name | Description |
| --- | --- |
| [Callee](arkts-ability-app-ability-uiability-callee-i.md) | Background communication object created by the system for the UIAbility, known as the Callee UIAbility (Callee), which is capable of receiving data sent from the Caller object. |
| [CalleeCallback](arkts-ability-app-ability-uiability-calleecallback-i.md) | Defines the callback of the registration message notification of the UIAbility. |
| [Caller](arkts-ability-app-ability-uiability-caller-i.md) | A Caller UIAbility can use the [startAbilityByCall](arkts-ability-uiabilitycontext-c.md#startabilitybycall) API to start the target Callee UIAbility. After the target UIAbility is started successfully, a Caller object is returned to the caller for communication. |
| [OnReleaseCallback](arkts-ability-app-ability-uiability-onreleasecallback-i.md) | Defines the callback that is invoked when the stub on the target UIAbility is disconnected. |
| [OnRemoteStateChangeCallback](arkts-ability-app-ability-uiability-onremotestatechangecallback-i.md) | Defines the callback that is invoked when the remote UIAbility state changes in the collaboration scenario. |

### Types

| Name | Description |
| --- | --- |
| [CalleeCallback](arkts-ability-calleecallback-t.md) | Defines the callback of the registration message notification of the UIAbility. |
| [OnReleaseCallback](arkts-ability-onreleasecallback-t.md) | Defines the callback that is invoked when the stub on the target UIAbility is disconnected. |
| [OnRemoteStateChangeCallback](arkts-ability-onremotestatechangecallback-t.md) | Defines the callback that is invoked when the remote UIAbility state changes in the collaboration scenario. |

