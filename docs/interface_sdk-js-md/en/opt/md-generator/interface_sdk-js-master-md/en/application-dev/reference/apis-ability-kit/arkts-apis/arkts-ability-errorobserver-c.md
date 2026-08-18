# ErrorObserver

The ErrorObserver module defines an observer to listen for application errors. It can be used as an input parameter in [ErrorManager.on](arkts-ability-errormanager-onerror-f.md#onerror) to listen for errors that occur in the current application.

**Since:** 9

<!--Device-unnamed-export default class ErrorObserver--><!--Device-unnamed-export default class ErrorObserver-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onException

```TypeScript
onException?(errObject: Error): void
```

Called when the application encounters an exception and reports it to the JavaScript layer.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorObserver-onException?(errObject: Error): void--><!--Device-ErrorObserver-onException?(errObject: Error): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| errObject | Error | Yes |

**Examples**

```TypeScript
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: errorManager.ErrorObserver = {
  onUnhandledException(errorMsg) {
    console.error('onUnhandledException, errorMsg: ', errorMsg);
  },
  onException(errorObj) {
    console.error('onException, name: ', errorObj.name);
    console.error('onException, message: ', errorObj.message);
    if (typeof (errorObj.stack) === 'string') {
      console.error('onException, stack: ', errorObj.stack);
    }
  }
};

try {
  errorManager.on('error', observer);
} catch (error) {
  console.error(`registerErrorObserver failed, error.code: ${(error as BusinessError).code}, error.message: ${(error as BusinessError).message}`);
}
```

## onUnhandledException

```TypeScript
onUnhandledException(errMsg: string): void
```

Called when an uncaught exception occurs in the application.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorObserver-onUnhandledException(errMsg: string): void--><!--Device-ErrorObserver-onUnhandledException(errMsg: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| errMsg | string | Yes |

**Examples**

```TypeScript
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: errorManager.ErrorObserver = {
  onUnhandledException(errorMsg) {
    console.error('onUnhandledException, errorMsg: ', errorMsg);
  }
};

try {
  errorManager.on('error', observer);
} catch (error) {
  console.error(`registerErrorObserver failed, error.code: ${(error as BusinessError).code}, error.message: ${(error as BusinessError).message}`);
}
```
