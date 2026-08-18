# exit

## 导入模块

```TypeScript
```

## exit

```TypeScript
function exit(): Promise<void>
```

退出扫描服务。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.PRINT

<!--Device-scan-function exit(): Promise<void>--><!--Device-scan-function exit(): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

```TypeScript
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

scan.exit().then(() => {
    console.info('scan exit success');
}).catch((error: BusinessError) => {
    console.error(`Failed to exit scan. Code: ${error.code}, message: ${error.message}`);
});
```
