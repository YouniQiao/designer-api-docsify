# getBundleArchiveInfo

## 导入模块

```TypeScript
import { bundle } from 'kits/@kit.AbilityKit';
```

## getBundleArchiveInfo

```TypeScript
function getBundleArchiveInfo(hapFilePath: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void
```

获取有关HAP中包含的应用程序包的信息，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapFilePath | string | 是 |
| bundleFlags | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)&gt; | 是 |


## getBundleArchiveInfo

```TypeScript
function getBundleArchiveInfo(hapFilePath: string, bundleFlags: number): Promise<BundleInfo>
```

获取有关HAP中包含的应用程序包的信息，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapFilePath | string | 是 |
| bundleFlags | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)&gt; |
