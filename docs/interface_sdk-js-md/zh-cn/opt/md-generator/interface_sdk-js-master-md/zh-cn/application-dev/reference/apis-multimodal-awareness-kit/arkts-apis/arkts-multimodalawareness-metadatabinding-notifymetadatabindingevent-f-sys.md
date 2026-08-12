# notifyMetadataBindingEvent（系统接口）

## notifyMetadataBindingEvent

```TypeScript
function notifyMetadataBindingEvent(bundleName: string): Promise<string>
```

推送待嵌入的信息给调用编码接口的应用或服务。使用promise异步回调。

**起始版本：** 18

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
| [32100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-文件创建失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName: string = '';
metadataBinding.notifyMetadataBindingEvent(bundleName).then((appLink:string)=>{
  console.info('notify metadata:' + appLink);
}).catch((error: BusinessError) => {
  console.error(`Failed to notify metadata. Code: ${error.code}, message: ${error.message}`);
});
```
