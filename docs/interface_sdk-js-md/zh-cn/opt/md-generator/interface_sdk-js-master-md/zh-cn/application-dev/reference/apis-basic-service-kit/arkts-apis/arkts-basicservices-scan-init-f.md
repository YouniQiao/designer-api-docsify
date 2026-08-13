# init

## init

```TypeScript
function init(): Promise<void>
```

初始化扫描服务。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PRINT

<!--Device-scan-function init(): Promise<void>--><!--Device-scan-function init(): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

scan.init().then(() => {
    console.info('scan init success');
}).catch((error: BusinessError) => {
    console.error(`Failed to init scan. Code: ${error.code}, message: ${error.message}`);
});
```
