# getArguments

## Modules to Import

```TypeScript
import { abilityDelegatorRegistry } from 'kits/@kit.TestKit';
```

## getArguments

```TypeScript
function getArguments(): AbilityDelegatorArgs
```

Obtains an [AbilityDelegatorArgs](arkts-test-abilitydelegatorregistry-abilitydelegatorargs-t.md) object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-abilityDelegatorRegistry-function getArguments(): AbilityDelegatorArgs--><!--Device-abilityDelegatorRegistry-function getArguments(): AbilityDelegatorArgs-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AbilityDelegatorArgs](arkts-test-abilitydelegatorregistry-abilitydelegatorargs-t.md) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

// Obtain the AbilityDelegatorArgs object of the application.
let args = abilityDelegatorRegistry.getArguments();
// Print the test parameter information.
console.info(`getArguments bundleName: ${args.bundleName}`);
console.info(`getArguments parameters: ${JSON.stringify(args.parameters)}`);
console.info(`getArguments testCaseNames: ${args.testCaseNames}`);
console.info(`getArguments testRunnerClassName: ${args.testRunnerClassName}`);
```
