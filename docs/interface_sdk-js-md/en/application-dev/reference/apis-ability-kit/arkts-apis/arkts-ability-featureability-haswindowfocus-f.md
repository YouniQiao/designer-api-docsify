# hasWindowFocus

## Modules to Import

```TypeScript
import { featureAbility } from 'kits/@kit.AbilityKit';
```

## hasWindowFocus

```TypeScript
function hasWindowFocus(callback: AsyncCallback<boolean>): void
```

Checks whether the main window of this ability has the focus. This API uses an asynchronous callback to return the result.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |


## hasWindowFocus

```TypeScript
function hasWindowFocus(): Promise<boolean>
```

Checks whether the main window of this ability has the focus. This API uses a promise to return the result.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |
