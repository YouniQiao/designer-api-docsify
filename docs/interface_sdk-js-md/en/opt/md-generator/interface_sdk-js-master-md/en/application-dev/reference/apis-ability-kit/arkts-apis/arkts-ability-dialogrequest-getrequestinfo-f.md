# getRequestInfo

## Modules to Import

```TypeScript
import { dialogRequest } from '@kit.AbilityKit';
```

## getRequestInfo

```TypeScript
function getRequestInfo(want: Want): RequestInfo
```

> **NOTE：**
> 
> This API can be used by a ServiceExtensionAbility. If the ServiceExtensionAbility implements modal dialog boxes,
> the request information can be obtained from Want. If this API is used in other scenarios, no return value is
> obtained.

Obtains the request information from Want.

**Since:** 9

<!--Device-dialogRequest-function getRequestInfo(want: Want): RequestInfo--><!--Device-dialogRequest-function getRequestInfo(want: Want): RequestInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RequestInfo](arkts-ability-dialogrequest-requestinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let requestInfo = dialogRequest.getRequestInfo(want);
    } catch (err) {
      console.error(`getRequestInfo err= ${JSON.stringify(err)}`);
    }
  }
}
```
