# revokeUriPermission (System API)

## Modules to Import

```TypeScript
import { uriPermissionManager } from '@kit.AbilityKit';
```

## revokeUriPermission

```TypeScript
function revokeUriPermission(uri: string, targetBundleName: string, callback: AsyncCallback<number>): void
```

Revokes the URI permission from an application. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> - This API can be used to revoke the URI permission of another application obtained by this application or URI
> permission granted by this application.
> 
> - URI processing involves encoding and decoding. Therefore, the input URI must be obtained through the
> [getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md#getUriFromPath) API. For URIs combined by the application, the
> system cannot guarantee their functions.

**Since:** 10

**Required permissions:** 
- API version 10 - 11: ohos.permission.PROXY_AUTHORIZATION_URI

<!--Device-uriPermissionManager-function revokeUriPermission(uri: string, targetBundleName: string, callback: AsyncCallback<number>): void--><!--Device-uriPermissionManager-function revokeUriPermission(uri: string, targetBundleName: string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| targetBundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000059](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000059-specified-uri-type-is-invalid) |

## Examples

```TypeScript
import { uriPermissionManager } from '@kit.AbilityKit';

let targetBundleName = 'com.example.test_case2';
let uri = "file://com.example.test_case1/data/storage/el2/base/haps/entry_test/files/newDir";

uriPermissionManager.revokeUriPermission(uri, targetBundleName, (error) => {
  if (error && error.code !== 0) {
    console.error("revokeUriPermission failed, error.code = " + error.code);
    return;
  }
  console.info("revokeUriPermission success");
});
```


## revokeUriPermission

```TypeScript
function revokeUriPermission(uri: string, targetBundleName: string): Promise<number>
```

Revokes the URI permission from an application. This API uses a promise to return the result.

> **NOTE：**
> 
> - This API can be used to revoke the URI permission of another application obtained by this application or URI
> permission granted by this application.
> 
> - URI processing involves encoding and decoding. Therefore, the input URI must be obtained through the
> [getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md#getUriFromPath) API. For URIs combined by the application, the
> system cannot guarantee their functions.

**Since:** 10

**Required permissions:** 
- API version 10 - 11: ohos.permission.PROXY_AUTHORIZATION_URI

<!--Device-uriPermissionManager-function revokeUriPermission(uri: string, targetBundleName: string): Promise<number>--><!--Device-uriPermissionManager-function revokeUriPermission(uri: string, targetBundleName: string): Promise<number>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| targetBundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000059](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000059-specified-uri-type-is-invalid) |

## Examples

```TypeScript
import { uriPermissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let targetBundleName = 'com.example.test_case2';
let uri = 'file://com.example.test_case1/data/storage/el2/base/haps/entry_test/files/newDir';

uriPermissionManager.revokeUriPermission(uri, targetBundleName)
  .then((data) => {
    console.info(`Verification success, data: ${JSON.stringify(data)}.`);
  }).catch((error: BusinessError) => {
  console.error(`Verification failed, err code: ${error.code}, err msg: ${error.message}.`);
});
```


## revokeUriPermission

```TypeScript
function revokeUriPermission(uri: string, targetBundleName: string, appCloneIndex: number): Promise<void>
```

Revokes the URI permission from an application. This API uses a promise to return the result.

> **NOTE：**
> 
> - This API can be used to revoke the URI permission of another application obtained by this application or URI
> permission granted by this application.
> 
> - This API can be used to revoke the URI permissions granted to a cloned application. You need to specify the
> application bundle name and index of the cloned application.
> 
> - URI processing involves encoding and decoding. Therefore, the input URI must be obtained through the
> [getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md#getUriFromPath) API. For URIs combined by the application, the
> system cannot guarantee their functions.

**Since:** 14

<!--Device-uriPermissionManager-function revokeUriPermission(uri: string, targetBundleName: string, appCloneIndex: int): Promise<void>--><!--Device-uriPermissionManager-function revokeUriPermission(uri: string, targetBundleName: string, appCloneIndex: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| targetBundleName | string | Yes |
| appCloneIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16000081](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000081-failed-to-obtain-the-target-application-information) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000059](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000059-specified-uri-type-is-invalid) |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want, wantConstant, uriPermissionManager } from '@kit.AbilityKit';
import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  }

  onForeground(): void {
    let targetBundleName: string = 'com.example.demo1';
    let filePath: string = this.context.filesDir + "/test.txt";
    let uri: string = fileUri.getUriFromPath(filePath);
    // revoke uri permission of main application
    try {
      let appCloneIndex: number = 0;
      uriPermissionManager.revokeUriPermission(uri, targetBundleName, appCloneIndex)
        .then(() => {
          console.info('revokeUriPermission succeeded.');
        }).catch((error: BusinessError) => {
        console.error(`revokeUriPermission failed. error: ${JSON.stringify(error)}.`);
      });
    } catch (error) {
      console.error(`revokeUriPermission failed. error: ${JSON.stringify(error)}.`);
    }

    // revoke uri permission of clone application
    try {
      let appCloneIndex: number = 1;
      uriPermissionManager.revokeUriPermission(uri, targetBundleName, appCloneIndex)
        .then(() => {
          console.info('revokeUriPermission succeeded.');
        }).catch((error: BusinessError) => {
        console.error(`revokeUriPermission failed. error: ${JSON.stringify(error)}.`);
      });
    } catch (error) {
      console.error(`revokeUriPermission failed. error: ${JSON.stringify(error)}.`);
    }
  }
}
```
