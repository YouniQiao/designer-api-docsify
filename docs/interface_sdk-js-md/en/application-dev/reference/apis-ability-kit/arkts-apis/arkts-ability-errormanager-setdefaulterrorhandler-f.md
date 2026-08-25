# setDefaultErrorHandler

## Modules to Import

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## setDefaultErrorHandler

```TypeScript
function setDefaultErrorHandler(defaultHandler?: ErrorHandler) : ErrorHandler
```

Returns the previously registered handler when a JavaScript crash exception occurs. It can only be used in the main thread.If an invalid parameter is passed or the API is called from a child thread, an error code is thrown and **undefined** is returned. You are advised to handle it with try-catch logic.If the API parameter is empty, subsequently registered handlers are not able to establish a connection with previously registered handlers, thereby breaking the chain call mechanism.

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| defaultHandler | [ErrorHandler](arkts-ability-errormanager-errorhandler-t.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ErrorHandler](arkts-ability-errormanager-errorhandler-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [16000205](../errorcode-ability.md#16000205-api-not-called-in-main-thread) |
