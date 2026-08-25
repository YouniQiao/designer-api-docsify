# isApplicationEnabledSync（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## isApplicationEnabledSync

```TypeScript
function isApplicationEnabledSync(bundleName: string): boolean
```

以同步方法获取指定应用的禁用或使能状态。

**起始版本：** 10

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
