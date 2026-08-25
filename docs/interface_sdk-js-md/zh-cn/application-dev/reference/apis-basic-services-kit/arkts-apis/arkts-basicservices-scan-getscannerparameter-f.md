# getScannerParameter

## 导入模块

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## getScannerParameter

```TypeScript
function getScannerParameter(scannerId: string): Promise<ScannerParameter[]>
```

获取扫描仪参数。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scannerId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ScannerParameter](arkts-basicservices-scan-scannerparameter-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
