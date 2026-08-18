# getContext

## Modules to Import

```TypeScript
```

## getContext

```TypeScript
function getContext(): Context
```

Obtains the application context.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-featureAbility-function getContext(): Context--><!--Device-featureAbility-function getContext(): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) |

**Examples**

```TypeScript
import { featureAbility } from '@kit.AbilityKit';

let context = featureAbility.getContext();
context.getBundleName((error, data) => {
  if (error && error.code !== 0) {
    console.error(`getBundleName fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`getBundleName success, data: ${JSON.stringify(data)}`);
  }
});
```
