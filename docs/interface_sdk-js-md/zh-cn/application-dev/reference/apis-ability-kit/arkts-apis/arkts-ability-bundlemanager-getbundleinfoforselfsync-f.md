# getBundleInfoForSelfSync

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getBundleInfoForSelfSync

```TypeScript
function getBundleInfoForSelfSync(bundleFlags: number): BundleInfo
```

以同步方法根据给定的bundleFlags获取当前应用的BundleInfo。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleFlags | number | 是 |

**返回值：**

| 类型 |
| --- |
| [BundleInfo](arkts-ability-bundleinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
