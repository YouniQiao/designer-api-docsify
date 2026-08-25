# grantUriPermission（系统接口）

## 导入模块

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
```

## grantUriPermission

```TypeScript
function grantUriPermission(
    uri: string,
    bundleName: string,
    flag: wantConstant.Flags,
    callback: AsyncCallback<void>
  ): void
```

为应用授予公共目录文件URI的临时访问权限，使用Callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.WRITE_MEDIA

**系统能力：** SystemCapability.FileManagement.AppFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| bundleName | string | 是 |
| flag | wantConstant.Flags | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14300001 |


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, bundleName: string, flag: wantConstant.Flags): Promise<void>
```

为应用授予公共目录文件URI的临时访问权限，使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.WRITE_MEDIA

**系统能力：** SystemCapability.FileManagement.AppFileService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| bundleName | string | 是 |
| flag | wantConstant.Flags | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14300001 |


## grantUriPermission

```TypeScript
function grantUriPermission(policies: Array<PolicyInfo>, targetBundleName: string, appCloneIndex: number): Promise<void>
```

给应用授予目标文件临时权限，使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.FILE_ACCESS_MANAGER

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| policies | Array&lt;[PolicyInfo](arkts-corefile-fileshare-policyinfo-i.md)&gt; | 是 |
| targetBundleName | string | 是 |
| appCloneIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 13900001 |
| 13900011 |
