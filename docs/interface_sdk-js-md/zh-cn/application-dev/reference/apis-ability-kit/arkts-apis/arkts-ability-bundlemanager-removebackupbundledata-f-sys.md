# removeBackupBundleData（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## removeBackupBundleData

```TypeScript
function removeBackupBundleData(bundleName: string, userId: number, appIndex: number): Promise<void>
```

删除指定用户下指定应用或分身应用的备份数据。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.CLEAN_APPLICATION_DATA

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| userId | number | 是 |
| appIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
