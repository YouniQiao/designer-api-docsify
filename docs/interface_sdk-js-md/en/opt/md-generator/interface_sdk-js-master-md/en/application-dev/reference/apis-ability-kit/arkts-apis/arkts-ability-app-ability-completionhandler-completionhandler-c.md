# CompletionHandler

CompletionHandler provides two callback functions,  
[onRequestSuccess](arkts-ability-app-ability-completionhandler-completionhandler-c.md#onrequestsuccess) and  
[onRequestFailure](arkts-ability-app-ability-completionhandler-completionhandler-c.md#onrequestfailure), to handle the results of successful and failed application launch requests, respectively.

**Since:** 20

<!--Device-unnamed-declare class CompletionHandler--><!--Device-unnamed-declare class CompletionHandler-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { CompletionHandler } from 'kits/@kit.AbilityKit';
```

## onRequestFailure

```TypeScript
onRequestFailure(elementName: ElementName, message: string): void
```

Called when the application fails to be launched.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CompletionHandler-onRequestFailure(elementName: ElementName, message: string): void--><!--Device-CompletionHandler-onRequestFailure(elementName: ElementName, message: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes |
| message | string | Yes |

## Examples

See [Usage of CompletionHandler](#usage-of-completionhandler).

## onRequestSuccess

```TypeScript
onRequestSuccess(elementName: ElementName, message: string): void
```

Called when the application is successfully launched.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CompletionHandler-onRequestSuccess(elementName: ElementName, message: string): void--><!--Device-CompletionHandler-onRequestSuccess(elementName: ElementName, message: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes |
| message | string | Yes |

## Examples

See [Usage of CompletionHandler](#usage-of-completionhandler).
