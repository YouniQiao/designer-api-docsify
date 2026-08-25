# migrateData（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## migrateData

```TypeScript
function migrateData(sourcePaths: Array<string>, destinationPath: string): Promise<void>
```

拷贝文件，将文件从源路径拷贝到目标路径。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MIGRATE_DATA

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourcePaths | Array & lt;string & gt; | 是 |
| destinationPath | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700080](../errorcode-bundle.md#17700080-源路径中存在无效路径) |
| [17700081](../errorcode-bundle.md#17700081-目标路径为无效路径) |
| [17700082](../errorcode-bundle.md#17700082-用户身份认证失败) |
| [17700083](../errorcode-bundle.md#17700083-用户身份认证超时) |
| [17700084](../errorcode-bundle.md#17700084-源路径中存在未开启权限路径) |
| [17700085](../errorcode-bundle.md#17700085-目标路径未开启写权限) |
| [17700086](../errorcode-bundle.md#17700086-发生系统错误) |
