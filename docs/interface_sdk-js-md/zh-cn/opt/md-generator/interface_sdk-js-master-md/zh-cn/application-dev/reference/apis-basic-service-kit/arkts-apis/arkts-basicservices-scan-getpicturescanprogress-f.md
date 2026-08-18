# getPictureScanProgress

## 导入模块

```TypeScript
```

## getPictureScanProgress

```TypeScript
function getPictureScanProgress(scannerId: string): Promise<PictureScanProgress>
```

获取图片扫描进度。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.PRINT

<!--Device-scan-function getPictureScanProgress(scannerId: string): Promise<PictureScanProgress>--><!--Device-scan-function getPictureScanProgress(scannerId: string): Promise<PictureScanProgress>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scannerId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PictureScanProgress](arkts-basicservices-scan-picturescanprogress-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

```TypeScript
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
scan.getPictureScanProgress(scannerId).then((progress: scan.PictureScanProgress) => {
    console.info('get picture scan progress success: ' + JSON.stringify(progress));
}).catch((error: BusinessError) => {
    console.error(`Failed to get picture scan progress. Code: ${error.code}, message: ${error.message}`);
});
```
