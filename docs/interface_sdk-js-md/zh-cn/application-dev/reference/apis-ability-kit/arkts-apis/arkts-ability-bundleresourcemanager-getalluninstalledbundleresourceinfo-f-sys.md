# getAllUninstalledBundleResourceInfo（系统接口）

## 导入模块

```TypeScript
import { bundleResourceManager } from 'kits/@kit.AbilityKit';
```

## getAllUninstalledBundleResourceInfo

```TypeScript
function getAllUninstalledBundleResourceInfo(resourceFlags: number): Promise<Array<BundleResourceInfo>>
```

根据给定的resourceFlags获取所有已卸载且保留数据的应用的BundleResourceInfo。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.GET_BUNDLE_RESOURCES

**系统能力：** SystemCapability.BundleManager.BundleFramework.Resource

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceFlags | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;BundleResourceInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
