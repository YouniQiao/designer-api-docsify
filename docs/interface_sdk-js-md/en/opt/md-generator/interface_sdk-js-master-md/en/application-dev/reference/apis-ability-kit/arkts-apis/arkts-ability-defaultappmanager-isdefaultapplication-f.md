# isDefaultApplication

## Modules to Import

```TypeScript
import { defaultAppManager } from 'kits/@kit.AbilityKit';
```

## isDefaultApplication

```TypeScript
function isDefaultApplication(type: string, callback: AsyncCallback<boolean>) : void
```

Checks whether this application is the default application of a system-defined application type or a  
[uniform data type](../../apis-arkdata/arkts-apis/arkts-data-uniformtypedescriptor.md/arkts-data-uniformtypedescriptor.md). This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-defaultAppManager-function isDefaultApplication(type: string, callback: AsyncCallback<boolean>) : void--><!--Device-defaultAppManager-function isDefaultApplication(type: string, callback: AsyncCallback<boolean>) : void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.DefaultApp

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## Examples

```TypeScript
import { defaultAppManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

defaultAppManager.isDefaultApplication(defaultAppManager.ApplicationType.BROWSER, (err: BusinessError, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. IsDefaultApplication ? ' + JSON.stringify(data));
});
```


## isDefaultApplication

```TypeScript
function isDefaultApplication(type: string) : Promise<boolean>
```

Checks whether this application is the default application of a system-defined application type or a  
[uniform data type](../../apis-arkdata/arkts-apis/arkts-data-uniformtypedescriptor.md/arkts-data-uniformtypedescriptor.md). This API uses a promise to return the result.

**Since:** 9

<!--Device-defaultAppManager-function isDefaultApplication(type: string) : Promise<boolean>--><!--Device-defaultAppManager-function isDefaultApplication(type: string) : Promise<boolean>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.DefaultApp

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## Examples

```TypeScript
import { defaultAppManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

defaultAppManager.isDefaultApplication(defaultAppManager.ApplicationType.BROWSER)
  .then((data) => {
    console.info('Operation successful. IsDefaultApplication ? ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
});
```
