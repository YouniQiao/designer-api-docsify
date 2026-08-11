# terminateSelf

## Modules to Import

```TypeScript
import { featureAbility } from 'kits/@kit.AbilityKit';
```

## terminateSelf

```TypeScript
function terminateSelf(callback: AsyncCallback<void>): void
```

Terminates this ability. This API uses an asynchronous callback to return the result.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-featureAbility-function terminateSelf(callback: AsyncCallback<void>): void--><!--Device-featureAbility-function terminateSelf(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { featureAbility } from '@kit.AbilityKit';

featureAbility.terminateSelf(
  (error) => {
    console.error(`error: ${JSON.stringify(error)}`);
  }
)
```


## terminateSelf

```TypeScript
function terminateSelf(): Promise<void>
```

Terminates this ability. This API uses a promise to return the result.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-featureAbility-function terminateSelf(): Promise<void>--><!--Device-featureAbility-function terminateSelf(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

featureAbility.terminateSelf().then(() => {
  console.info('==========================>terminateSelf=======================>');
}).catch((error: BusinessError) => {
  console.error(`terminateSelf failed, error.code: ${error.code}, error.message: ${error.message}`);
});
```
