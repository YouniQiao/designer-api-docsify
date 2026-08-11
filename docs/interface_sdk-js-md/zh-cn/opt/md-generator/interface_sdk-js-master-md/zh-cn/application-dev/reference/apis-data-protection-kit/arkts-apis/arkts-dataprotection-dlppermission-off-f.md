# off

## off('openDLPFile')

```TypeScript
function off(type: 'openDLPFile', listener?: Callback<AccessedDLPFileInfo>): void
```

取消监听打开DLP文件。仅支持在非DLP沙箱应用中调用。调用成功后，将不再接收DLP文件打开事件的通知。

该接口通常在页面销毁或不再需要监听时调用以释放资源。

**起始版本：** 10

<!--Device-dlpPermission-function off(type: 'openDLPFile', listener?: Callback<AccessedDLPFileInfo>): void--><!--Device-dlpPermission-function off(type: 'openDLPFile', listener?: Callback<AccessedDLPFileInfo>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'openDLPFile' | 是 |
| listener | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AccessedDLPFileInfo&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100007](../errorcode-dlp.md#19100007-dlp沙箱应用不允许调用此接口) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.off('openDLPFile', (info: dlpPermission.AccessedDLPFileInfo) => {
  console.info('openDlpFile event', info.uri, info.lastOpenTime);
}); // 取消订阅。
```
