# getPermissionUsedRecord（系统接口）

## getPermissionUsedRecord

```TypeScript
function getPermissionUsedRecord(request: PermissionUsedRequest): Promise<PermissionUsedResponse>
```

获取历史权限使用记录，可用于权限审计或安全监控场景，例如检查某应用在指定时间段内对敏感权限的使用情况。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function getPermissionUsedRecord(request: PermissionUsedRequest): Promise<PermissionUsedResponse>--><!--Device-privacyManager-function getPermissionUsedRecord(request: PermissionUsedRequest): Promise<PermissionUsedResponse>-End-->

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [PermissionUsedRequest](arkts-ability-privacymanager-permissionusedrequest-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PermissionUsedResponse](arkts-ability-privacymanager-permissionusedresponse-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |

## 示例

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let request: privacyManager.PermissionUsedRequest = {
    'tokenId': 1, // 可以通过应用BundleInfo中的ApplicationInfo的accessTokenId字段获取。
    'isRemote': false,
    'deviceId': 'device',
    'bundleName': 'bundle',
    'permissionNames': [],
    'beginTime': 0,
    'endTime': 1,
    'flag': privacyManager.PermissionUsageFlag.FLAG_PERMISSION_USAGE_DETAIL,
};

// 查询历史权限使用记录
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

获取历史权限使用记录，可用于权限审计或安全监控场景，例如检查某应用在指定时间段内对敏感权限的使用情况。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function getPermissionUsedRecord(    request: PermissionUsedRequest,    callback: AsyncCallback<PermissionUsedResponse>): void--><!--Device-privacyManager-function getPermissionUsedRecord(    request: PermissionUsedRequest,    callback: AsyncCallback<PermissionUsedResponse>): void-End-->

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [PermissionUsedRequest](arkts-ability-privacymanager-permissionusedrequest-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PermissionUsedResponse](arkts-ability-privacymanager-permissionusedresponse-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |

## 示例

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let request: privacyManager.PermissionUsedRequest = {
    'tokenId': 1, // 可以通过应用BundleInfo中的ApplicationInfo的accessTokenId字段获取。
    'isRemote': false,
    'deviceId': 'device',
    'bundleName': 'bundle',
    'permissionNames': [],
    'beginTime': 0,
    'endTime': 1,
    'flag': privacyManager.PermissionUsageFlag.FLAG_PERMISSION_USAGE_DETAIL,
};

// 查询历史权限使用记录
privacyManager.getPermissionUsedRecord(request, (err: BusinessError, data: privacyManager.PermissionUsedResponse) => {
  if (err) {
    console.error(`getPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`getPermissionUsedRecord success, result: ${data}`);
  }
});
```
