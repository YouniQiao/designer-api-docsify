# hasWindowFocus

## Modules to Import

```TypeScript
import { featureAbility } from '@kit.AbilityKit';
```

## hasWindowFocus

```TypeScript
function hasWindowFocus(callback: AsyncCallback<boolean>): void
```

Checks whether the main window of this ability has the focus. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-featureAbility-function hasWindowFocus(callback: AsyncCallback<boolean>): void--><!--Device-featureAbility-function hasWindowFocus(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
import { featureAbility } from '@kit.AbilityKit';

featureAbility.hasWindowFocus((error, data) => {
  if (error && error.code !== 0) {
    console.error(`hasWindowFocus fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`hasWindowFocus success, data: ${JSON.stringify(data)}`);
  }
});
```


## hasWindowFocus

```TypeScript
function hasWindowFocus(): Promise<boolean>
```

Checks whether the main window of this ability has the focus. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-featureAbility-function hasWindowFocus(): Promise<boolean>--><!--Device-featureAbility-function hasWindowFocus(): Promise<boolean>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## Examples

```TypeScript
import { featureAbility } from '@kit.AbilityKit';

featureAbility.hasWindowFocus().then((data) => {
  console.info(`hasWindowFocus data: ${JSON.stringify(data)}`);
});
```
