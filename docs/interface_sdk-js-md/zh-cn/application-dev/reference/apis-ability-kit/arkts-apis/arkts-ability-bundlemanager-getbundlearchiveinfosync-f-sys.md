# getBundleArchiveInfoSync（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getBundleArchiveInfoSync

```TypeScript
function getBundleArchiveInfoSync(hapFilePath: string, bundleFlags: number): BundleInfo
```

以同步方法根据给定的hapFilePath和bundleFlags获取BundleInfo对象。

**起始版本：** 10

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapFilePath | string | 是 |
| bundleFlags | number | 是 |

**返回值：**

| 类型 |
| --- |
| [BundleInfo](arkts-ability-bundleinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700022](../errorcode-bundle.md#17700022-输入的待解析源文件无效) |
