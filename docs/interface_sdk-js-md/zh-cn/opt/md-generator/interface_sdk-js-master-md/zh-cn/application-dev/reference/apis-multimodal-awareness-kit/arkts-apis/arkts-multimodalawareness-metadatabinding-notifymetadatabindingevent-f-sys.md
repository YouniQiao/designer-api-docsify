# notifyMetadataBindingEvent（系统接口）

## 导入模块

```TypeScript
```

## notifyMetadataBindingEvent

```TypeScript
function notifyMetadataBindingEvent(bundleName: string): Promise<string>
```

推送待嵌入的元数据信息给调用编码接口的应用或服务。系统会向指定包名的应用推送信息，并返回当前所在页面的applink信息，用于后续的编码处理。使用Promise异步回调。

**起始版本：** 23

<!--Device-metadataBinding-function notifyMetadataBindingEvent(bundleName: string): Promise<string>--><!--Device-metadataBinding-function notifyMetadataBindingEvent(bundleName: string): Promise<string>-End-->

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [32100001](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-文件创建失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';

// bundleName需为已安装应用的包名
let bundleName: string = '';
metadataBinding.notifyMetadataBindingEvent(bundleName).then((appLink:string) => {
  console.info('notify metadata:' + appLink);
}).catch((error: BusinessError) => {
  console.error(`Failed to notify metadata. Code: ${error.code}, message: ${error.message}`);
});
```
