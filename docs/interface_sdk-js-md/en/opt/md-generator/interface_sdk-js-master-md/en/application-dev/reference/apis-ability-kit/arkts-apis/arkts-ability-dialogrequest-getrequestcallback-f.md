# getRequestCallback

## Modules to Import

```TypeScript
import { dialogRequest } from 'kits/@kit.AbilityKit';
```

## getRequestCallback

```TypeScript
function getRequestCallback(want: Want): RequestCallback
```

Obtains the request callback from Want.

> **NOTE：**
> 
> This API can be used by a ServiceExtensionAbility. If the ServiceExtensionAbility implements modal dialog boxes,
> the request callback can be obtained from Want. If this API is used in other scenarios, no return value is
> obtained.

**Since:** 9

<!--Device-dialogRequest-function getRequestCallback(want: Want): RequestCallback--><!--Device-dialogRequest-function getRequestCallback(want: Want): RequestCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RequestCallback](arkts-ability-dialogrequest-requestcallback-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let requestCallback = dialogRequest.getRequestCallback(want);
    } catch(err) {
      console.error(`getRequestInfo err= ${JSON.stringify(err)}`);
    }
  }
}
```
