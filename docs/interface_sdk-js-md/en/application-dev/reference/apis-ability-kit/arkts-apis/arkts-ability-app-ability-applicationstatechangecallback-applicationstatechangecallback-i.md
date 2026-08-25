# ApplicationStateChangeCallback

The module is used to listen for state changes of the current application process. For ease of description, the term"application process" will be referred to as "process" in the following sections. You can call [ApplicationContext.on('applicationStateChange')](arkts-ability-applicationcontext-c.md#onapplicationstatechange) and pass in a custom ApplicationStateChangeCallback to listen for foreground/background state changes of the current process. This allows you to perform certain actions based on the process state changes, for example, tracking the duration of the process in the foreground and background, or clearing memory caches when the process moves to the background.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { ApplicationStateChangeCallback } from '@kit.AbilityKit';
```
