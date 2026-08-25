# getOverlayModuleInfo

## 导入模块

```TypeScript
import { overlay } from 'kits/@kit.AbilityKit';
```

## getOverlayModuleInfo

```TypeScript
function getOverlayModuleInfo(moduleName: string, callback: AsyncCallback<OverlayModuleInfo>): void
```

获取当前应用中overlay特征module的OverlayModuleInfo信息。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;OverlayModuleInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700032](../errorcode-bundle.md#17700032-指定的应用不包含overlay特征的module) |
| [17700033](../errorcode-bundle.md#17700033-指定的module不是overlay特征的module) |


## getOverlayModuleInfo

```TypeScript
function getOverlayModuleInfo(moduleName: string): Promise<OverlayModuleInfo>
```

获取当前应用中overlay特征module的OverlayModuleInfo信息。使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;OverlayModuleInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700032](../errorcode-bundle.md#17700032-指定的应用不包含overlay特征的module) |
| [17700033](../errorcode-bundle.md#17700033-指定的module不是overlay特征的module) |
