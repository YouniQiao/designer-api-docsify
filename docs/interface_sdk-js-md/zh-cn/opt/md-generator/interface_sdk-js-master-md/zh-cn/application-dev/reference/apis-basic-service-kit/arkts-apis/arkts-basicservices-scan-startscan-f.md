# startScan

## startScan

```TypeScript
function startScan(scannerId: string, batchMode: boolean): Promise<void>
```

开始扫描。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PRINT

<!--Device-scan-function startScan(scannerId: string, batchMode: boolean): Promise<void>--><!--Device-scan-function startScan(scannerId: string, batchMode: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scannerId | string | 是 |
| batchMode | boolean | 是 |

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

let scannerId: string = 'scanner_001';
let batchMode: boolean = true;
scan.startScan(scannerId, batchMode).then(() => {
    console.info('start scan success');
}).catch((error: BusinessError) => {
    console.error(`Failed to start scan. Code: ${error.code}, message: ${error.message}`);
});
```
