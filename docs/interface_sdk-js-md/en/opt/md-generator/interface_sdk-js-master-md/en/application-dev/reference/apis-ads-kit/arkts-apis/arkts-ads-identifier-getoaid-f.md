# getOAID

## Modules to Import

```TypeScript
import { identifier } from '@kit.AdsKit';
```

## getOAID

```TypeScript
function getOAID(callback: AsyncCallback<string>): void
```

Obtains the OAID. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> The setting item of cross-app association access permission was named app tracking access permission
> in HarmonyOS NEXT Developer Beta5 and earlier versions.

**Since:** 10

**Required permissions:** ohos.permission.APP_TRACKING_CONSENT

<!--Device-identifier-function getOAID(callback: AsyncCallback<string>): void--><!--Device-identifier-function getOAID(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Advertising.OAID

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-oaid.md#17300001-system-internal-error) |

## Examples

```TypeScript
import { identifier } from '@kit.AdsKit';
import { BusinessError } from '@kit.BasicServicesKit';

identifier.getOAID((err: BusinessError, data: string) => {
  if (err.code) {
    return;
  }
  const oaid: string = data;
});
```


## getOAID

```TypeScript
function getOAID(): Promise<string>
```

Obtains the OAID. This API uses a promise to return the result.

> **NOTE：**
> 
> The setting item of cross-app association access permission was named app tracking access permission
> in HarmonyOS NEXT Developer Beta5 and earlier versions.

**Since:** 10

**Required permissions:** ohos.permission.APP_TRACKING_CONSENT

<!--Device-identifier-function getOAID(): Promise<string>--><!--Device-identifier-function getOAID(): Promise<string>-End-->

**System capability:** SystemCapability.Advertising.OAID

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-oaid.md#17300001-system-internal-error) |

## Examples

```TypeScript
import { identifier } from '@kit.AdsKit';

identifier.getOAID().then((data: string) => {
  const oaid: string = data;
});
```
