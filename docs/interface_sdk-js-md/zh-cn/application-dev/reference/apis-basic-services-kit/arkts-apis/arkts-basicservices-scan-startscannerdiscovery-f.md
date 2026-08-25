# startScannerDiscovery

## 导入模块

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## startScannerDiscovery

```TypeScript
function startScannerDiscovery(): Promise<void>
```

开始发现扫描仪。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.PRINT

**系统能力：** SystemCapability.Print.PrintFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
