# terminateSelf

## Modules to Import

```TypeScript
import { particleAbility } from '@ohos.ability.particleAbility';
```

## terminateSelf

```TypeScript
function terminateSelf(callback: AsyncCallback<void>): void
```

Terminates this ParticleAbility. This API uses an asynchronous callback to return the result.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | Yes | Callback used to return the result. If the ParticleAbility is terminated,**err** is **undefined**; otherwise, **err** is an error object. |

**Example**

```TypeScript
import { particleAbility } from '@kit.AbilityKit';

particleAbility.terminateSelf(
  (error) => {
    if (error && error.code !== 0) {
      console.error(`terminateSelf fail, error: ${JSON.stringify(error)}`);
    }
  }
);

```


## terminateSelf

```TypeScript
function terminateSelf(): Promise<void>
```

Terminates this ParticleAbility. This API uses a promise to return the result.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. Promise that returns no value. |

**Example**

```TypeScript
import { particleAbility } from '@kit.AbilityKit';

particleAbility.terminateSelf().then(() => {
  console.info('particleAbility terminateSelf');
});

```

