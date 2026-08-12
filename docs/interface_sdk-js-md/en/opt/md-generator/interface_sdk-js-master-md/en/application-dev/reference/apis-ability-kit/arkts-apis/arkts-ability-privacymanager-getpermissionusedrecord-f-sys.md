# getPermissionUsedRecord (System API)

## Modules to Import

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
```

## getPermissionUsedRecord

```TypeScript
function getPermissionUsedRecord(request: PermissionUsedRequest): Promise<PermissionUsedResponse>
```

Obtains historical permission usage records, which can be used in permission auditing or security monitoring scenarios, such as checking an application's usage of sensitive permissions within a specified time period.This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function getPermissionUsedRecord(request: PermissionUsedRequest): Promise<PermissionUsedResponse>--><!--Device-privacyManager-function getPermissionUsedRecord(request: PermissionUsedRequest): Promise<PermissionUsedResponse>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [PermissionUsedRequest](arkts-ability-privacymanager-permissionusedrequest-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PermissionUsedResponse](arkts-ability-privacymanager-permissionusedresponse-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100001-invalid-parameters) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100007-system-service-not-working-properly) |

## Examples

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let request: privacyManager.PermissionUsedRequest = {
    'tokenId': 1, // It can be obtained through the accessTokenId field of ApplicationInfo in the application's BundleInfo.
    'isRemote': false,
    'deviceId': 'device',
    'bundleName': 'bundle',
    'permissionNames': [],
    'beginTime': 0,
    'endTime': 1,
    'flag': privacyManager.PermissionUsageFlag.FLAG_PERMISSION_USAGE_DETAIL,
};

// Query historical permission usage records
privacyManager.getPermissionUsedRecord(request).then((data) => {
  console.info(`getPermissionUsedRecord success, result: ${data}`);
}).catch((err: BusinessError): void => {
  console.error(`getPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
});
```


## getPermissionUsedRecord

```TypeScript
function getPermissionUsedRecord(
    request: PermissionUsedRequest,
    callback: AsyncCallback<PermissionUsedResponse>): void
```

Obtains historical permission usage records, which can be used in permission auditing or security monitoring scenarios, such as checking an application's usage of sensitive permissions within a specified time period.This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function getPermissionUsedRecord(    request: PermissionUsedRequest,    callback: AsyncCallback<PermissionUsedResponse>): void--><!--Device-privacyManager-function getPermissionUsedRecord(    request: PermissionUsedRequest,    callback: AsyncCallback<PermissionUsedResponse>): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [PermissionUsedRequest](arkts-ability-privacymanager-permissionusedrequest-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PermissionUsedResponse](arkts-ability-privacymanager-permissionusedresponse-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100001-invalid-parameters) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100007-system-service-not-working-properly) |

## Examples

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let request: privacyManager.PermissionUsedRequest = {
    'tokenId': 1, // It can be obtained through the accessTokenId field in the ApplicationInfo of the application's BundleInfo.
    'isRemote': false,
    'deviceId': 'device',
    'bundleName': 'bundle',
    'permissionNames': [],
    'beginTime': 0,
    'endTime': 1,
    'flag': privacyManager.PermissionUsageFlag.FLAG_PERMISSION_USAGE_DETAIL,
};

// Query historical permission usage records
privacyManager.getPermissionUsedRecord(request, (err: BusinessError, data: privacyManager.PermissionUsedResponse) => {
  if (err) {
    console.error(`getPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`getPermissionUsedRecord success, result: ${data}`);
  }
});
```
