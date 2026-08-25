# getRequestInfo

## Modules to Import

```TypeScript
import { dialogRequest } from 'kits/@kit.AbilityKit';
```

## getRequestInfo

```TypeScript
function getRequestInfo(want: Want): RequestInfo
```


> **NOTE：**&gt;
> This API can be used by a ServiceExtensionAbility. If the ServiceExtensionAbility implements modal dialog boxes,
> the request information can be obtained from Want. If this API is used in other scenarios, no return value is
> obtained.
Obtains the request information from Want.

**Since:** 9

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
