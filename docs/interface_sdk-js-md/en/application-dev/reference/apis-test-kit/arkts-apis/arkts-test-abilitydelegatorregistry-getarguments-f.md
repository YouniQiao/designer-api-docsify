# getArguments

## Modules to Import

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
```

## getArguments

```TypeScript
function getArguments(): AbilityDelegatorArgs
```

Obtains an [AbilityDelegatorArgs](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegatorargs-abilitydelegatorargs-i.md) object.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-abilityDelegatorRegistry-function getArguments(): AbilityDelegatorArgs--><!--Device-abilityDelegatorRegistry-function getArguments(): AbilityDelegatorArgs-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| AbilityDelegatorArgs | [AbilityDelegatorArgs]{ |

**Examples**

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

let args = abilityDelegatorRegistry.getArguments();
console.info(`getArguments bundleName: ${args.bundleName}`);
console.info(`getArguments parameters: ${JSON.stringify(args.parameters)}`);
console.info(`getArguments testCaseNames: ${args.testCaseNames}`);
console.info(`getArguments testRunnerClassName: ${args.testRunnerClassName}`);
```

