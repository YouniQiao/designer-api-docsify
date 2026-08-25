# getBundleInfoSync

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getBundleInfoSync

```TypeScript
function getBundleInfoSync(bundleName: string, bundleFlags: number, userId: number): BundleInfo
```

以同步方法根据给定的bundleName、bundleFlags和userId获取BundleInfo。获取调用方自身的信息时不需要权限。

**起始版本：** 14

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| bundleFlags | number | 是 |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [BundleInfo](arkts-ability-bundleinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700026](../errorcode-bundle.md#17700026-指定应用被禁用) |


## getBundleInfoSync

```TypeScript
function getBundleInfoSync(bundleName: string, bundleFlags: number): BundleInfo
```

以同步方法根据给定的bundleName、bundleFlags获取调用方所在用户下的BundleInfo。获取调用方自身的信息时不需要权限。

**起始版本：** 14

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| bundleFlags | number | 是 |

**返回值：**

| 类型 |
| --- |
| [BundleInfo](arkts-ability-bundleinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700026](../errorcode-bundle.md#17700026-指定应用被禁用) |
