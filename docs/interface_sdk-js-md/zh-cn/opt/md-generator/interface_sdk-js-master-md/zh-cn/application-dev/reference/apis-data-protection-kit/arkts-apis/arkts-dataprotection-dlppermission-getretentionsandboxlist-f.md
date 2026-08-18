# getRetentionSandboxList

## 导入模块

```TypeScript
```

## getRetentionSandboxList

```TypeScript
function getRetentionSandboxList(bundleName?: string): Promise<Array<RetentionSandboxInfo>>
```

查询指定应用的保留沙箱信息列表。仅支持在非DLP沙箱应用中调用。使用Promise异步回调。 该接口用于查询指定应用的保留沙箱列表，以便查看或管理当前处于保留状态的沙箱环境。

**起始版本：** 10

<!--Device-dlpPermission-function getRetentionSandboxList(bundleName?: string): Promise<Array<RetentionSandboxInfo>>--><!--Device-dlpPermission-function getRetentionSandboxList(bundleName?: string): Promise<Array<RetentionSandboxInfo>>-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[RetentionSandboxInfo](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100007](../errorcode-dlp.md#19100007-dlp沙箱应用不允许调用此接口) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |

**示例**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getRetentionSandboxList().then((sandboxList) => { // 获取沙箱保留列表。
  console.info('sandboxList', JSON.stringify(sandboxList));
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
});
```


## getRetentionSandboxList

```TypeScript
function getRetentionSandboxList(bundleName: string, callback: AsyncCallback<Array<RetentionSandboxInfo>>): void
```

查询指定应用的保留沙箱信息列表。仅支持在非DLP沙箱应用中调用。使用callback异步回调。 该接口用于查询指定应用的保留沙箱列表，以便查看或管理当前处于保留状态的沙箱环境。

**起始版本：** 10

<!--Device-dlpPermission-function getRetentionSandboxList(bundleName: string, callback: AsyncCallback<Array<RetentionSandboxInfo>>): void--><!--Device-dlpPermission-function getRetentionSandboxList(bundleName: string, callback: AsyncCallback<Array<RetentionSandboxInfo>>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[RetentionSandboxInfo](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100007](../errorcode-dlp.md#19100007-dlp沙箱应用不允许调用此接口) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |

**示例**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getRetentionSandboxList('bundleName', (err, sandboxList) => {
  if (err) {
    console.error(`Failed to get retention sandbox list. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('sandboxList', JSON.stringify(sandboxList));
  }
}); // 获取沙箱保留列表。
```


## getRetentionSandboxList

```TypeScript
function getRetentionSandboxList(callback: AsyncCallback<Array<RetentionSandboxInfo>>): void
```

查询当前应用的保留沙箱信息列表。使用callback异步回调。 该接口用于查询指定应用的保留沙箱列表，以便查看或管理当前处于保留状态的沙箱环境。仅支持在非DLP沙箱应用中调用。

**起始版本：** 10

<!--Device-dlpPermission-function getRetentionSandboxList(callback: AsyncCallback<Array<RetentionSandboxInfo>>): void--><!--Device-dlpPermission-function getRetentionSandboxList(callback: AsyncCallback<Array<RetentionSandboxInfo>>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[RetentionSandboxInfo](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100007](../errorcode-dlp.md#19100007-dlp沙箱应用不允许调用此接口) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |

**示例**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getRetentionSandboxList((err, retentionSandboxList) => {
  if (err) {
    console.error(`Failed to get retention sandbox list. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('retentionSandboxList', JSON.stringify(retentionSandboxList));
  }
}); // 获取沙箱保留列表。
```
