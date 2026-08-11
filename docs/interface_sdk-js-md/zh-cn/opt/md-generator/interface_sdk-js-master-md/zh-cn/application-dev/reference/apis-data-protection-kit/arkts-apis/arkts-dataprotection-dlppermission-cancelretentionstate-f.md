# cancelRetentionState

## cancelRetentionState

```TypeScript
function cancelRetentionState(docUris: Array<string>): Promise<void>
```

取消沙箱保留状态，即恢复DLP文件关闭时自动卸载沙箱策略。使用Promise异步回调。

该接口用于取消沙箱保留状态，恢复默认行为以释放系统资源，适用于不再频繁访问DLP文件的场景。

**起始版本：** 10

<!--Device-dlpPermission-function cancelRetentionState(docUris: Array<string>): Promise<void>--><!--Device-dlpPermission-function cancelRetentionState(docUris: Array<string>): Promise<void>-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| docUris | Array&lt;string&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
dlpPermission.cancelRetentionState([uri]).then(() => { // 取消沙箱保留。
  console.info('success!');
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
});
```


## cancelRetentionState

```TypeScript
function cancelRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void
```

取消沙箱保留状态即恢复DLP文件关闭时自动卸载沙箱策略。使用callback异步回调。

该接口用于取消沙箱保留状态，恢复默认行为以释放系统资源，适用于不再频繁访问DLP文件的场景。

**起始版本：** 10

<!--Device-dlpPermission-function cancelRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void--><!--Device-dlpPermission-function cancelRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| docUris | Array&lt;string&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
dlpPermission.cancelRetentionState([uri], (err, res) => {
  if (err) {
    console.error(`Failed to cancel retention state. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('cancelRetentionState success');
  }
}); // 取消沙箱保留。
```
