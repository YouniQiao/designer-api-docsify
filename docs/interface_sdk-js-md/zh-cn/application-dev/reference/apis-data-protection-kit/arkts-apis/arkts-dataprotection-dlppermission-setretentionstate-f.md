# setRetentionState

## 导入模块

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## setRetentionState

```TypeScript
function setRetentionState(docUris: Array<string>): Promise<void>
```

设置DLP沙箱的保留状态。默认情况下，打开DLP文件时系统会自动创建沙箱环境，关闭文件后自动销毁沙箱。设置保留状态后，即使关闭DLP文件，沙箱环境也会保留，便于快速重新打开相同DLP文件。适用于需要频繁操作同一DLP文件的场景 ，可提升文件打开效率。仅支持在DLP沙箱应用中调用。使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [docUris](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md) | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100006](../errorcode-dlp.md#19100006-非dlp沙箱应用) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |


## setRetentionState

```TypeScript
function setRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void
```

设置DLP沙箱的保留状态。默认情况下，打开DLP文件时系统会自动创建沙箱环境，关闭文件后自动销毁沙箱。设置保留状态后，即使关闭DLP文件，沙箱环境也会保留，便于快速重新打开相同DLP文件。适用于需要频繁操作同一DLP文件的场景 ，可提升文件打开效率。仅支持在DLP沙箱应用中调用。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [docUris](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md) | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100006](../errorcode-dlp.md#19100006-非dlp沙箱应用) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |
